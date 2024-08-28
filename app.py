app_url = "https://b6a405e449777e6edf.gradio.live/"
Language='English'
# Language='English'# @param ['English','Hindi','Bengali','Afrikaans', 'Amharic', 'Arabic', 'Azerbaijani', 'Bulgarian', 'Bosnian', 'Catalan', 'Czech', 'Welsh', 'Danish', 'German', 'Greek', 'Spanish', 'French', 'Irish', 'Galician', 'Gujarati', 'Hebrew', 'Croatian', 'Hungarian', 'Indonesian', 'Icelandic', 'Italian', 'Japanese', 'Javanese', 'Georgian', 'Kazakh', 'Khmer', 'Kannada', 'Korean', 'Lao', 'Lithuanian', 'Latvian', 'Macedonian', 'Malayalam', 'Mongolian', 'Marathi', 'Malay', 'Maltese', 'Burmese', 'Norwegian Bokmål', 'Nepali', 'Dutch', 'Polish', 'Pashto', 'Portuguese', 'Romanian', 'Russian', 'Sinhala', 'Slovak', 'Slovenian', 'Somali', 'Albanian', 'Serbian', 'Sundanese', 'Swedish', 'Swahili', 'Tamil', 'Telugu', 'Thai', 'Turkish', 'Ukrainian', 'Urdu', 'Uzbek', 'Vietnamese', 'Chinese', 'Zulu']

#bot name is 'meta'
# bot_name_bad_pronunciation=["meta",'meetha',"metre","matter"]

import pyaudio
import cv2
import numpy as np
import math
import os
import shutil
from PIL import Image
import simpleaudio as sa
import threading
import time
import pysrt
import speech_recognition as sr
from gradio_client import Client, file
from pydub import AudioSegment
from microsoft_tts import edge_tts_pipeline
from dotenv import load_dotenv
from dotenv import dotenv_values
from deep_translator import GoogleTranslator
config = dotenv_values(".env")
username=config['USERNAME']
password=config['PASSWORD']


# Constants and initializations
video_width = 640
video_height = 480
# wave_height = 200
wave_height = 300

background_color = (0, 0, 0)
wave_color = (92, 230, 92)  # RGB color for the wave
wave_screen_width = video_width
wave_screen_height = wave_height

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)


try:
    client = Client(app_url,auth=[str(username), str(password)])
except Exception as e:
    print(f"Error: Could not connect to the server. {e}")

# Directory creation
os.makedirs("./compressed_image", exist_ok=True)
os.makedirs("./audio", exist_ok=True)
import textwrap
from PIL import ImageFont, ImageDraw
def pill_text(image, text, position,font_path, font_size=40, font_color=(255, 255, 255)):
    image=Image.fromarray(image)
    font = ImageFont.truetype(font_path, font_size)
    draw = ImageDraw.Draw(image)
    draw.text(position, text, font=font, fill=font_color)
    image = np.array(image)
    return image
play_obj = None
subtitles = None
current_prompt = ""
audio_start_time = None
class AudioVisualizer:
    @staticmethod
    def tts(text, Language='English', local_save_path=''):
        Gender = "Female"
        edge_save_path = edge_tts_pipeline(text, Language, Gender, tts_save_path='')
        srt_file_path = edge_save_path.replace('.wav', '.srt')

        if os.path.exists(srt_file_path):
            if local_save_path:
                temp_srt_file_path = local_save_path.replace('.wav', '.srt')
                shutil.copyfile(edge_save_path, local_save_path)
                shutil.copyfile(srt_file_path, temp_srt_file_path)
                return local_save_path, temp_srt_file_path
            else:
                return edge_save_path, srt_file_path
        else:
            if local_save_path:
                shutil.copyfile(edge_save_path, local_save_path)
                return local_save_path, ''
            else:
                return edge_save_path, ''

    @staticmethod
    def generate_image_name():
        return f'./compressed_image/temp.jpg'

    @staticmethod
    def compress_image(frame, quality=50):
        if frame is not None and frame.size > 0:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            convert_pil = Image.fromarray(frame_rgb)
            output_image_path = AudioVisualizer.generate_image_name()
            convert_pil.save(output_image_path, optimize=True, quality=quality)
            return output_image_path
        return None

    @staticmethod
    def play_audio(filename):
        global play_obj, audio_start_time
        try:
            wave_obj = sa.WaveObject.from_wave_file(filename)
            play_obj = wave_obj.play()
            audio_start_time = time.time()  # Record the start time of the audio playback
            return play_obj
        except Exception as e:
            print(f"Error playing audio: {e}")
            return None
        
    @staticmethod
    def draw_sine_wave(amplitude, subtitle_text="", max_words_per_line=5):
        global wave_screen_height, wave_screen_width
        image = np.zeros((wave_screen_height, wave_screen_width, 3), dtype=np.uint8)
        image[:] = background_color
        # wave_screen_height=200
        points = []
        if amplitude > 10:
            for x in range(0, wave_screen_width):
                y = int(wave_screen_height / 2 + amplitude * math.sin(x * 0.02))
                points.append((x, y))
        else:
            points.append((0, wave_screen_height // 2))
            points.append((wave_screen_width, wave_screen_height // 2))

        for i in range(len(points) - 1):
            cv2.line(image, points[i], points[i + 1], wave_color, 2)

        if subtitle_text:
            words = subtitle_text.split()
            wrapped_text = []
            while len(words) > max_words_per_line:
                wrapped_text.append(' '.join(words[:max_words_per_line]))
                words = words[max_words_per_line:]
            wrapped_text.append(' '.join(words))
            for i, line in enumerate(wrapped_text):
                y_position = wave_screen_height - 50 - (i * 30)
                if Language=="English":
                    cv2.putText(image, line, (100, y_position), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
                elif Language=="Bengali":
                    image=pill_text(image, line, (100, y_position), font_path='Bengali.ttf', font_size=20, font_color=(255, 255, 255))
                else:
                    return image

        return image

    @staticmethod
    def get_microphone_input_level():
        data = stream.read(CHUNK, exception_on_overflow=False)
        rms = 0
        for i in range(0, len(data), 2):
            sample = int.from_bytes(data[i:i+2], byteorder='little', signed=True)
            rms += sample**2
        rms = math.sqrt(rms / CHUNK)
        return rms
import json
with open('language_code.json') as f:
    languages = json.load(f)
def describe_image(prompt, image_file):
    if not prompt:
        prompt = "Describe the image in a single sentence"
    # result = prompt
    # Uncomment after testing
    result = client.predict(prompt, file(image_file), api_name="/predict")
    
    audio_path, srt_path = AudioVisualizer.tts(str(result), Language=Language , local_save_path='./temp.wav')
    print(f"Audio path: {audio_path}, SRT path: {srt_path}")
    global subtitles
    if os.path.exists(srt_path):
        subtitles = pysrt.open(srt_path)
    play_obj = AudioVisualizer.play_audio(audio_path)
    return play_obj, subtitles

def translate_text(text, Language):
    global languages    
    # print("calling translate")
    target_language=languages[Language]
    if Language == "Chinese":
          target_language='zh-CN'
    translator = GoogleTranslator(target=target_language)
    translation = translator.translate(text.strip())
    t_text=str(translation)
    # print(f"{t_text}---{Language}----{target_language}")
    return t_text


def speech_recognition():
# def speech_recognition(frame):
    global current_prompt,Language
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 2000
    recognizer.pause_threshold = 1
    recognizer.phrase_time_limit = 0.1
    recognizer.dynamic_energy_threshold = True

    while True:
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)
                # AudioVisualizer.play_audio("./ready.wav")
                print("Listening...")
                audio_data = recognizer.listen(source, timeout=10, phrase_time_limit=None)
                text = recognizer.recognize_google(audio_data, language=languages[Language])
                print("You said:", text)
                upload_image = AudioVisualizer.compress_image(frame)
                print(f"Image: {upload_image}")
                # if upload_image:
                if Language != 'English':
                    text=translate_text(text, 'English')
                    print(f"Translate Recognition: {text}")
                pronunciations = bot_name_bad_pronunciation  # Add any variations you want to consider

                matching_variation = next((variation for variation in pronunciations if variation in text.lower()), None)

                if matching_variation and upload_image:
                    prompt=text.lower().replace(matching_variation, "")
                    print(f"Prompt: {prompt}")
                    describe_image(prompt, upload_image)
    
        except Exception as e:
            print(e)
            continue

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open video capture.")
        exit()

    frame = None

    # Start the speech recognition thread
    # speech_thread = threading.Thread(target=speech_recognition, args=(frame,))
    speech_thread = threading.Thread(target=speech_recognition)

    speech_thread.start()

    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        if not ret:
            print("Error: Could not read frame.")
            continue

        amplitude_adjustment = AudioVisualizer.get_microphone_input_level() / 50
        amplitude = max(10, amplitude_adjustment)
        wave_image = AudioVisualizer.draw_sine_wave(amplitude)
        
        # Calculate the elapsed time since the audio started playing
        elapsed_time = time.time() - audio_start_time if play_obj and play_obj.is_playing() else None
        subtitle_text = ""
        
        if elapsed_time and subtitles:
            for sub in subtitles:
                start_sec = sub.start.seconds + sub.start.milliseconds / 1000.0
                end_sec = sub.end.seconds + sub.end.milliseconds / 1000.0
                if start_sec <= elapsed_time <= end_sec:
                    subtitle_text = sub.text
                    break
        
        wave_image_with_subtitle = AudioVisualizer.draw_sine_wave(amplitude, subtitle_text)

        if frame is not None and wave_image_with_subtitle is not None:
            combined_frame = np.vstack((frame, wave_image_with_subtitle))
            cv2.imshow('Webcam with Wave Sign', combined_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # Check if audio playback is done
        if play_obj and not play_obj.is_playing():
            play_obj = None
            subtitles = None
            current_prompt = ""

    cap.release()
    cv2.destroyAllWindows()
    stream.stop_stream()
    stream.close()
    p.terminate()
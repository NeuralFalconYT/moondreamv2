#@title <-- Just run the cell (config edge TTS)
edge_folder="."
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

from deep_translator import GoogleTranslator

languages = {
    "Afrikaans": "af",
    "Amharic": "am",
    "Arabic": "ar",
    "Azerbaijani": "az",
    "Bulgarian": "bg",
    "Bengali": "bn",
    "Bosnian": "bs",
    "Catalan": "ca",
    "Czech": "cs",
    "Welsh": "cy",
    "Danish": "da",
    "German": "de",
    "Greek": "el",
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "Irish": "ga",
    "Galician": "gl",
    "Gujarati": "gu",
    "Hebrew": "he",
    "Hindi": "hi",
    "Croatian": "hr",
    "Hungarian": "hu",
    "Indonesian": "id",
    "Icelandic": "is",
    "Italian": "it",
    "Japanese": "ja",
    "Javanese": "jv",
    "Georgian": "ka",
    "Kazakh": "kk",
    "Khmer": "km",
    "Kannada": "kn",
    "Korean": "ko",
    "Lao": "lo",
    "Lithuanian": "lt",
    "Latvian": "lv",
    "Macedonian": "mk",
    "Malayalam": "ml",
    "Mongolian": "mn",
    "Marathi": "mr",
    "Malay": "ms",
    "Maltese": "mt",
    "Burmese": "my",
    "Norwegian Bokmål": "nb",
    "Nepali": "ne",
    "Dutch": "nl",
    "Polish": "pl",
    "Pashto": "ps",
    "Portuguese": "pt",
    "Romanian": "ro",
    "Russian": "ru",
    "Sinhala": "si",
    "Slovak": "sk",
    "Slovenian": "sl",
    "Somali": "so",
    "Albanian": "sq",
    "Serbian": "sr",
    "Sundanese": "su",
    "Swedish": "sv",
    "Swahili": "sw",
    "Tamil": "ta",
    "Telugu": "te",
    "Thai": "th",
    "Turkish": "tr",
    "Ukrainian": "uk",
    "Urdu": "ur",
    "Uzbek": "uz",
    "Vietnamese": "vi",
    "Chinese": "zh",
    "Zulu": "zu"
}

def translate_text(text, Language):
    # print("calling translate")
    target_language=languages[Language]
    if Language == "Chinese":
          target_language='zh-CN'
    translator = GoogleTranslator(target=target_language)
    translation = translator.translate(text.strip())
    t_text=str(translation)
    # print(f"{t_text}---{Language}----{target_language}")
    return t_text


female_voice_list={'Vietnamese': 'vi-VN-HoaiMyNeural',
 'Bengali': 'bn-BD-NabanitaNeural',
 'Thai': 'th-TH-PremwadeeNeural',
 'English': 'en-AU-NatashaNeural',
 'Portuguese': 'pt-BR-FranciscaNeural',
 'Arabic': 'ar-AE-FatimaNeural',
 'Turkish': 'tr-TR-EmelNeural',
 'Spanish': 'es-AR-ElenaNeural',
 'Korean': 'ko-KR-SunHiNeural',
 'French': 'fr-BE-CharlineNeural',
 'Indonesian': 'id-ID-GadisNeural',
 'Russian': 'ru-RU-SvetlanaNeural',
 'Hindi': 'hi-IN-SwaraNeural',
 'Japanese': 'ja-JP-NanamiNeural',
 'Afrikaans': 'af-ZA-AdriNeural',
 'Amharic': 'am-ET-MekdesNeural',
 'Azerbaijani': 'az-AZ-BanuNeural',
 'Bulgarian': 'bg-BG-KalinaNeural',
 'Bosnian': 'bs-BA-VesnaNeural',
 'Catalan': 'ca-ES-JoanaNeural',
 'Czech': 'cs-CZ-VlastaNeural',
 'Welsh': 'cy-GB-NiaNeural',
 'Danish': 'da-DK-ChristelNeural',
 'German': 'de-AT-IngridNeural',
 'Greek': 'el-GR-AthinaNeural',
 'Irish': 'ga-IE-OrlaNeural',
 'Galician': 'gl-ES-SabelaNeural',
 'Gujarati': 'gu-IN-DhwaniNeural',
 'Hebrew': 'he-IL-HilaNeural',
 'Croatian': 'hr-HR-GabrijelaNeural',
 'Hungarian': 'hu-HU-NoemiNeural',
 'Icelandic': 'is-IS-GudrunNeural',
 'Italian': 'it-IT-ElsaNeural',
 'Javanese': 'jv-ID-SitiNeural',
 'Georgian': 'ka-GE-EkaNeural',
 'Kazakh': 'kk-KZ-AigulNeural',
 'Khmer': 'km-KH-SreymomNeural',
 'Kannada': 'kn-IN-SapnaNeural',
 'Lao': 'lo-LA-KeomanyNeural',
 'Lithuanian': 'lt-LT-OnaNeural',
 'Latvian': 'lv-LV-EveritaNeural',
 'Macedonian': 'mk-MK-MarijaNeural',
 'Malayalam': 'ml-IN-SobhanaNeural',
 'Mongolian': 'mn-MN-YesuiNeural',
 'Marathi': 'mr-IN-AarohiNeural',
 'Malay': 'ms-MY-YasminNeural',
 'Maltese': 'mt-MT-GraceNeural',
 'Burmese': 'my-MM-NilarNeural',
 'Norwegian Bokmål': 'nb-NO-PernilleNeural',
 'Nepali': 'ne-NP-HemkalaNeural',
 'Dutch': 'nl-BE-DenaNeural',
 'Polish': 'pl-PL-ZofiaNeural',
 'Pashto': 'ps-AF-LatifaNeural',
 'Romanian': 'ro-RO-AlinaNeural',
 'Sinhala': 'si-LK-ThiliniNeural',
 'Slovak': 'sk-SK-ViktoriaNeural',
 'Slovenian': 'sl-SI-PetraNeural',
 'Somali': 'so-SO-UbaxNeural',
 'Albanian': 'sq-AL-AnilaNeural',
 'Serbian': 'sr-RS-SophieNeural',
 'Sundanese': 'su-ID-TutiNeural',
 'Swedish': 'sv-SE-SofieNeural',
 'Swahili': 'sw-KE-ZuriNeural',
 'Tamil': 'ta-IN-PallaviNeural',
 'Telugu': 'te-IN-ShrutiNeural',
 'Chinese': 'zh-CN-XiaoxiaoNeural',
 'Ukrainian': 'uk-UA-PolinaNeural',
 'Urdu': 'ur-IN-GulNeural',
 'Uzbek': 'uz-UZ-MadinaNeural',
 'Zulu': 'zu-ZA-ThandoNeural'}
male_voice_list= {'Vietnamese': 'vi-VN-NamMinhNeural',
 'Bengali': 'bn-BD-PradeepNeural',
 'Thai': 'th-TH-NiwatNeural',
 'English': 'en-US-BrianMultilingualNeural',
 'Portuguese': 'pt-BR-AntonioNeural',
 'Arabic': 'ar-AE-HamdanNeural',
 'Turkish': 'tr-TR-AhmetNeural',
 'Spanish': 'es-AR-TomasNeural',
 'Korean': 'ko-KR-HyunsuNeural',
 'French': 'fr-BE-GerardNeural',
 'Indonesian': 'id-ID-ArdiNeural',
 'Russian': 'ru-RU-DmitryNeural',
 'Hindi': 'hi-IN-MadhurNeural',
 'Japanese': 'ja-JP-KeitaNeural',
 'Afrikaans': 'af-ZA-WillemNeural',
 'Amharic': 'am-ET-AmehaNeural',
 'Azerbaijani': 'az-AZ-BabekNeural',
 'Bulgarian': 'bg-BG-BorislavNeural',
 'Bosnian': 'bs-BA-GoranNeural',
 'Catalan': 'ca-ES-EnricNeural',
 'Czech': 'cs-CZ-AntoninNeural',
 'Welsh': 'cy-GB-AledNeural',
 'Danish': 'da-DK-JeppeNeural',
 'German': 'de-AT-JonasNeural',
 'Greek': 'el-GR-NestorasNeural',
 'Irish': 'ga-IE-ColmNeural',
 'Galician': 'gl-ES-RoiNeural',
 'Gujarati': 'gu-IN-NiranjanNeural',
 'Hebrew': 'he-IL-AvriNeural',
 'Croatian': 'hr-HR-SreckoNeural',
 'Hungarian': 'hu-HU-TamasNeural',
 'Icelandic': 'is-IS-GunnarNeural',
 'Italian': 'it-IT-DiegoNeural',
 'Javanese': 'jv-ID-DimasNeural',
 'Georgian': 'ka-GE-GiorgiNeural',
 'Kazakh': 'kk-KZ-DauletNeural',
 'Khmer': 'km-KH-PisethNeural',
 'Kannada': 'kn-IN-GaganNeural',
 'Lao': 'lo-LA-ChanthavongNeural',
 'Lithuanian': 'lt-LT-LeonasNeural',
 'Latvian': 'lv-LV-NilsNeural',
 'Macedonian': 'mk-MK-AleksandarNeural',
 'Malayalam': 'ml-IN-MidhunNeural',
 'Mongolian': 'mn-MN-BataaNeural',
 'Marathi': 'mr-IN-ManoharNeural',
 'Malay': 'ms-MY-OsmanNeural',
 'Maltese': 'mt-MT-JosephNeural',
 'Burmese': 'my-MM-ThihaNeural',
 'Norwegian Bokmål': 'nb-NO-FinnNeural',
 'Nepali': 'ne-NP-SagarNeural',
 'Dutch': 'nl-BE-ArnaudNeural',
 'Polish': 'pl-PL-MarekNeural',
 'Pashto': 'ps-AF-GulNawazNeural',
 'Romanian': 'ro-RO-EmilNeural',
 'Sinhala': 'si-LK-SameeraNeural',
 'Slovak': 'sk-SK-LukasNeural',
 'Slovenian': 'sl-SI-RokNeural',
 'Somali': 'so-SO-MuuseNeural',
 'Albanian': 'sq-AL-IlirNeural',
 'Serbian': 'sr-RS-NicholasNeural',
 'Sundanese': 'su-ID-JajangNeural',
 'Swedish': 'sv-SE-MattiasNeural',
 'Swahili': 'sw-KE-RafikiNeural',
 'Tamil': 'ta-IN-ValluvarNeural',
 'Telugu': 'te-IN-MohanNeural',
 'Chinese': 'zh-CN-YunjianNeural',
 'Ukrainian': 'uk-UA-OstapNeural',
 'Urdu': 'ur-IN-SalmanNeural',
 'Uzbek': 'uz-UZ-SardorNeural',
 'Zulu': 'zu-ZA-ThembaNeural'}

def chunks_sentences(paragraph, join_limit=2):
    sentences = sent_tokenize(paragraph)
    # Initialize an empty list to store the new sentences
    new_sentences = []

    # Iterate through the list of sentences in steps of 'join_limit'
    for i in range(0, len(sentences), join_limit):
        # Join the sentences with a space between them
        new_sentence = ' '.join(sentences[i:i + join_limit])
        new_sentences.append(new_sentence)
    return new_sentences


def calculate_rate_string(input_value):
    rate = (input_value - 1) * 100
    sign = '+' if input_value >= 1 else '-'
    return f"{sign}{abs(int(rate))}"


def make_chunks(input_text, language):
    language="English"
    if language == "English":
      filtered_list=chunks_sentences(input_text, join_limit=2)
      # temp_list = input_text.strip().split(".")
      # filtered_list = [element.strip() + '.' for element in temp_list[:-1] if element.strip() and element.strip() != "'" and element.strip() != '"']
      # if temp_list[-1].strip():
      #     filtered_list.append(temp_list[-1].strip())
      return filtered_list




import re
import uuid
def tts_file_name(text):
    if text.endswith("."):
        text = text[:-1]
    text = text.lower()
    text = text.strip()
    text = text.replace(" ","_")
    truncated_text = text[:25] if len(text) > 25 else text if len(text) > 0 else "empty"
    random_string = uuid.uuid4().hex[:8].upper()
    file_name = f"{edge_folder}/edge_tts_voice/{truncated_text}_{random_string}.mp3"
    return file_name


from pydub import AudioSegment
import shutil
import os
def merge_audio_files(audio_paths, output_path):
    # Initialize an empty AudioSegment
    merged_audio = AudioSegment.silent(duration=0)

    # Iterate through each audio file path
    for audio_path in audio_paths:
        # Load the audio file using Pydub
        audio = AudioSegment.from_file(audio_path)

        # Append the current audio file to the merged_audio
        merged_audio += audio

    # Export the merged audio to the specified output path
    merged_audio.export(output_path, format="mp3")


from datetime import timedelta

def add_time_to_timestamp(timestamp, add_time):
    """Add a timedelta to a timestamp string."""
    # Convert VTT/SRT timestamp to timedelta
    time_parts = timestamp.split(' --> ')
    start_time = time_parts[0].strip().replace('.', ',')
    end_time = time_parts[1].strip().replace('.', ',')

    def parse_time(time_str):
        """Convert timestamp string to timedelta."""
        hours, minutes, seconds = time_str.split(':')
        seconds, milliseconds = seconds.split(',')
        return timedelta(hours=int(hours),
                         minutes=int(minutes),
                         seconds=int(seconds),
                         milliseconds=int(milliseconds))
    
    start_dt = parse_time(start_time)
    end_dt = parse_time(end_time)

    # Add the fixed duration
    add_td = timedelta(hours=int(add_time.split(':')[0]),
                       minutes=int(add_time.split(':')[1]),
                       seconds=int(add_time.split(':')[2]),
                       milliseconds=int(add_time.split(':')[3]))

    new_start_dt = start_dt + add_td
    new_end_dt = end_dt + add_td

    # Convert back to timestamp format
    def timedelta_to_str(td):
        total_seconds = int(td.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        milliseconds = int(td.microseconds / 1000)
        return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"

    return f"{timedelta_to_str(new_start_dt)} --> {timedelta_to_str(new_end_dt)}"

def vtt_to_srt(vtt_file_path, srt_file_path, add_time="00:00:00:00"):
    # Open the VTT file with UTF-8 encoding and handle errors
    with open(vtt_file_path, 'r', encoding='utf-8', errors='replace') as vtt_file:
        vtt_lines = vtt_file.readlines()
    
    srt_lines = []
    index = 1
    for line in vtt_lines:
        line = line.strip()

        # Skip the WEBVTT header and any empty lines
        if line == "WEBVTT" or line == "":
            continue
        
        # Convert VTT timestamp to SRT format
        if "-->" in line:
            timestamp = add_time_to_timestamp(line, add_time)  # Add time to timestamp
            srt_lines.append(f"{index}")  # Add subtitle index
            srt_lines.append(timestamp)   # Add timestamp line
            index += 1
        else:
            # Add the subtitle text
            srt_lines.append(line)
        
        # Ensure there is a blank line after each subtitle entry in SRT format
        if line != "" and "-->" not in line:
            srt_lines.append("")  

    # Write the SRT lines to the output file with UTF-8 encoding
    with open(srt_file_path, 'w', encoding='utf-8') as srt_file:
        srt_file.write("\n".join(srt_lines))
        
        
        
# def vtt_to_srt(vtt_file_path, srt_file_path):
#     # Open the VTT file with UTF-8 encoding and handle errors
#     with open(vtt_file_path, 'r', encoding='utf-8', errors='replace') as vtt_file:
#         vtt_lines = vtt_file.readlines()
    
#     srt_lines = []
#     index = 1
#     for line in vtt_lines:
#         line = line.strip()

#         # Skip the WEBVTT header and any empty lines
#         if line == "WEBVTT" or line == "":
#             continue
        
#         # Convert VTT timestamp to SRT format
#         if "-->" in line:
#             timestamp = line.replace('.', ',')  # Convert '.' to ',' in the timestamp
#             srt_lines.append(f"{index}")  # Add subtitle index
#             srt_lines.append(timestamp)   # Add timestamp line
#             index += 1
#         else:
#             # Add the subtitle text
#             srt_lines.append(line)
        
#         # Ensure there is a blank line after each subtitle entry in SRT format
#         if line != "" and "-->" not in line:
#             srt_lines.append("")  

#     # Write the SRT lines to the output file with UTF-8 encoding
#     with open(srt_file_path, 'w', encoding='utf-8') as srt_file:
#         srt_file.write("\n".join(srt_lines))

from pydub import AudioSegment
import srt
from datetime import timedelta

def adjust_srt_timestamps(subtitles, time_offset):
    """ Adjust SRT subtitles timestamps by adding a time offset """
    for subtitle in subtitles:
        subtitle.start += time_offset
        subtitle.end += time_offset
    return subtitles

def srt_marge(audio_list, save_srt_path):
    """ Merge audio files and adjust SRT timestamps based on audio duration """
    
    def get_audio_duration(file_path):
      """ Get the duration of an audio file """
      audio = AudioSegment.from_file(file_path)  # This handles various formats including .mp3
      return timedelta(milliseconds=len(audio))
    
    # Initialize total offset and list for all subtitles
    total_offset = timedelta()
    all_subtitles = []
    
    # Process each audio and SRT file
    for audio_file in audio_list:
        # Calculate the duration of the current audio file
        audio_duration = get_audio_duration(audio_file)
        srt_file = audio_file.replace('.mp3', '.srt')
        
        # Read and adjust the SRT file
        with open(srt_file, "r", encoding="utf-8") as f:
            subtitles = list(srt.parse(f.read()))
        
        # Adjust subtitles based on the current total offset
        adjusted_subtitles = adjust_srt_timestamps(subtitles, total_offset)
        all_subtitles.extend(adjusted_subtitles)
        
        # Update total offset for the next SRT file
        total_offset += audio_duration
    
    # Convert subtitles to SRT format and write to the output file
    with open(save_srt_path, "w", encoding="utf-8") as f:
        f.write(srt.compose(all_subtitles))
    

    
    print(f"Merging Srt completed! Output files: {save_srt_path}")
        
def edge_free_tts(chunks_list,speed,voice_name,save_path,translate_text_flag,Language):
  # print(voice_name)
  # print(chunks_list)
  store_text=""
  vtt_path=save_path.lower().replace(".mp3",".vtt")
  srt_file_path=save_path.lower().replace(".mp3",".srt")
 
  if len(chunks_list)>1:
    chunk_audio_list=[]
    if os.path.exists(f"{edge_folder}/edge_tts_voice"):
      shutil.rmtree(f"{edge_folder}/edge_tts_voice")
    os.mkdir(f"{edge_folder}/edge_tts_voice")
    k=1
    for i in chunks_list:
      # print(i)
      if translate_text_flag:
        text=translate_text(i, Language)
      else:
        text=i
      store_text+=text+" "
      text=text.replace('"',"")
      edge_command=f'edge-tts  --rate={calculate_rate_string(speed)}% --voice {voice_name} --text "{text}" --write-media {edge_folder}/edge_tts_voice/{k}.mp3 --write-subtitles {edge_folder}/edge_tts_voice/{k}.vtt'
      var1=os.system(edge_command)
      if var1==0:
        # pass
        vtt_to_srt(f"{edge_folder}/edge_tts_voice/{k}.vtt", f"{edge_folder}/edge_tts_voice/{k}.srt", add_time="00:00:00:0")
      
      
      else:
        print(f"Failed: {i}")
        print(edge_command)
      chunk_audio_list.append(f"{edge_folder}/edge_tts_voice/{k}.mp3")
      k+=1
    # print(chunk_audio_list)
    merge_audio_files(chunk_audio_list, save_path)
    srt_marge(chunk_audio_list, srt_file_path)
  else:
    if translate_text_flag:
      text=translate_text(chunks_list[0], Language)
    else:
      text=chunks_list[0]
    text=text.replace('"',"")
    store_text+=text+" "
    edge_command=f'edge-tts  --rate={calculate_rate_string(speed)}% --voice {voice_name} --text "{text}" --write-media {save_path} --write-subtitles {vtt_path}'
    var2=os.system(edge_command)
    if var2==0:
      # pass
      vtt_to_srt(vtt_path, srt_file_path,add_time="00:00:00:0")
    else:
      print(f"Failed: {chunks_list[0]}")
      print(edge_command)
  with open("./temp.txt", "w", encoding="utf-8") as text_file:
    text_file.write(store_text)
  return save_path


# speed = 1  # @param {type: "number"}
# translate_text_flag  = True # @param {type:"boolean"}
# long_sentence = True # @param {type:"boolean"}








from IPython.display import clear_output
from IPython.display import Audio
if not os.path.exists(f"{edge_folder}/audio"):
    os.mkdir(f"{edge_folder}/audio")
import uuid
def random_audio_name_generate():
  random_uuid = uuid.uuid4()
  audio_extension = ".mp3"
  random_audio_name = str(random_uuid)[:8] + audio_extension
  return random_audio_name
def edge_tts_pipeline(input_text,Language,Gender,translate_text_flag=True,no_silence=False,speed=1,tts_save_path="",long_sentence=True):
  # print("calling gradio_talk")
  # global long_sentence,translate_text_flag,Language,speed,voice_name,Gender
  global male_voice_list,female_voice_list
  
  # long_sentence=True
  # translate_text_flag=True
  # speed=1
  if long_sentence==False:
    if len(input_text)>500:
      long_sentence=True
  voice_name=''
  if Gender=="Male":
    voice_name=male_voice_list[Language]
  if Gender=="Female":
    voice_name=female_voice_list[Language]
  if long_sentence==True and translate_text_flag==True:
    chunks_list=make_chunks(input_text,Language)
  elif long_sentence==True and translate_text_flag==False:
    chunks_list=make_chunks(input_text,"English")
  else:
    chunks_list=[input_text]
  temp_save_path=f"{edge_folder}/audio/"+random_audio_name_generate()
  save_path=temp_save_path.lower().replace(".mp3",".wav")
  # print(chunks_list,speed,voice_name,save_path,translate_text_flag,Language)
  edge_save_path=edge_free_tts(chunks_list,speed,voice_name,temp_save_path,translate_text_flag,Language)
  mp3_to_wav(edge_save_path, save_path)
  audio_return_path=save_path
  if no_silence:
    clean_path=f"{edge_folder}/audio/"+random_audio_name_generate().replace(".mp3",".wav")
    remove_silence(save_path,clean_path)
    audio_return_path=save_path
    # return clean_path
  if tts_save_path=="":
    return audio_return_path
  else:
    shutil.copyfile(audio_return_path,tts_save_path)
    return audio_return_path



def talk(input_text):
  # global long_sentence,translate_text_flag,Language,speed,voice_name,Gender
  global Language, Gender,male_voice_list,female_voice_list
  global no_silence
  long_sentence=True
  translate_text_flag=False
  speed=1

  if Gender=="Male":
    voice_name=male_voice_list[Language]
  if Gender=="Female":
    voice_name=female_voice_list[Language]
  if long_sentence==True and translate_text_flag==True:
    chunks_list=make_chunks(input_text,Language)
  elif long_sentence==True and translate_text_flag==False:
    chunks_list=make_chunks(input_text,"English")
  else:
    chunks_list=[input_text]
  
  temp_save_path=f"{edge_folder}/audio/"+random_audio_name_generate()
  # print(f"temp_save_path: {temp_save_path}")
  save_path=temp_save_path.replace(".mp3",".wav")
  # print(f"save_path: {save_path}")
  edge_save_path=edge_free_tts(chunks_list,speed,voice_name,temp_save_path,translate_text_flag,Language)
  
  mp3_to_wav(edge_save_path, save_path)
  if no_silence:
    # clean_path=f"{edge_folder}/audio/"+random_audio_name_generate().replace(".mp3",".wav")
    temp_path=save_path.replace(".wav","__.wav")
    shutil.copyfile(save_path,temp_path)
    remove_silence(temp_path,save_path)
    return save_path
  return save_path

from pydub import AudioSegment
from pydub.silence import split_on_silence
import os
 
def remove_silence(file_path,output_path):
    # Extract file name and format from the provided path
    file_name = os.path.basename(file_path)
    audio_format = "wav"

    # Reading and splitting the audio file into chunks
    sound = AudioSegment.from_file(file_path, format=audio_format)
    audio_chunks = split_on_silence(sound,
                                    min_silence_len=100,
                                    silence_thresh=-45,
                                    keep_silence=50)

    # Putting the file back together
    combined = AudioSegment.empty()
    for chunk in audio_chunks:
        combined += chunk


    combined.export(output_path, format=audio_format)

    return output_path


from pydub import AudioSegment

def mp3_to_wav(mp3_file, wav_file):
    # Load the MP3 file
    # print("calling mp3_to_wav")
    # print(mp3_file,wav_file)
    audio = AudioSegment.from_mp3(mp3_file)

    # Export the audio to WAV format
    audio.export(wav_file, format="wav")

# edge_save_path=talk(text)
# print(f"Audio File Save at: {edge_save_path}")

# text = "a quick brown fox jumps over the lazy dog and the dog barks loudly"
# Language = "English" # @param ['English','Hindi','Bengali','Afrikaans', 'Amharic', 'Arabic', 'Azerbaijani', 'Bulgarian', 'Bosnian', 'Catalan', 'Czech', 'Welsh', 'Danish', 'German', 'Greek', 'Spanish', 'French', 'Irish', 'Galician', 'Gujarati', 'Hebrew', 'Croatian', 'Hungarian', 'Indonesian', 'Icelandic', 'Italian', 'Japanese', 'Javanese', 'Georgian', 'Kazakh', 'Khmer', 'Kannada', 'Korean', 'Lao', 'Lithuanian', 'Latvian', 'Macedonian', 'Malayalam', 'Mongolian', 'Marathi', 'Malay', 'Maltese', 'Burmese', 'Norwegian Bokmål', 'Nepali', 'Dutch', 'Polish', 'Pashto', 'Portuguese', 'Romanian', 'Russian', 'Sinhala', 'Slovak', 'Slovenian', 'Somali', 'Albanian', 'Serbian', 'Sundanese', 'Swedish', 'Swahili', 'Tamil', 'Telugu', 'Thai', 'Turkish', 'Ukrainian', 'Urdu', 'Uzbek', 'Vietnamese', 'Chinese', 'Zulu']
# no_silence = False
# Gender = "Male"# @param ['Male', 'Female']
# translate_text_flag=True
# no_silence=True
# speed=1
# tts_save_path='temp.wav'
# edge_save_path=edge_tts_pipeline(text,Language,Gender,translate_text_flag=translate_text_flag,no_silence=no_silence,speed=speed,tts_save_path=tts_save_path)
# print(f"Audio File Save at: {edge_save_path}")

# from microsoft_tts import edge_tts_pipeline
# def tts(text,tts_save_path=''):
#     # text = "a quick brown fox jumps over the lazy dog and the dog barks loudly"
#     Language = "English" # @param ['English','Hindi','Bengali','Afrikaans', 'Amharic', 'Arabic', 'Azerbaijani', 'Bulgarian', 'Bosnian', 'Catalan', 'Czech', 'Welsh', 'Danish', 'German', 'Greek', 'Spanish', 'French', 'Irish', 'Galician', 'Gujarati', 'Hebrew', 'Croatian', 'Hungarian', 'Indonesian', 'Icelandic', 'Italian', 'Japanese', 'Javanese', 'Georgian', 'Kazakh', 'Khmer', 'Kannada', 'Korean', 'Lao', 'Lithuanian', 'Latvian', 'Macedonian', 'Malayalam', 'Mongolian', 'Marathi', 'Malay', 'Maltese', 'Burmese', 'Norwegian Bokmål', 'Nepali', 'Dutch', 'Polish', 'Pashto', 'Portuguese', 'Romanian', 'Russian', 'Sinhala', 'Slovak', 'Slovenian', 'Somali', 'Albanian', 'Serbian', 'Sundanese', 'Swedish', 'Swahili', 'Tamil', 'Telugu', 'Thai', 'Turkish', 'Ukrainian', 'Urdu', 'Uzbek', 'Vietnamese', 'Chinese', 'Zulu']
#     no_silence = False
#     Gender = "Male"# @param ['Male', 'Female']
#     translate_text_flag=True
#     no_silence=True
#     speed=1
#     # tts_save_path='temp.wav'
#     long_sentence=True
#     edge_save_path=edge_tts_pipeline(text,Language,Gender,translate_text_flag=translate_text_flag,no_silence=no_silence,speed=speed,tts_save_path=tts_save_path,long_sentence=long_sentence)
#     print(f"Audio File Save at: {edge_save_path}")
#     return edge_save_path

## for srt use how to call

# from microsoft_tts import edge_tts_pipeline
# import shutil
# import os

# def tts(text, Language='English', local_save_path=''):
#     Gender = "Female"
#     translate_text_flag = True
#     no_silence = False
#     speed = 1
#     long_sentence = False 
#     tts_save_path = ''                         
#     edge_save_path = edge_tts_pipeline(text, Language, Gender, translate_text_flag=translate_text_flag, 
#                                        no_silence=no_silence, speed=speed, tts_save_path=tts_save_path, 
#                                        long_sentence=long_sentence)

#     srt_file_path = edge_save_path.replace('.wav', '.srt')

#     # Check if the SRT file exists
#     if os.path.exists(srt_file_path):
#         if local_save_path:
#             temp_srt_file_path = local_save_path.replace('.wav', '.srt')
#             shutil.copyfile(edge_save_path, local_save_path)
#             shutil.copyfile(srt_file_path, temp_srt_file_path)   
#             return local_save_path, temp_srt_file_path
#         else:
#             return edge_save_path, srt_file_path
#     else:
#         # Handle only the WAV file if SRT is not available
#         if local_save_path:
#             shutil.copyfile(edge_save_path, local_save_path)
#             return local_save_path, ''
#         else:
#             return edge_save_path, ''

# # Test the function
# text="Hello, how are you?"
# Language = 'English'
# local_save_path = 'edge_tts.wav'
# tts_path, srt_path = tts(text, Language, local_save_path)
# print(tts_path, srt_path)


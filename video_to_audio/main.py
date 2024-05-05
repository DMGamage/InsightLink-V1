# import subprocess
#
# def convert_video_to_audio(input_file,output_file):
#     ffmpeg_cmd = ['ffmpeg', '-i', input_file, '-acodec',"libmp3lame", "-ab", "192k", "-ar","44100","-y",output_file]
#
#     try:
#         subprocess.run(ffmpeg_cmd,check=True)
#         print("Success")
#     except subprocess.CalledProcessError as e:
#         print("Conversion")
#
# convert_video_to_audio("test.mp4","test.mp3")

import subprocess
import os

def convert_video_to_audio(input_file, output_file):
    ffmpeg_cmd = ['ffmpeg', '-i', input_file, '-acodec', 'libmp3lame', '-ab', '192k', '-ar', '44100', '-y', output_file]

    try:
        subprocess.run(ffmpeg_cmd, check=True)
        print("Audio conversion successful")
    except subprocess.CalledProcessError as e:
        print("Audio conversion failed")

def split_audio(input_file, output_folder, duration=30):
    os.makedirs(output_folder, exist_ok=True)  # Create output folder if it doesn't exist

    ffmpeg_cmd = ['ffmpeg', '-i', input_file, '-f', 'segment', '-segment_time', str(duration), '-c', 'copy',
                  f'{output_folder}/part_%03d.mp3']

    try:
        subprocess.run(ffmpeg_cmd, check=True)
        print("Audio splitting successful")
    except subprocess.CalledProcessError as e:
        print("Audio splitting failed")

if __name__ == "__main__":
    input_file = "test.mp4"
    temp_audio_file = "temp_audio.mp3"
    output_folder = "audio_parts"

    # Convert video to audio
    convert_video_to_audio(input_file, temp_audio_file)

    # Split audio into 30-second parts
    split_audio(temp_audio_file, output_folder)


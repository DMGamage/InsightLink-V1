import subprocess

def convert_video_to_audio(input_file,output_file):
    ffmpeg_cmd = ['ffmpeg', '-i', input_file, '-acodec',"libmp3lame", "-ab", "192k", "-ar","44100","-y",output_file]

    try:
        subprocess.run(ffmpeg_cmd,check=True)
        print("Success")
    except subprocess.CalledProcessError as e:
        print("Conversion")

convert_video_to_audio("test.mp4","test.mp3")

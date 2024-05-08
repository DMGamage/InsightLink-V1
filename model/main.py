from transformers import pipeline
import os
import soundfile as sf
import numpy as np
import librosa

# Initialize ASR pipeline
asr = pipeline(task="automatic-speech-recognition",
               model="distil-whisper/distil-small.en")


def count_and_read_audio_parts(output_folder):
    # List all files in the output folder
    audio_files = os.listdir(output_folder)

    # Count the number of audio files
    num_files = len(audio_files)
    print(f"Total number of audio files: {num_files}")

    audio_files.sort()
    full_text =""

    for file_name in audio_files:
        file_path = os.path.join(output_folder, file_name)

        try:
            # Read audio file
            audio, sampling_rate = sf.read(file_path)

            # Process the audio data as needed
            audio_transposed = np.transpose(audio)


            audio_mono = librosa.to_mono(audio_transposed)

            audio_16KHz = librosa.resample(audio_mono,
                                           orig_sr=sampling_rate,
                                           target_sr=16000)

            # Transcribe audio using ASR pipeline
            result = asr(
                audio_16KHz,
                chunk_length_s=30,  # 30 seconds
                batch_size=21,
                return_timestamps=True,
            )["chunks"]

            # Extracting text from the first element of the list
            # transcribed_text = result[0]['text']  # Access transcribed text using the correct key 'text'
            # full_text =transcribed_text + " "

            for chunk in result:
                transcribed_text = chunk['text']
                full_text += transcribed_text + " "

             # Print transcribed text
        except Exception as e:
            print(f"Error processing audio file {file_name}: {e}")

    print(full_text)

if __name__ == "__main__":
    # Count and read audio parts
    count_and_read_audio_parts("../video_to_audio/audio_parts")

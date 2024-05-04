import wave

obj = wave.open('hawking01.wav',"rb")

print("Number of channels",obj.getnchannels())
print("Sample Width",obj.getsampwidth())
print("Frame rate",obj.getframerate())
print("Number of frames",obj.getnframes())
print("Parameteres",obj.getparams())

t_audio = obj.getnframes() / obj.getframerate()
print("Audio Time",t_audio)

frames = obj.readframes(-1)
print(type(frames),type(frames[0]))
print(len(frames)/2)

obj.close()
obj_new = wave.open("hawking_new","wb")
obj_new.setnchannels(1)
obj_new.setsampwidth(2)
obj_new.setframerate(16000)

obj_new.writeframes(frames)

obj_new.close()
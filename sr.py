import speech_recognition as sr 


recognizer = sr.Recognizer()

harvard = sr.AudioFile('harvard.wav')
jackhammer = sr.AudioFile("jackhammer.wav")

#with harvard as source:
	#audio = recognizer.record(source)
with jackhammer as source:
	recognizer.adjust_for_ambient_noise(source, duration = 0.5)
	audio = recognizer.record(source, duration = 5)

print(recognizer.recognize_google(audio))
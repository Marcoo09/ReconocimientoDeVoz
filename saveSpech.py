import speech_recognition as sr 
import sys
from scheduler import Scheduler

#Variables
recognizer = sr.Recognizer()
microphone = sr.Microphone(device_index = 0)
scheduler = Scheduler()
text = ''

fileName = 'speech.txt'

file = open(fileName,'w+')


def speechToText():
	print('Grabando')
	with microphone as source:
		#recognize.adjust_for_ambient_noise(source) 
		audio = recognizer.listen(source)
	try:	
		text = recognizer.recognize_google(audio)
		file.write(text + '\n')
	except:
		text = 'Debe hablar claro'
	print(text)
	print('Fin grabación')
	return text


if __name__ = '__main__':
	scheduler.add(1,0,speechToText())
	while text != 'see':
		text = scheduler.run()

	file.close()

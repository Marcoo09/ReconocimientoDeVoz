import speech_recognition as sr 

#Variables
recognizer = sr.Recognizer()
microphone = sr.Microphone(device_index = 0)

#To sar what microphone use
#print(sr.Microphone.list_microphone_names())
'''
print('Grabando')
with microphone as source:
	#recognize.adjust_for_ambient_noise(source) 
	audio = recognizer.listen(source)

print(recognizer.recognize_google(audio))
print('Fin grabación')
'''
text = ''

while text != 'salir':
	print('Grabando')
	with microphone as source:
		#recognize.adjust_for_ambient_noise(source) 
		audio = recognizer.listen(source)
	try:	
		text = recognizer.recognize_google(audio) 
	except:
		text = 'Debe hablar claro'
	print(text)
	print('Fin grabación')


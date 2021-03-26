import pyttsx3
import beepy
def speak_aloud(text):
	engine = pyttsx3.init()
	voices = engine.getProperty('voices')
	for voice in voices:
		if voice.languages[0] == u'en_US':
		   engine.setProperty('voice', voice.id)
	engine.say(text)
	print(text)
	engine.runAndWait()
def beep(num_of_beeps = 1):
	for x in range(num_of_beeps):
		beepy.beep(sound=1)
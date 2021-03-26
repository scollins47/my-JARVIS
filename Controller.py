import threading
import concurrent.futures
import time
import os
import sys
import TestTouch
import beepy
import ears 
from gpiozero import MotionSensor
from extract_embeddings import extract_embeddings
from train_model import train
import voice_commands as vc
import importlib.util
from recognize_video import vid_detect
from get_face_data import face_data
from num2words import num2words
from subprocess import call
import mouth

def get_auth_from_face():
	name, confidence = vid_detect(.8, 5)#confidence, seconds recorded
	return name
def auth_process():
	name = get_auth_from_face()#grab name if we can
	if name == "n/a":#no face in frame
		return "n/a"
	elif name =="unknown":#unknown face in frame
		to_speak = "want to make a profile?"
		mouth.speak_aloud(to_speak)
		if ears.listen_for_trigger(["yes", "yeah", "okay",'sure'], time = 3):
			to_speak = "What would you like me too call you?"
			mouth.speak_aloud(to_speak)
			new_name = ears.listen_and_translate(time = 5)
			mouth.speak_aloud("Look into the Camera")
			face_data(new_name, 1)
			extract_embeddings()
			train()
			name = new_name
	else:
		to_speak = "Hello " +name+ ", awaiting commands"
		mouth.speak_aloud(to_speak)
		mouth.speak_aloud(vc.decode_and_run(ears.listen_and_translate(5)))
def main_thread():
	#pir = MotionSensor(16)
	name = ""
	memory = []
	while True:
		if name != "n/a" or name != "":
			print(name)
# 		if  pir.motion_detected:
# 			print('motion detected')
# 			name = auth_process()
		if ears.listen_for_trigger("sixteen", 3):
			print("trigger heard")
			mouth.speak_aloud("Listening")
			command = ears.listen_and_translate(6)
			print(command)
			memory.append(command)
			if "recognize" in command.split(' '):
				name = auth_process()
			else:
				cmd = str(vc.decode_and_run(command))
				mouth.speak_aloud(cmd)
		
#POST AUTHENTICATION
main_thread()
	#spot.pause(name)
quit()
#face.face_data('sammy', 0) to get new user data <----
# spec2 = importlib.util.spec_from_file_location("extract_embeddings","opencvface/extract_embeddings.py")
# emb = importlib.util.module_from_spec(spec2)
# spec2.loader.exec_module(emb)
# emb
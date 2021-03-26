#!/usr/bin/env python3

from vosk import Model, KaldiRecognizer, SetLogLevel
import sys
import os
import subprocess
import wave
import time
import json
  #pre: the file name to translate
  #post: the words from that file
def translate_file(filename="last5.wav"):
    SetLogLevel(-1)

    if not os.path.exists("model"):
        print ("Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
        exit (1)
    filepath = "./" +filename
    wf = wave.open(filepath, "rb")
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
        print ("Audio file must be WAV format mono PCM.")
        exit (1)

    model = Model("./model")
    rec = KaldiRecognizer(model, 16000)
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            res = rec.FinalResult()
            #print(rec.FinalResult())
        #else:
            #print(rec.PartialResult())
    try:#for some reason res doesnt get assigned post loop
        results = res
        #print("results: " +results)
    except UnboundLocalError:
        results = rec.FinalResult() #rec.FinalResult() holds the words in this case
    results_json = json.loads(results)
    #print(results_json["text"])
    return (results_json["text"]) #["results"] for confidence of each word
def listen_(filename, howlong = 7):
    ret = subprocess.call("arecord -d "+str(howlong) + " -D plughw:2,0 --channels=1 -r 16000 -f S16_LE ./"+filename, shell=True)
  #pre: triggers to check for and how long to record default 5 seconds
  #post: True or False whether one of the triggers was heard 
def listen_for_trigger(trigger, time = 5):
	listen_('last5.wav',time)
	words = translate_file().split(' ')
	print("WORDS: " + str(words))
	for word in words:
		if(trigger == word):
			return True
	return False
def listen_for_wordy_trigger(trigger, time = 3):
	listen_('last5.wav', time) #comment/uncomment for testing
	words = translate_file()
	print(words)
	words_array = words.split(' ')
	length_of_trigger = len(trigger.split(' '))
	if len(words_array) < length_of_trigger:
		return False
	if(len(words_array) == length_of_trigger):
		return words == trigger
	for i in range(0, len(words_array) - length_of_trigger):
		to_check = ''
		for j in range(i, length_of_trigger + i):
			to_check += words_array[j] + ' '
		if to_check == trigger:
			print("Trigger heard")
			return True
	return False
  #pre: how long you want to record for
  #post: String: the words in the recording 
def listen_and_translate(time = 3, filename = "last5.wav"):
	listen_(filename, time)
	response = translate_file()
	return response
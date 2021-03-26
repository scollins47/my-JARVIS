#!/usr/bin/env python3

from vosk import Model, KaldiRecognizer, SetLogLevel
import sys
import os
import subprocess
import wave
import json

def translate_file(filename="last5.wav"):
    SetLogLevel(0)

    if not os.path.exists("model"):
        print ("Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder.")
        exit (1)
    filepath = "./" +filename
    wf = wave.open(filepath, "rb")
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
        print ("Audio file must be WAV format mono PCM.")
        exit (1)

    model = Model("./model")
    rec = KaldiRecognizer(model, wf.getframerate())

    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            print(rec.Result())
        else:
            print(rec.PartialResult())
    results = rec.FinalResult()
    return json.loads(results)["text"] #["results"] for confidence of each word
def listen_(howlong = 7):
    ret = subprocess.call("arecord -d "+str(howlong) + " -D plughw:2,0 --channels=1 -r 48000 -f S16_LE ./last5.wav", shell=True)

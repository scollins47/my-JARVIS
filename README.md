# my-JARVIS (trigger is atlas for now, easily modifiable)
personal AI developed by me for raspberry pi 4 (NOOBS os), with tensor flow for facial recognition and VOSK for audio recognition.
# About This Project
Since my senior year of highschool and subsequent failed attempt at making computer vision, I had always been into working with AI. Making an AI like JARVIS in iron man had always been a goal of mine. I began working on this project around August 2020 (summer break), not only has it been a really good learning experience for Python, and tensor flow,
but working with an ARM architecture has been another huge learning experience as I just started learning about the effects of different architectures and how they store data in my 
computer systems class. I never have much time to work on it with college and all, so pardon the messy/rushed code, but I try to work on it at least once or twice a week to keep the ideas flowing.
My plan for this project is to eventually to have a jarvis from iron man type ai.

## Goals
### General
  - comment everything lol
  - News bot (https://newsapi.org/pricing)
  - ToDo - list
  - clean up code (i know you're supposed to never write un-clean code -_-)
  - add stock predictor api, should be easy, just have to configure it on the raspi
  - add at least 2 new voice commands a week. 
  - add chat bot 
  - Figure out how big of a model the pi can take with GPT-NEO / integrate GPT-NEO from mac -> pi
  - create GUI/visual interface that makes it a bit more non-compsci people friendly 
  - create a memory system so that the pi knows who it has talked to (MongoDB on the webserver part, or PI DB)
  
### Thread/Make concurrent:
  - motion sensor activate and trigger the authentication when motion is present
  - The listening for the trigger/voice commands
  
### Spotipy api 
  - actually get queueing and searching to work properly
  - have the queueing and searching be updated with website so that anyone connected to the website can queue songs
  
### Video Recognition
  - have a database of the last person seen (using pi mongoDB) 
  - update that database so that the pi knows who is in the room <br/> this can be done by tracking two points on the screen and seeing the direction that
  a person is walking, ie. a psuedo memory of who has entered/left the room
  
### Speech Recognition
  - update so that it actually listens in real-time and not in psuedo real time ie. every 3 seconds it records and then quickly checks for trigger word
  - implement chat bot, with memory, should be easy (throw back to oberle's class using a tree to keep track of questions/responses)

## IDEAS:
  - laser maze, reqs. 1 laser diode, a laser reciever, and a lot of tiny mirrors angled correctly. 20$

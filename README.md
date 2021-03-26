# my-JARVIS (trigger is sixteen for now, easily modifiable)
personal AI developed by me for raspberry pi 4 (NOOBS os), with tensor flow for some snazzy add ons :), DONT USE THIS TO TAKE OVER THE WORLD!!
also dont use any of the pictures for any illegal or malicious reasons.

# About This Project
This was mainly a pet project that I have always wanted to do, I think having an AI that doesn't listen and send all the data it collects to google or amazon
would be really cool and fun to have. I began working on this project around August 2020 (summer break), not only has it been a really good learning experience for Python, and tensor flow,
but working with an ARM architecture has been another huge learning experience as I just started learning about the effects of different architectures and how they store data in my 
computer systems class. I never have much time to work on it with college and all, so pardon the messy/rushed code, but I try to work on it at least once or twice a week to keep the ideas flowing.
My plan for this project is to eventually to have a jarvis from iron man type ai.

## Goals
### General
  - comment everything lol
  - clean up code (i know you're supposed to never write un-clean code -_-)
  - add stock predictor api, should be easy, just have to configure it on the raspi
  - add at least 2 new voice commands a week. 
  - add chat bot 
  - create GUI/visual interface that makes it a bit more non-compsci people friendly 
  - create a memory system so that the pi knows who it has talked to
  
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

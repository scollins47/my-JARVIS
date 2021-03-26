import spotipy_playback as spot
from picamera import PiCamera
import stock_methods as stocks
import ears
import time
from word2number import w2n
import mouth
import weather
from gpiozero import MotionSensor
import os
from recognize_video import vid_detect
from datetime import date
from datetime import datetime

def get_index_of_word(word, response):
	count = 0
	for x in response:
		if(x == word): return count
		count += 1
	return count

def is_word_in_response(word, response):
	for x in response:
		if word == x : return True

def get_time_interval(words):
	words_array = words.split(' ')
	seconds = -1
	minutes = -1
	hours = -1
	count = 0
	for word in words_array:
		print(word)
		if(word == 'second' or word =='seconds'):
			print('found')
			seconds = count
		if word == 'minute' or word == 'minutes':
			print('found')
			minutes = count
		if word == 'hours' or word == 'hour':
			print('found')
			hours = count
		count = count + 1
	time_vars = [-1, -1, -1]#[sec, min, hour]
	if(seconds > 0):
		time_vars[0] = w2n.word_to_num(words_array[seconds-1])
	if(minutes > 0):
		time_vars[1] = w2n.word_to_num(words_array[minutes-1])
	if(hours > 0):
		time_vars[2] = w2n.word_to_num(words_array[hours - 1])
	print(time_vars)
	try:
		if(seconds > 0):
			extra = w2n.word_to_num(words_array[seconds-2])
			time_vars[0] += extra
	except(ValueError, IndexError):
		print('no second term for seconds')
	try:
		if(minutes > 0):
			extra = w2n.word_to_num(words_array[minutes - 2])
			time_vars[1] += extra
	except(ValueError, IndexError):
		print('no second term for minutes')
	try:
		if(hours > 0):
			extra = w2n.word_to_num(words_array[hours - 2])
			time_vars[2] += extra
	except(ValueError, IndexError):
		print('no second term for hours')
	print(time_vars)
	return time_vars
def monitor(words):
	times = get_time_interval(words)
	total_seconds = 0
	if(times[0] > 0):
		total_seconds += times[0]
	if(times[1] > 0):
		total_seconds += times[1] * 60
	if(times[2] > 0):
		total_seconds += times[2] * 60 * 60
	print(str(total_seconds))
	if(total_seconds == 0): total_seconds = 10
	pir = MotionSensor(16)
	def helper():
		os.system('raspivid -o ./monitor_capture/temp'+str(datetime.now().strftime("%H:%M:%S"))+'.h264 -t 10000')
		return 0
	pir.when_motion = helper
	count = 0
	mouth.speak_aloud("Monitor Mode Active")
	timeout = time.time() + total_seconds
	while time.time() < timeout:
		pir.wait_for_motion(total_seconds)
		count += 1
	return "Leaving Monitor Mode"

def timer(words):
	sleep_time = 0
	vals = get_time_interval(words)
	print(vals)
	mouth.speak_aloud("Starting timer")
	seconds = vals[0]
	minutes = vals[1]
	hours = vals[2]
	if(seconds > 0):
		sleep_time += seconds
	if(minutes > 0):
		sleep_time += (minutes * 60)
	if(hours > 0):
		sleep_time += (hours * 60 * 60)
	print("Sleep Time: " + str(vals[2]) + " hours | "+str(vals[1])+" minutes | "+str(vals[0]))
	time.sleep(sleep_time)
	mouth.beep()
	return "Timer Up"

def run_auth_command(name, command):
	if(name != 'n/a' and name != 'unknown'):
		print('something')

def decode(response):
	print('WORDS: ' + str(response))
	return response.split(" ")

def decode_and_run(response):
	words = decode(response)
	try:#if its a spotipy command gotta make sure speakers are on
		if("skip" in response and "dont" not in response):
			spot.skip('sammy')
			return "ok"
		if(("previous" in response or "go back" in response) and "dont" not in response):
			spot.previous('sammy')
			return "ok"
		if("pause" in response and "dont" not in response):
			spot.pause('sammy')
			return "ok"
		if("set volume" in response and "dont" not in response):
			for word in words:
				if word.isnumeric():
					spot.volume('sammy', int(word))
					return "ok"
					break
			return "Number required"
	except:#Some speaker error i think
		return "Not playing music"
	if "timer" in response:
		return timer(response.split(' '))
	if "whether" in response or "weather" in response:
		temp, desc = weather.parse_weather()
		return "temperature is: "+temp+" degrees.\n weather pattern: " +desc
	if "ticker data" in response:
		temp = -1
		ticker = ''
		for x in range(0,len(response.split(' '))):
			if words[x] == "for":
				temp = x + 1
		for j in range(temp, len(words)):
			ticker += words[j]
		try:
			stock = stocks.get_stock_by_ticker(ticker)
		except(ValueError):
			return "No valid tickers in response"
		return str(stock['symbol']) + ': '+ str(stock['regularMarketPrice'])
	if("stock data" in response):
		name = ''
		for word in response.split(' '):
			if(word == "my"):
				name, confidence = vid_detect(60, 5)
		if(name == '' or name == 'n/a'):
			print(stocks.get_relevant_info())
		elif(name == 'unknown'):
			return "You do not have a profile, set one up to access personal stock data"
		else:
			print(stocks.get_relevant_info(user = name))
		return 'too long didnt read'
	if("stop functions" in response or "shut down" in response):
		name, confidence = vid_detect(.6, 5)
		if(name == "sammy"):
			return "quit"
		else:
			return "NOT AUTHOURIZED!"
	if("take a picture" in response or "take a photo" in response):
		camera = PiCamera()
		today = date.today()
		camera.start_preview()
		mouth.speak_aloud("say cheese")
		time.sleep(2)
		camera.capture('./pictures/'+ today.strftime("%b-%d-%Y")+'.jpg')
		camera.stop_preview()
		camera.close()
		return "picture taken"
	if("monitor mode" in response):
		return monitor(response)
	if("time is it" in response):
		now = datetime.now()
		rn = now.strftime("%H:%M")
		return ("It is, ", rn)
	if("what are you" in response):
		return "I am Sixteen, a A.I. created by sammy"
	if("q song" in response or "queue song" in response):#WIP
		by_index = -1
		start = -1
		for x in range(len(words)):
			if words[x] == "q":
				if((words[x+1] == "the" or words[x+1] == "this") and words[x+2] == "song"):
					start = x + 2 + 1
				else:
					start = x+1
			if words[x] == "by":
				by_index = x
		count = 0
		song = ""
		artist = ""
		for x in range(start, len(words)):
			if x < by_index:
				song += words[x] + ' '
			if x > by_index:
				artist += words[x] + ' '
		print("SONG: " + song)
		print("ARTIST: " +artist)
		print(spot.search_artist_track('sammy', artist, song))
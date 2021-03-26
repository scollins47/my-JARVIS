import requests
import json
def get_jmu_weather():
	api_key = "79910167d4f852fe9c8e9f5aa077b81f"
	polygon_id = "60067df52b4d08461e9cc094"
	r = requests.get('http://api.agromonitoring.com/agro/1.0/weather?polyid='+polygon_id+'&appid='+api_key)
	return r.json()
def parse_weather():
	weather_json = get_jmu_weather()
	temp = str((float(weather_json['main'].get('temp')) - 273.15) * (9/5) + 32)[:5]
	desc = weather_json['weather'][0].get('description')
	return (temp,desc)
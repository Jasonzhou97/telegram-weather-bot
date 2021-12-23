import requests
from weather_index import rain_id,uvi_index
import datetime
API_key = "5348b4e5f4ea388575a31d19bb0a70ed"

parameters = {"lat":1.352083,
      "lon":103.819839,
      "appid":API_key,
    "exclude":"current,minutely"}


def daily_rain():
    response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
    data = response.json()
    current_day = data["daily"][0]
    daily_rain_status = current_day["weather"][0]["id"]
    return rain_id[daily_rain_status]

def hourly_rain():
    response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
    data = response.json()
    current_hour = data["hourly"][0]
    hourly_rain_status = current_hour["weather"][0]["id"]
    return rain_id[hourly_rain_status]

def hourly_uvi():
    response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
    data = response.json()
    current_hour = data["hourly"][0]
    hourly_uvi_status = int(current_hour["uvi"])
    return uvi_index[hourly_uvi_status]

def daily_uvi():
    response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
    data = response.json()
    current_hour = data["daily"][0]
    daily_uvi_status = int(current_hour["uvi"])
    return uvi_index[daily_uvi_status]

def sunrise_time():
    response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
    data = response.json()
    current_day, next_day = data["daily"][0], data["daily"][1]
    current_day_sunrise_time,next_day_sunrise_time = current_day["sunrise"],next_day["sunrise"]
    current_day_sunrise_time,next_day_sunrise_time = int(current_day_sunrise_time),int(next_day_sunrise_time)
    current_day_sunrise_time,next_day_sunrise_time = datetime.datetime.fromtimestamp(int(current_day_sunrise_time)).strftime('%Y-%m-%d %H:%M:%S'),datetime.datetime.fromtimestamp(int(next_day_sunrise_time)).strftime('%Y-%m-%d %H:%M:%S')
    return [current_day_sunrise_time[11:16],next_day_sunrise_time[11:16]]

def sunset_time():
    response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
    data = response.json()
    current_day, next_day = data["daily"][0], data["daily"][1]
    current_day_sunrise_time,next_day_sunrise_time = current_day["sunset"],next_day["sunset"]
    current_day_sunrise_time,next_day_sunrise_time = int(current_day_sunrise_time),int(next_day_sunrise_time)
    current_day_sunrise_time,next_day_sunrise_time = datetime.datetime.fromtimestamp(int(current_day_sunrise_time)).strftime('%Y-%m-%d %H:%M:%S'),datetime.datetime.fromtimestamp(int(next_day_sunrise_time)).strftime('%Y-%m-%d %H:%M:%S')
    return [current_day_sunrise_time[11:16],next_day_sunrise_time[11:16]]

def psi_reading():
    response = requests.get(url="https://api.data.gov.sg/v1/environment/psi")
    data = response.json()
    pollution_data = data["items"]
    psi_reading = pollution_data[0]["readings"]["psi_twenty_four_hourly"]["national"]
    return psi_reading
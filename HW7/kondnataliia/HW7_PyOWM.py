from pyowm import OWM

owm = OWM('ef2206ff5da67de63306d0b143e20872')
mgr = owm.weather_manager()

city = input("Enter the city you live in: ")
observation = mgr.weather_at_place(city)
w = observation.weather

status_clouds = w.detailed_status
wind_speed = w.wind()['speed']
wind_deg = w.wind()['deg']
humidity = w.humidity
temperature = w.temperature('celsius')['temp']
max_temperature = w.temperature('celsius')['temp_max']
min_temperature = w.temperature('celsius')['temp_min']
rain = w.rain
heat_index = w.heat_index
clouds = w.clouds

print(f"The detailed_status in {city} is {status_clouds}.")
print(f"In {city}, the wind speed is {wind_speed}.")
print(f"In {city}, the wind degree is {wind_deg}.")
print(f"In {city}, the temperature is {temperature} degrees Celsius.")
print(f"In {city}, the maximal temperature is {max_temperature} degrees Celsius.")
print(f"In {city}, the minimal temperature is {min_temperature} degrees Celsius.")
print(f"In {city}, the rain expectancy is {rain}.")
print(f"In {city}, the heat_index is {heat_index}.")
print(f"In {city}, the clouds rate is {clouds}.")

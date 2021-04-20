import pyowm

# ---------- FREE API KEY examples ---------------------

owm = pyowm.OWM('a5605de9995c5cbda72c9dec4b4ea37a')
mgr = owm.weather_manager()

city = input("Please, input the city you are interested in: ")

observation = mgr.weather_at_place(city)
w = observation.weather

status_clouds = w.detailed_status                              # 'clouds'
speed_wind = w.wind()['speed']                                 # {'speed': 4.6, 'deg': 330}
humidity_level = w.humidity                                    # 87
temperature_max = w.temperature('celsius')['temp_max']         # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
temperature= w.temperature('celsius')['temp']
temperature_min = w.temperature('celsius')['temp_min']
rain = w.rain                          # {}
heat_index = w.heat_index              # None
clouds = w.clouds                      # 75

print (f"In city {city} will be {status_clouds}")
print (f"In city {city} the spped of wind will be {speed_wind} km/hour")
print (f"In city {city} the humidity level will be {humidity_level}")
print (f"In city {city} maximum temperature will be {temperature_max}")
print (f"In city {city} minimum temperature will be {temperature_min}")
print (f"In city {city} averaige temperature will be {temperature}")
print (f"In city {city} expeted {rain} ")
print (f"In city {city} heat index will be {heat_index}")
print (f"In city {city} expected level of clouds is {clouds}")

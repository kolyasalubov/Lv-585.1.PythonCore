from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

# ---------- FREE API KEY examples ---------------------

owm = OWM('ef2206ff5da67de63306d0b143e20872')
mgr = owm.weather_manager()
input_city=input("What city you are interested:")


# Search for current weather in London (Great Britain) and get details
observation = mgr.weather_at_place(input_city)
w = observation.weather

w.detailed_status         # 'clouds'
w.wind()                  # {'speed': 4.6, 'deg': 330}
w.humidity                # 87
w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
w.rain                    # {}
w.heat_index              # None
w.clouds                  # 75
status_clouds = w.detailed_status()
speed_wind = w.wind()["speed"]
humidity = w.humidity
temperature = w.temperature('celsius')["temp"]
temperature_max = w.temperature('celsius')["temp_max"]
temperature_min = w.temperature('celsius')["temp_min"]
print(f"In {input_city} the wind speed is {speed_wind}")
print(f"In {input_city} the humidity is {humidity}")
print(f"In {input_city} the temperature is {temperature}")
print(f"In {input_city} the max. temp. is{temperature_max}")
print(f"In {input_city} the min. temp. is{temperature_min}")

# Will it be clear tomorrow at this time in Milan (Italy) ?
forecast = mgr.forecast_at_place('Milan,IT', 'daily')
answer = forecast.will_be_clear_at(timestamps.tomorrow())
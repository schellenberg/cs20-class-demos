from weather import Weather
weather = Weather(temperature_unit="Celsius") # Celsius (or) Kelvin (or) Fahrenheit
current_weather = weather.fetch_weather(city='Saskatoon', only_temp=False) # if only_temp is set To True It Will Only return The current temperature in given unit

temp = current_weather['Temperature: ']
raw_temp = int(temp[0:-2])

if raw_temp < -15:
    result = "bloody cold"
elif raw_temp > 20:
    result = "hot"
else:
    result = "neutral"

with open("weather.txt", "w") as data:
    data.write(result)

print(result)
import requests

# The API key
api_key = "52d200dd0dee27f8c8351154b9c6032c"

# Getting user input and the URL
city = input("Enter the city: ")
weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")


# Checking input error
if weather_data.json()['cod'] == '404':
    print("Invalid City")
else:
    weather = weather_data.json()['weather'][0]['main']
    humid = weather_data.json()['main']['humidity']
    temp_f = weather_data.json()['main']['temp']
    temp_c = round((temp_f - 32) * 5 / 9)

    print(f"The weather information for {city} is\n"
          f"Weather: {weather}\n"
          f"Temperature: {temp_c}\n"
          f"Humidity: {humid}")






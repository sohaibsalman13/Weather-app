import requests
from tkinter import messagebox
from tkinter import *
from configparser import ConfigParser

url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

# reading the api key from the config file
config_file = 'config.ini'
config = ConfigParser()
config.read(config_file)
api_key = config['api_key']['key']


def get_weather(city):
    result = requests.get(url.format(city, api_key))

    if result:

        # getting the data from json
        city = result.json()['name']
        country = result.json()['sys']['country']
        weather = result.json()['weather'][0]['main']
        icon = result.json()['weather'][0]['icon']
        humid = result.json()['main']['humidity']
        temp = int(result.json()['main']['temp'] - 273.15)

        # tuple to save all the value
        final = (city, country, temp, icon, weather, humid)
        return final
    else:
        return None


def search():
    city = city_text.get()

    # calling the get_weather function
    weather = get_weather(city)
    if weather:
        # setting the label values from the get_weather function
        location_lbl['text'] = '{}, {}'.format(weather[0], weather[1])
        icon_ref = PhotoImage(file='weather_icons/{}.png'.format(weather[3]))
        image['image'] = icon_ref
        image.image = icon_ref
        temp_lbl['text'] = '{}°C'.format(weather[2])
        weather_lbl['text'] = weather[4]
        humid_lbl['text'] = '{}%'.format(weather[5])

    else:
        # error message for invalid input
        messagebox.showerror('Error', 'Cannot find city {}'.format(city))


# setting the app window
app = Tk()
app.geometry("700x500")
app.title("Weather")
city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()

# setting the search button
search_btn = Button(app, text='Search', width=15, command=search)
search_btn.pack()

# setting the location label
location_lbl = Label(app, text='Location', font=('Bold', 20))
location_lbl.pack()

# setting the weather image
image = Label(app, image='')
image.pack()

# setting the temperature label
temp_lbl = Label(app, text='Temperature')
temp_lbl.pack()

# setting the weather label
weather_lbl = Label(app, text='Weather')
weather_lbl.pack()

# setting the humidity label
humid_lbl = Label(app, text='Humidity')
humid_lbl.pack()

app.mainloop()

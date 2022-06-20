import requests
import tkinter as tk


def func(canvas):
    city = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=52d200dd0dee27f8c8351154b9c6032c"
    json_data = requests.get(api).json()

    weather = json_data['weather'][0]['main']
    humid = json_data['main']['humidity']
    temp = int(json_data['main']['temp']-273.15)
    min_temp = int(json_data['main']['temp_min']-273.15)
    max_temp = int(json_data['main']['temp_max']-273.15)
    pressure = json_data['main']['pressure']
    wind = json_data['wind']['speed']

    final_info = weather + "\n" + str(temp) + "°C"
    final_data = "\n" + "Max temp: " + str(max_temp) + "\n" \
                 + "Min temp: " + str(min_temp) + "\n" + "Pressure: " \
                 + str(pressure) + "\n" + "Humidity: " + str(humid) + "\n" \
                 + "Wind Speed: " + str(wind)

    L1.config(text = final_info)
    L2.config(text = final_data)


canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")

f = ("New Times Roman", 15, "bold",)
t = ("New Times Roman", 30, "bold")

textField = tk.Entry(canvas, font = t)
textField.pack(pady = 20)
textField.focus()
textField.bind('<Return>', func)

L1 = tk.Label(canvas, font = t)
L1.pack()
L2 = tk.Label(canvas, font = f)
L2.pack()

canvas.mainloop()









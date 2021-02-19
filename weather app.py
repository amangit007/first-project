from configparser import ConfigParser
from datetime import datetime
from tkinter import *
from tkinter import messagebox
import requests

url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

config_file = 'config.ini'
config = ConfigParser()
config.read(config_file)
api_key = config['api_key']['key']


def get_wether(city) :
    result = requests.get(url.format(city, api_key))
    if result :
        json = result.json()
        
        city = json['name']
        country = json['sys']['country']
        temp_kelvin = json['main']['temp']
        temp_celsius = temp_kelvin - 273.15
        temp_fahrenheit = (temp_kelvin - 273.15) * 9 / 5 + 32
        icon = json['weather'][0]['icon']
        weather = json['weather'][0]['main']
        desc = json['weather'][0]["description"]
        humidity = json['main']["humidity"]
        pressure = json['main']["pressure"]
        winds = json['wind']["speed"]
        windd = json['wind']["deg"]
        visibility = json['visibility']
        clouds = json['clouds']['all']
        sunr = json['sys']['sunrise']
        sunrise = datetime.fromtimestamp(sunr)
        suns = json['sys']['sunset']
        sunset = datetime.fromtimestamp(suns)
        temp_kelvino = json['main']["temp_min"]
        mincelsius = temp_kelvino - 273.15
        minfar = (temp_kelvino - 273.15) * 9 / 5 + 32
        temp_kelvino = json['main']["temp_max"]
        maxcelsius = temp_kelvino - 273.15
        maxfar = (temp_kelvino - 273.15) * 9 / 5 + 32
        final = (
            city, country, temp_celsius, temp_fahrenheit, icon, weather, desc, humidity, pressure, winds, windd,
            visibility,
            clouds, sunrise, sunset, mincelsius, minfar, maxcelsius, maxfar)
        return final

    else :
        return None


def search() :
    city = city_text.get()
    weather = get_wether(city)
    if weather :
        location_lbl['text'] = '{}, {}'.format(weather[0], weather[1])

        temp_lbl['text'] = '{:.2f}°C,{:.2f}°F'.format(weather[2], weather[3])
        weather_lbl['text'] = 'DESCRIPTION : {} , {}'.format(weather[5], weather[6])

        humid['text'] = 'HUMIDITY : {}%'.format(weather[7])
        pres['text'] = 'PRESSURE : {} hPa'.format(weather[8])
        ws['text'] = 'WIND SPEED : {} meters/second'.format(weather[9])
        wd['text'] = 'WIND DIRECTION : {} degrees'.format(weather[10])
        vi['text'] = 'VISIBILITY : {} Meters'.format(weather[11])
        cl['text'] = 'CLOUDS : {} %'.format(weather[12])
        
        sr['text'] = 'SUNRISE : {} '.format(weather[13])
        ss['text'] = 'SUNSET : {} '.format(weather[14])

        tempi['text'] = 'LOW : {:.2f}°C,{:.2f}°F'.format(weather[15], weather[16])
        tempa['text'] = 'HIGH  : {:.2f}°C,{:.2f}°F'.format(weather[17], weather[18])

    else :
        messagebox.showerror('error', "can't find {}".format(city))


app = Tk()
app.title("weather app")
app.geometry("400x500")
app.configure(background="light blue")

app.iconphoto(True, PhotoImage(file="weather.png"))

so = Label(app, text='GET CURRENT WEATHER DATA BY CITY NAME',fg="red",bg="black",font=("bold",13))
so.pack()

city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()

search_btn = Button(app, text='Search weather', width=12, command=search, activeforeground="white",
                    activebackground="blue", pady=10)
search_btn.pack()

location_lbl = Label(app, text='',background="light blue", font=("bold", 20))
location_lbl.pack()



temp_lbl = Label(app, text="",background="light blue", font=("bold", 24))
temp_lbl.pack()

tempi = Label(app, text="",background="light blue",fg="blue", font=("bold", 12))
tempi.pack()

tempa = Label(app, text="",background="light blue",fg="red", font=("bold", 12))
tempa.pack()

weather_lbl = Label(app, text='',background="light blue",font=("bold"))
weather_lbl.pack()

humid = Label(app, text='',background="light blue", font=("bold"))
humid.pack()

pres = Label(app, text='',background="light blue", font=("bold"))
pres.pack()

ws = Label(app, text='',background="light blue", font=("bold"))
ws.pack()

wd = Label(app, text='',background="light blue", font=("bold"))
wd.pack()

vi = Label(app, text='',background="light blue", font=("bold"))
vi.pack()

cl = Label(app, text='',background="light blue",fg="white", font=("bold", 14))
cl.pack()

sr = Label(app, text='',background="light blue",fg="yellow", font=("bold", 14))
sr.pack()

ss = Label(app, text='',background="light blue",fg="orange", font=("bold", 14))
ss.pack()

bs = Label(app, text='',background="light blue")
bs.pack()

app.mainloop()

import tkinter as tk
import datetime as dt
import requests

class MyGUI:
    
    def __init__(self):
        self.win = tk.Tk()
        self.win.geometry('700x200')
        self.win.title('Weather API')

        self.welcomeLabel = tk.Label(self.win, text="Welcome to Weather Application!", font=('Courier',26))
        self.welcomeLabel.pack(padx=20,pady=20)


        self.cityLabel = tk.Label(self.win, text='Enter the City:', font=('Courier',20))
        self.cityLabel.pack(padx=20)


        self.userCity = tk.StringVar(self.win)
        self.cityTxt = tk.Entry(self.win, font=('Courier',12), textvariable=self.userCity)
        self.cityTxt.pack(padx=20)
        

        self.submitBtn = tk.Button(self.win, text="Generate",command=self.displayCity)
        self.submitBtn.pack(padx=20,pady=20)


        self.win.mainloop()



    def displayCity(self):
        self.cityWeather = tk.Toplevel(bg='Cyan')
        self.cityWeather.geometry('700x300')
        self.cityWeather.title('Weather Report')

        self.location = self.userCity.get()
        self.cityWeather1, self.weatherD, self.cityTemp, self.sunRise, self.sunDown, self.cityWind = self.getWeather(self.location)
        self.cityTempF = round(self.cityTemp * 1.8 + 32, 2)

        self.lbl = tk.Label(self.cityWeather, text='Weather in ' + self.location, font=('Courier',20), bg='White', fg='Gray13')
        self.lbl.pack(padx=20,pady=10)

        self.weatherLbl = tk.Label(self.cityWeather, text='Current Weather: ' + self.cityWeather1, font=('Courier',16), bg='White', fg='Gray13')
        self.weatherLbl.pack(padx=20,pady=5)

        self.weatherDLbl = tk.Label(self.cityWeather, text='Weather Description: ' + self.weatherD, font=('Courier',16), bg='White', fg='Gray13')
        self.weatherDLbl.pack(padx=20,pady=5)
        
        self.windLbl = tk.Label(self.cityWeather, text='Wind Speed(km/h): ' + str(self.cityWind), font=('Courier',16), bg='White', fg='Gray13')
        self.windLbl.pack(padx=20,pady=5)

        self.tLbl = tk.Label(self.cityWeather, text='Tempeature(C): ' + str(self.cityTemp), font=('Courier',16), bg='White', fg='Gray13')
        self.tLbl.pack(padx=20)

        self.tFLbl = tk.Label(self.cityWeather, text='Tempeature(F): ' + str(self.cityTempF), font=('Courier',16), bg='White', fg='Gray13')
        self.tFLbl.pack(padx=20)
        
        self.sunRiseLbl = tk.Label(self.cityWeather, text='Sun Rise in ' + self.location + '(Your Local Time):\n' + str(self.sunRise), font=('Courier',16), bg='White', fg='Gray13')
        self.sunRiseLbl.pack(padx=20, pady=5)

        self.sunDownLbl = tk.Label(self.cityWeather, text='Sun Down in ' + self.location + '(Your Local Time):\n' + str(self.sunDown), font=('Courier',16), bg='White', fg='Gray13')
        self.sunDownLbl.pack(padx=20,pady=5)
        
        self.cityWeather.mainloop()



    def getWeather(self,location):
        apiKey = 'cd32d78eaf78b54f78021be696a47c06'
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={apiKey}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            # Access the weather data from the response
            data = response.json()

            # Extract the relevant weather information
            self.weather = data['weather'][0]['main']
            self.weatherD = data['weather'][0]['description']
            self.temperature = data['main']['temp']
            self.sRTime = data['sys']['sunrise']
            self.sDTime = data['sys']['sunset']
            self.sRTime = dt.datetime.fromtimestamp(self.sRTime)
            self.sDTime = dt.datetime.fromtimestamp(self.sDTime)
            self.wind = data['wind']['speed']
            print(data)

            return self.weather, self.weatherD, self.temperature, self.sRTime, self.sDTime, self.wind

        else:
            # Show an error messagebox if the API request fails
            print('Oopsie!')



        


MyGUI()
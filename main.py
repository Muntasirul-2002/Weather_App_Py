import requests
import json
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")

speak.Speak("Enter the name of the city")
city = input("Enter the name of the city\n")
url = f"https://api.weatherapi.com/v1/current.json?key=bf19d4e2d7de482b84370727232005&q={city}"
r = requests.get(url)
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]
print('Current temperature is: ', wdic["current"]["temp_c"])
speak.Speak(f'The current weather in {city} is{w}degrees')


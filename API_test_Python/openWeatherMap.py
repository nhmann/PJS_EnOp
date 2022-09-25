import requests
import json
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.dates

plz = input("Für welche deutsche Postleitzahl soll die Temperatur angezeigt werden?")
appid = "SECRET_KEY"
country = "de"
units = "metric"
url = "http://api.openweathermap.org/geo/1.0/zip?zip=%s,%s&appid=%s" % (plz, country, appid)
resp = requests.get(url)
coords = json.loads(resp.text)

lat = coords['lat']
lon = coords['lon']

print("Hier ist das Wetter für %s %s, %s:" % (coords['zip'], coords['name'], coords['country']))

url = "https://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&appid=%s&units=%s&lang=%s" % (lat, lon, appid, units, country)
resp = requests.get(url)
weather = json.loads(resp.text)

print("Das aktuelle Wetter in %s beträgt %s°C" % (coords['name'], weather['main']['temp']))


antwort = input("Wollen Sie die Wettervorhersage sehen? [y/n]")
if (antwort.lower().startswith("y")):
    print("Hier ist die Wettervorhersage für %s %s, %s:" % (coords['zip'], coords['name'], coords['country']))
    
    url = "https://api.openweathermap.org/data/2.5/forecast?lat=%s&lon=%s&appid=%s&units=%s&lang=%s" % (lat, lon, appid, units, country)
    resp = requests.get(url)
    forecast = json.loads(resp.text)

    temperatures = []
    dates = []

    for entry in forecast['list']:
        temperatures.append(entry['main']['temp'])
        dates.append(datetime.strptime(entry['dt_txt'], '%Y-%m-%d %H:%M:%S'))

    plt.plot(dates, temperatures)
    plt.xlabel('Zeit')
    plt.ylabel('Temperatur in Grad Celsius')
    plt.title("Wettervorhersage für %s" % (coords['name']))
    plt.show()

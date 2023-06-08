# getOpenWeather.py - Prints the weather for a location from the command line.

APPID = 'Enter APPID HERE'

import json, requests, sys

# Compute location from command line arguments.
if len(sys.argv) < 2:
    print('Usage: getOpenWeather.py city_name, state_name, 2-letter_country_code')
    sys.exit()
location = ' '.join(sys.argv[1:])

# Download the JSON data from openweather.org's API.
findLatLonUrl = f'http://api.openweathermap.org/geo/1.0/direct?q={location}&appid={APPID}'
response = requests.get(findLatLonUrl)
response.raise_for_status()

latLonData = json.loads(response.text)
lon = latLonData[0]['lon']
lat = latLonData[0]['lat']

#Load JSON data into a python variable.
url = f'http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={APPID}'
response = requests.get(url)
response.raise_for_status()

weatherData = json.loads(response.text)

# Print weather descriptions.
w = weatherData['list']

print('The current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])

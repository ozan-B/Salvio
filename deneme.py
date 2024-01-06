import json
import requests

url = 'https://api.ip.sb/geoip'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
getgeo = requests.get(url, headers=headers)
getgeo_json=getgeo.json()

print(getgeo_json['latitude'])


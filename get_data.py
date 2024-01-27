import requests
import time

username = 'leductai'
feed_key = ''

url = f'https://io.adafruit.com/api/v2/{username}/feeds/{feed_key}/data?limit=100'

while(True):
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(data[0]['value'])
        print(data[0]['created_at'])
    else:
        print(f'Request failed with status code {response.status_code}')
    time.sleep(3)
    

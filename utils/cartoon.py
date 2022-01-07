import requests
import logging

from data.config import TOKEN

url = "https://api.deepai.org/api/toonify"
headers = {'api-key': TOKEN}


async def cartoon(img_url):
    r = requests.post(url=url, data={'image': f'{img_url}'},headers=headers)
    print(r.text)
    return r.json()

# -*- coding: utf-8 -*-

import requests

url = 'http://127.0.0.1:8000/diamond_classifier'

s = requests.Session()
payload = '呵呵'

while 1:
    s.post(url, data=payload)

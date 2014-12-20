# -*- coding: utf-8 -*-

import requests

url = 'http://127.0.0.1:8080/diamond_classifier'

s = requests.Session()
payload = {'text': u'呵呵'}

while 1:
    s.post(url, data=payload)

# -*- coding: utf-8 -*-

import requests

url = 'http://127.0.0.1:8080/diamond_classifier'

while 1:
    payload = {'text': u'呵呵'}
    requests.post(url, data=payload)

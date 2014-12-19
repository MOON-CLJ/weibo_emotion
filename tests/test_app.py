# -*- coding: utf-8 -*-

import unittest
import requests


class AppTestCase(unittest.TestCase):
    def setUp(self):
        super(AppTestCase, self).setUp()
        self._url = "http://127.0.0.1:8080/diamond_classifier"

    def test_diamond_classifier(self):
        payload = {'text': 'hehe'}
        r = requests.post(self._url, data=payload)
        self.assertEqual(r.text, '1')
        self.assertEqual(r.status_code, 200)

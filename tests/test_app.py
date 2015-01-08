# -*- coding: utf-8 -*-

import unittest
import requests


class AppTestCase(unittest.TestCase):
    def setUp(self):
        super(AppTestCase, self).setUp()
        self._url = "http://127.0.0.1:8000/diamond_classifier"

    def test_text_hehe(self):
        payload = {'text': 'hehe'}
        r = requests.post(self._url, data=payload)
        self.assertEqual(r.text, '1')
        self.assertEqual(r.status_code, 200)

    def test_text_sad(self):
        payload = {'text': 'sad'}
        r = requests.post(self._url, data=payload)
        self.assertEqual(r.text, '0')
        self.assertEqual(r.status_code, 200)

    def test_text_cn_hehe(self):
        payload = {'text': u'呵呵'}
        r = requests.post(self._url, data=payload)
        self.assertEqual(r.text, '1')
        self.assertEqual(r.status_code, 200)


if __name__ == '__main__':
    unittest.main()

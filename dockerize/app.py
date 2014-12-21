# -*- coding: utf-8 -*-

import falcon

from triple_sentiment_classifier import triple_classifier


def _diamond_classifier(text):
    # 其他类
    sentiment = 0

    text_utf8 = text.encode('utf-8')
    if '【' in text_utf8 and '】' in text_utf8:
        # 简单规则判断新闻类
        sentiment = 4
    else:
        # 积极、愤怒、悲伤3类情感分类器
        sentiment = triple_classifier(text)

    return sentiment


class DiamondClassifierResource:
    def on_post(self, req, resp):
        body = req.stream.read()
        text = body.decode('utf-8', 'ignore')
        resp.body = (str(_diamond_classifier(text)))
        resp.status = falcon.HTTP_200

# falcon.API instances are callable WSGI apps
app = falcon.API()

diamond_classifier = DiamondClassifierResource()

app.add_route('/diamond_classifier', diamond_classifier)

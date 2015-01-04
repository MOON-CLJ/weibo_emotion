# -*- coding: utf-8 -*-

import web

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


class Ping(object):
    def GET(self):
        text = u"哈哈"
        return _diamond_classifier(text)


class DiamondClassifier(object):
    def POST(self):
        i = web.input()
        if hasattr(i, 'text'):
            return str(_diamond_classifier(i.text))
        return "-1"

urls = (
    '/', 'Ping',
    '/diamond_classifier', 'DiamondClassifier'
)

app = web.application(urls, globals())
web.config.debug = False
wsgiapp = app.wsgifunc()

if __name__ == "__main__":
    app.run()

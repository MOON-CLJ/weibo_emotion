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


urls = (
        '/diamond_classifier', 'DiamondClassifier'
)


class DiamondClassifier(object):
    def POST(self):
        i = web.input()
        if hasattr(i, 'text'):
            print [i.text]
            return str(_diamond_classifier(i.text))
        return "-1"


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

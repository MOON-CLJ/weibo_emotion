# -*- coding: utf-8 -*-

import time
import web
import logging

from triple_sentiment_classifier import triple_classifier


logging.basicConfig(format='%(asctime)s %(levelname)s [%(name)s]: %(message)s')
logger = logging.getLogger('weibo_emotion.app')
logger.setLevel(logging.INFO)


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
    def __init__(self):
        self.cnt = 0
        self.last_time = time.time()

    def POST(self):
        self.cnt += 1
        if self.cnt % 1000 == 0:
            now = time.time()
            logger.info(str(now - self.last_time))
            self.last_time = now
        i = web.input()
        if hasattr(i, 'text'):
            return str(_diamond_classifier(i.text))
        return "-1"

app = web.application(urls, globals())


if __name__ == "__main__":
    web.config.debug = False
    app.run()

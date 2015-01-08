# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web


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


class PingHandler(tornado.web.RequestHandler):
    def get(self):
        text = u"哈哈"
        self.write(str(_diamond_classifier(text)))


class DiamondClassifier(tornado.web.RequestHandler):
    def post(self):
        text = self.get_argument('text')
        if text:
            self.write(str(_diamond_classifier(text)))
        self.write("-1")


application = tornado.web.Application([
    (r'/', PingHandler),
    (r'/diamond_classifier', DiamondClassifier),
])

if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()

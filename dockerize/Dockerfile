FROM ubuntu:precise

MAINTAINER chenlijun

ENV DEBIAN_FRONTEND noninteractive

ADD sources.list /etc/apt/sources.list

RUN apt-get update \
     && apt-get install -y gcc python-dev python-setuptools libc6-dev git opencc python-numpy python-scipy gfortran libopenblas-dev liblapack-dev

# swcs
ENV SWCS_DOWNLOAD_URL http://www.xunsearch.com/scws/down/scws-1.2.2.tar.bz2
ENV SWCS_DOWNLOAD_SHA1 8ded9125036cbeadffb86c7ee3f47bb103b99481
ENV SWCS_DICT_CHS_UTF8_DOWNLOAD_URL http://www.xunsearch.com/scws/down/scws-dict-chs-utf8.tar.bz2
ENV SWCS_DICT_CHT_UTF8_DOWNLOAD_URL http://www.xunsearch.com/scws/down/scws-dict-cht-utf8.tar.bz2

RUN buildDeps='make curl bzip2'; \
    set -x; \
    apt-get update && apt-get install -y $buildDeps --no-install-recommends \
    && mkdir -p /usr/src/swcs \
    && curl -sSL "$SWCS_DOWNLOAD_URL" -o swcs.tar.bz2 \
    && echo "$SWCS_DOWNLOAD_SHA1 *swcs.tar.bz2" | sha1sum -c - \
    && tar xvjf swcs.tar.bz2 -C /usr/src/swcs --strip-components=1 \
    && rm swcs.tar.bz2 \
    && cd /usr/src/swcs && ./configure --prefix=/usr/local/scws && cd ~/ \
    && make -C /usr/src/swcs \
    && make -C /usr/src/swcs install \
    && curl -sSL "$SWCS_DICT_CHS_UTF8_DOWNLOAD_URL" -o scws-dict-chs-utf8.tar.bz2 \
    && curl -sSL "$SWCS_DICT_CHT_UTF8_DOWNLOAD_URL" -o scws-dict-cht-utf8.tar.bz2 \
    && tar xvjf scws-dict-chs-utf8.tar.bz2 -C /usr/local/scws/etc \
    && tar xvjf scws-dict-cht-utf8.tar.bz2 -C /usr/local/scws/etc \
    && rm scws-dict-chs-utf8.tar.bz2 \
    && rm scws-dict-cht-utf8.tar.bz2 \
    && echo "/usr/local/scws/lib/" >> /etc/ld.so.conf \
    && ldconfig \
    && rm -r /usr/src/swcs \
    && apt-get purge -y $buildDeps \
    && apt-get autoremove -y

# Set timezone to Shanghai
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

ADD requirements.txt /
RUN easy_install pip
RUN pip install -r requirements.txt

RUN mkdir /data

ADD data /data
ADD app.py /
ADD triple_sentiment_classifier.py /

EXPOSE 8000

CMD ["python", "app.py"]

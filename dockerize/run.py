import os


bin_ = "/Users/clj/www/emotion/bin/gunicorn"
os.execl(bin_, bin_, "--access-logfile", "/tmp/gunicorn.log", "app:app")

import os


bin_ = "/usr/local/bin/gunicorn"
os.execl(bin_, bin_, "--access-logfile", "/tmp/gunicorn.log", "app:app")

import os


bin_ = "/usr/local/bin/gunicorn"
os.execl(bin_, bin_, "--access-logfile", "-b", "0.0.0.0:8000", "/tmp/gunicorn.log", "app:app")

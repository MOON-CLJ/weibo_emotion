import os


bin_ = "/usr/local/bin/gunicorn"
os.execl(bin_, bin_, "-b", "0.0.0.0:8000", "--access-logfile", "/tmp/gunicorn.log", "app:app")

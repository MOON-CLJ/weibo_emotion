start:
	docker run -i -t -p 8000:8000 --net=host weibo_emotion:1.2

bench:
	palb -c 10 -n 10000 http://127.0.0.1:8000/

build:
	lektor build -O tmp
run:
	lektor server -O tmp -p 5001
sponsor-pages:
	python utils/sponsors.py

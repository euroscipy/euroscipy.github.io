build:
	lektor build -O tmp
run:
	lektor server -O tmp -p 5001
sponsor-pages:
	python utils/sponsors.py
talk-pages:
	python utils/talks.py
	python utils/social_cards.py

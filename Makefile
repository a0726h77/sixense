install:
	sudo pip install -r requirements.txt

test:
	coverage run -m unittest discover

clean:
	find -name "*.pyc" -exec rm {} \;

.PHONY: test

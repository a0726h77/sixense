install:
	cp sixense.cfg ~/.sixense.cfg
	sudo pip install -r requirements.txt

clean:
	find -name "*.pyc" -exec rm {} \;

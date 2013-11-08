install:
	cp Slx7hS3ns3onLinux.cfg ~/.Slx7hS3ns3onLinux.cfg
	sudo pip install chromium_compact_language_detector

clean:
	find -name "*.pyc" -exec rm {} \;

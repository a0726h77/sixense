name = 'notify'


def show(content):
    try:
        import pynotify
        pynotify.init('Slx7hS3ns3on')
        notify = pynotify.Notification('Slx7hS3ns3on', content, "dialog-information")
        notify.show()
    except:
        print("**** Requires pynotify. sudo pip install py-notify.")

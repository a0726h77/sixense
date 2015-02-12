name = 'notify'


def show(content):
    try:
        import notify2
        notify2.init('Slx7hS3ns3on')
        notify = notify2.Notification('Slx7hS3ns3on', content, "dialog-information")
        notify.show()
    except:
        print("**** Requires notify. sudo pip install notify2.")

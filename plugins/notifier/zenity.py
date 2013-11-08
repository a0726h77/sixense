name = 'zenity'


def show(content):
    from plugins.libs import PyZenity
    PyZenity.InfoMessage(content)

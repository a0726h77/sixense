name = 'sample_translator'


def isMatch(lang):
    """/*
       Function: isMatch

         check if string match rules.

       Parameters:

         lang - array of expected language code from clipbaord string.

       Returns:

         Boolean if lang match code.
    */"""
    if lang == 'de':
        return True
    else:
        return False


def translate(clipboard_content):
    """/*
       Function: translate

         translate clipbaord string use online/local translate API/tools.

       Parameters:

         clipboard_content - clipboard string.

       Returns:

         translateed string.
    */"""
    content = clipboard_content

    return content

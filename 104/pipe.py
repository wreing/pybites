MESSAGE = """Hello world!
We hope that you are learning a lot of Python.
Have fun with our Bites of Py.
Keep calm and code in Python!
Become a PyBites ninja!"""

def split_in_columns(message=MESSAGE):
    """Split the message by newline (\n) and join it together on '|'
       (pipe), return the obtained output string"""
    a = message.split('\n')
    r = ''
    for x in a:
        if r == '':
            r = x
        else:
            r = r+'|' + x
    return r


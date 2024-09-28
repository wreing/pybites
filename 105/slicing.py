from curses.ascii import islower
from typing import List

from string import ascii_lowercase

TEXT = """
One really nice feature of Python is polymorphism: using the same operation
on different types of objects.
Let's talk about an elegant feature: slicing.
You can use this on a string as well as a list for example
'pybites'[0:2] gives 'py'.
 The first value is inclusive and the last one is exclusive so
here we grab indexes 0 and 1, the letter p and y.
  When you have a 0 index you can leave it out so you can write this as 'pybites'[:2]
but here is the kicker: you can use this on a list too!
['pybites', 'teaches', 'you', 'Python'][-2:] would gives ['you', 'Python']
and now you know about slicing from the end as well :)
keep enjoying our bites!
"""


def slice_and_dice(text: str = TEXT) -> List[str]:
    r = []
    text = text.strip()
    aText = text.split('\n')
    for line in aText:
        line = line.strip()
        if islower(line[0:1]):
            words = line.split()
            w = words[-1]
            if w[-1] in ['.','!']:
                w = w[0:-1]
            r.append(w)

    return r




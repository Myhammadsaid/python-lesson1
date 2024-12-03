print("\n\n")
# import time

# time.sleep(3)
# print('Hello')

import datetime as d, sys, os, platform
import random
from math import sqrt, ceil

# print(d.datetime.now().date())
# print(d.datetime.now().time())

# print(sys.path)
# print(os.name)
# print(platform.system())

# print(sqrt(100))
# print(ceil(sqrt(25)))

# import mymodule as my
# print(my.hello())

from mymodule import add_three_numbers as add
print(add(5,4,4))

import cowsay as c
c.cow('Hello')
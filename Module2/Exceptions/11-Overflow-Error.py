# The code prints subsequent
# values of exp(k), k = 1, 2, 4, 8, 16, ...

from math import exp

ex = 1

try:
    while True:
        try:
            print("Please terminate the process using Keyboard Interrupt")
            print(exp(ex))
            ex *= 2
        except KeyboardInterrupt:
            print("Luckily you terminated the process otherwise an overflow error would eventually occur")
except OverflowError:
    print('The number is too big.')

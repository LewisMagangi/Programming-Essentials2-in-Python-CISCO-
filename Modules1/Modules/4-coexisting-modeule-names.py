import math

def sin(x):    #We've defined our own sin here.
    if 2 * x == pi:
        return 0.99999999
    else:
        return None

pi = 3.14     #We've defined our own pi here.

print(sin(pi/2))
print(math.sin(math.pi/2))

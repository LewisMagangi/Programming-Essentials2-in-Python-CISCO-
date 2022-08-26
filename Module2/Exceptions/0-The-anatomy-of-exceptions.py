"""
try:
    y = 1 / 0
except ArithmeticError:                #Note that replacing the exception's name with either Exception or BaseException won't change the program's behavior.
    print("Oooppsss...")

print("THE END.")
"""

try:
    y = 1 / 0
except ZeroDivisionError:
    print("Oooppsss...")

print("THE END.")

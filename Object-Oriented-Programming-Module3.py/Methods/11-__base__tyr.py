class SuperOne:
    pass


class SuperTwo:
    pass


class Sub(SuperOne, SuperTwo):
    pass


def printBases(cls):
    print('( ', end='')

    for x in cls.__bases__:
        print(x.__name__, end=' ')
    print(')')

SuperOneObject = SuperOne()

printBases(SuperOne)
printBases(SuperTwo)
printBases(Sub)
try:
    print(SuperOneObject.__bases__)
except AttributeError:
    print("The __base__ Atrribute is absent in the object because it only exists inside objects")
    raise

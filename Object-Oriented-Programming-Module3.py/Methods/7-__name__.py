'''
Note: the __name__ attribute is absent from the object - it exists only inside classes.


If you want to find the class of a particular object, you can use a function named type(), which is able (among other things) to find a class which has been used to instantiate any object.
'''
class Classy:
    pass


print(Classy.__name__)
obj = Classy()
print(type(obj).__name__)

try:
    print(obj.__name__)
except AttributeError:
    print("The __name__ Atrribute is absent in the object because it only exists inside objects")
    raise

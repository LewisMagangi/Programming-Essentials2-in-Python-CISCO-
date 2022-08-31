'''
Python's attitude to object instantiation raises one important issue - in contrast to other programming languages, you may not expect that all objects of the same class have the same sets of properties.
'''
class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


example_object = ExampleClass(1)

print(example_object.a)
print(example_object.b)

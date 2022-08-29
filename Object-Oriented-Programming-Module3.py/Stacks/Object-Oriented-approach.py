class Stack:  # Defining the Stack class.
    def __init__(self):  # Defining the constructor function.
        print("Hi!")


stack_object = Stack()  # Instantiating the object.

class Stack:
    def __init__(self):
        self.stack_list = []


stack_object = Stack()
print(len(stack_object.stack_list))

'''
The object approach: a stack from scratch
Now it's time for the two functions (methods) implementing the push and pop operations. Python assumes that a function of this kind (a class activity) should be immersed inside the class body - just like a constructor.

We want to invoke these functions to push and pop values. This means that they should both be accessible to every class's user (in contrast to the previously constructed list, which is hidden from the ordinary class's users).

Such a component is called public, so you can't begin its name with two (or more) underscores. There is one more requirement - the name must have no more than one trailing underscore. As no trailing underscores at all fully meets the requirement, you can assume that the name is acceptable.

The functions themselves are simple. Take a look:

class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
       The class declaration is complete, and all its components have been listed. The class is ready for use. self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        delwith __stack_list ready to be used, you can perform the third and last step  self.__stack_list[-1]
        return val


stack_object = Stack()

stack_object.push(3)
stack_object.push(2)
stack_object.push(1)

print(stack_object.pop())
print(stack_object.pop())
print(stack_object.pop())


However, there's something really strange in the code. The functions look familiar, but they have more parameters than their procedural counterparts.

Here, both functions have a parameter namednext, you need to get to the __stack_list list  self at the first position of the parameters list.

Is it needed? Yes, it is.

All methods have to have this parameter. It plays the same role as the first constructor parameter.

It allows the method to access entities (properties and activities/methods) carried out by the actual object. You cannot omit it. Every time Python invokes a method, it implicitly sends the current object as the first argument.

This means that a method is obligated to have at least one parameter, which is used by Python itself - you don't have any influence on it.

If your method needs no parameters at all, this one must be specified anyway. If it's designed to process just one parameter, you have to specify two, and the first one's role is still the same.

There is one more thing that requires explanation - the way in which methods are invoked from within the __stack_list variable.

Fortunately, it's much simpler than it looks:

the first stage delivers the object as a whole 
'''
class Stack:
    def __init__(self):
        self.__stack_list = []


    def push(self, val):
        self.__stack_list.append(val)


    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


stack_object = Stack()

stack_object.push(3)
stack_object.push(2)
stack_object.push(1)

print(stack_object.pop())
print(stack_object.pop())
print(stack_object.pop())

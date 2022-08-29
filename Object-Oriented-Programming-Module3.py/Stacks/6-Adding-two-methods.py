'''
The object approach: a stack from scratch (continued)
Secondly, let's add two methods. But let us ask you: is it really adding? We have these methods in the superclass already. Can we do something like that?

Yes, we can. It means that we're going to change the functionality of the methods, not their names. We can say more precisely that the interface (the way in which the objects are handled) of the class remains the same when changing the implementation at the same time.

Let's start with the implementation of the push function. This is what we expect from it:

to add the value to the __sum variable;
to push the value onto the stack.
Note: the second activity has already been implemented inside the superclass - so we can use that. Furthermore, we have to use it, as there's no other way to access the __stackList variable.

This is how the push method looks in the subclass:

def push(self, val):
    self.__sum += val
    Stack.push(self, val)


Note the way we've invoked the previous implementation of the push method (the one available in the superclass):

we have to specify the superclass's name; this is necessary in order to clearly indicate the class containing the method, to avoid confusing it with any other function of the same name;
we have to specify the target object and to pass it as the first argument (it's not implicitly added to the invocation in this context.)
We say that the push method has been overridden - the same name as in the superclass now represents a different functionality.

'''
class Stack:
    def __init__(self):
        self.__stackList = []

    def push(self, val):
        self.__stackList.append(val)

    def pop(self):
        val = self.__stackList[-1]
        del self.__stackList[-1]
        return val


class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0


# Enter code here.

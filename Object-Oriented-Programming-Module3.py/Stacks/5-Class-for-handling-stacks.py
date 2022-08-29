'''
The object approach: a stack from scratch (continued)
Now let's go a little further. Let's add a new class for handling stacks.

The new class should be able to evaluate the sum of all the elements currently stored on the stack.

We don't want to modify the previously defined stack. It's already good enough in its applications, and we don't want it changed in any way. We want a new stack with new capabilities. In other words, we want to construct a subclass of the already existing Stack class.

The first step is easy: just define a new subclass pointing to the class which will be used as the superclass.

This is what it looks like:

class AddingStack(Stack):
    pass


The class doesn't define any new component yet, but that doesn't mean that it's empty. It gets all the components defined by its superclass - the name of the superclass is written before the colon directly after the new class name.

This is what we want from the new stack:

we want the push method not only to push the value onto the stack but also to add the value to the sum variable;
we want the pop function not only to pop the value off the stack but also to subtract the value from the sum variable.

Firstly, let's add a new variable to the class. It'll be a private variable, like the stack list. We don't want anybody to manipulate the sum value.

As you already know, adding a new property to the class is done by the constructor. You already know how to do that, but there is something really intriguing inside the constructor. Take a look:

class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0


The second line of the constructor's body creates a property named __sum - it will store the total of all the stack's values.

But the line before it looks different. What does it do? Is it really necessary? Yes, it is.

Contrary to many other languages, Python forces you to explicitly invoke a superclass's constructor. Omitting this point will have harmful effects - the object will be deprived of the __stack_list list. Such a stack will not function properly.

This is the only time you can invoke any of the available constructors explicitly - it can be done inside the subclass's constructor.

Note the syntax:

you specify the superclass's name (this is the class whose constructor you want to run)
you put a dot (.)after it;
you specify the name of the constructor;
you have to point to the object (the class's instance) which has to be initialized by the constructor - this is why you have to specify the argument and use the self variable here; note: invoking any method (including constructors) from outside the class never requires you to put the self argument at the argument's list - invoking a method from within the class demands explicit usage of the self argument, and it has to be put first on the list.
Note: it's generally a recommended practice to invoke the superclass's constructor before any other initializations you want to perform inside the subclass. This is the rule we have followed in the snippet.

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


class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

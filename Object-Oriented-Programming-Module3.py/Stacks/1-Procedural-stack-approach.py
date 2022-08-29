'''
The stack - the procedural approach
First, you have to decide how to store the values which will arrive onto the stack. We suggest using the simplest of methods, and employing a list for this job. Let's assume that the size of the stack is not limited in any way. Let's also assume that the last element of the list stores the top element.

The stack itself is already created:

stack = []


We're ready to define a function that puts a value onto the stack. Here are the presuppositions for it:

the name for the function is push;
the function gets one parameter (this is the value to be put onto the stack)
the function returns nothing;
the function appends the parameter's value to the end of the stack;
This is how we've done it - take a look:

def push(val):
    stack.append(val)


Now it's time for a function to take a value off the stack. This is how you can do it:

the name of the function is pop;
the function doesn't get any parameters;
the function returns the value taken from the stack
the function reads the value from the top of the stack and removes it.
'''
stack = []


def push(val):
    stack.append(val)


def pop():
    val = stack[-1]
    del stack[-1]
    return val


push(3)
push(2)
push(1)

print(pop())
print(pop())
print(pop())

# Testing properties: instance variables.
"""
Note: the existence of the supVar variable is obviously conditioned by the Super class constructor invocation. Omitting it would result in the absence of the variable in the created object (try it yourself).
"""
class Super:
    def __init__(self):
        self.supVar = 11

class Sub(Super):
    def __init__(self):
        super().__init__()
        self.subVar = 12

obj = Sub()

print(obj.subVar)
print(obj.supVar)
                                                

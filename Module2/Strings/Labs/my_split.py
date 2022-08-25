def mysplit(strng):
    x = 0
    my_list = list(strng)
    for i in range(1, len(my_list) - 1):
        if my_list[i] is not " ":
            my_list[x] += my_list[i]
        else :
            x += 1
           # del my_list[i]
    return my_list

"""
print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
"""

print(mysplit("To be or not to be, that is the question"))

def mysplit(strng):
    x = 0
    my_list = []
    word = ''
    for char in strng:
        if char is not " ":
            word += char
        else:
            my_list.append(word)
            word = ''
    my_list.append(word)
    return my_list 

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))

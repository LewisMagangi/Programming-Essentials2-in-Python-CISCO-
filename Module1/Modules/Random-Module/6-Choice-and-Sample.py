from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""The first choice function chooses a "random" element from the input sequence and returns it."""

print(choice(my_list))
print(sample(my_list, 5))    # builds a list (a sample) consisting of the elements_to_choose element "drawn" from the input sequence.
print(sample(my_list, 10))

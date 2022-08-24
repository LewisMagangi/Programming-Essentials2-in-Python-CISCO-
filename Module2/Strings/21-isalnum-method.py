# Demonstrating the isalnum() method:
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())

"""Hint: the cause of the first result is a space - it's neither a digit nor a letter."""
t = 'Six lambdas'
print(t.isalnum())  

t = '^@%'
print(t.isalnum())

t = '20E1'
print(t.isalnum())

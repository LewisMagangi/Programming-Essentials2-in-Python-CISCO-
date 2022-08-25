# Demonstrating the lstrip() method:
print("[" + "            I'm a fantastic kid working on my goals                  ".lstrip() + "]")
random_string = '   this is good '

# Leading whitepsace are removed
print(random_string.lstrip())

# Argument doesn't contain space
# No characters are removed.
print(random_string.lstrip('sti'))

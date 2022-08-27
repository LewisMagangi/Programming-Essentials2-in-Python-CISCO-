# This code causes the MemoryError exception.
# Warning: executing this code may affect your OS.
# Don't run it in production environments!

string = 'x'
try:
    while True:
        try:
            print("Please stop the infinite loop; by pressing Cntrl-C before you run out of memory")
            string = string + string
            print(len(string))
        except KeyboardInterrupt:
            print('Luckily you stopped the program otherwise you were at risk of running out of memory')
            break
except MemoryError:
    print('This is not funny!')


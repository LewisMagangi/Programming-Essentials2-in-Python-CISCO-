from math import sin, pi    # carry out the selective import;

print(sin(pi / 2))    #make use of the imported entities and get the expected result (1.0)

""" redefine the meaning of pi and sin - in effect, they supersede the original (imported) definitions within the code's namespace;
 get 0.99999999, which confirms our conclusions."""
pi = 3.14

def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None

print(sin(pi / 2))    

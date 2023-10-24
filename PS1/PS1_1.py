import numpy as np
import random

def Print_values(a,b,c):
    if a>b:
        if b>c:
            print(str(a) + ", " + str(b) + ", " + str(c))
        else:
            if a>c:
                print(str(a) + ", " + str(c) + ", " + str(b))
            else:
                print(str(c) + ", " + str(a) + ", " + str(b))
    else:
        if b>c:
            if a>c:
                print(str(b) + ", " + str(a) + ", " + str(c))
            else:
                print(str(b) + ", " + str(c) + ", " + str(a))
        else:
            print(str(c) + ", " + str(b) + ", " + str(a))
 
    
 
# Check output with some random a, b, and c
for _ in range(3):
    a = random.randint(1,1000)
    b = random.randint(1,1000)
    c = random.randint(1,1000)
print("Random numbers a, b, c:\n" + str(a) + ", " + str(b) + ", " + str(c) +"\n")


print("Print a, b and c in the given order:")
Print_values(a,b,c)          

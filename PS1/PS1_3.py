import numpy as np
import random

n=300
k=100

def coeff(n,k):
    if k==0 or k==n:
        return 1
    else:
        return coeff(n-1,k-1)+coeff(n-1,k)
    
    
def Pascal_triangle(k) : 
 
    line = [] 
     
    line.append(1)  #The first number of a line
     
# For the input do not match the row numbers:
    if k<=0:
        return "Please input a positive integer to get the k-th line of Pascal's triangle"

# For the 1-st line:
    if k==1:
        return line
     
    # Generate the previous row 
    prev = Pascal_triangle(k - 1) 
 
    for i in range(1, len(prev)) :
        num = prev[i - 1] + prev[i]
        line.append(num)
 
    line.append(1)   #The last number of a line
     
    # Return the row 
    return line


print('Pascal_triangle(100):\n', Pascal_triangle(100))
print('-'*100)
print('Pascal_triangle(200):\n', Pascal_triangle(200))



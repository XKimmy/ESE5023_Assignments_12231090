import numpy as np
import random

# Define a recursive function to get the least times to reach the target number
def moveTimes(current, target):
        if current == target:
            return 0
        if current > target:
            return float('inf')

        double_moves = 1 + moveTimes(current * 2, target)
        add_moves = 1 + moveTimes(current + 1, target)

        return min(double_moves, add_moves)


# Define whether the input number is an integer between 1 and 100
def inputCheck(num):
    if num.isnumeric():  # if the input is number or not
        num = int(num)  
        
        if 1 <= num <= 100:  # if the input is in the interval
            return True
    return False

def least_moves():
    x = input("Please input an integer from 1 to 100:")
    
    if inputCheck(x):
        min_moves = moveTimes(1, int(x))
        
        print("\nThe smallest times of moves from 1 RMB to", x, "RMB is", min_moves, ".")
    
    else:
        print("\nPlease check your input is an integer ranging from 1 to 100")

least_moves()
import numpy as np
import random

# Define whether the input number is an integer between 1 and 100
def inputCheck(num):
    if num.isnumeric():  # if the input is number or not
        num = int(num)  
        
        if 1 <= num <= 100:  # if the input is in the interval
            return True
    return False


def Find_expression():
    
    target = input("Please input an integer from 1 to 100:")
    
    if inputCheck(target):
        
        # Initialize a list to store expressions
        expressions = ['1']
        
        for i in range(2, 10):
            new_expressions = []
            for expression in expressions:
                new_expressions.append(expression + '+' + str(i))
                new_expressions.append(expression + '-' + str(i))
                new_expressions.append(expression + str(i))
            expressions = new_expressions
        
        # Evaluate and print expressions that match the target
        for expression in expressions:
            if eval(expression) == int(target):
                print(expression + '=' + str(target))

    
    else:
        print("\nPlease check your input is an integer ranging from 1 to 100")
        
Find_expression()
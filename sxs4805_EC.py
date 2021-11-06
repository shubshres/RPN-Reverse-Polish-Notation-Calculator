# Name: Shubhayu Shrestha 
# NetID: 100174804
# Date Turned In: 11/6/21
# OS Used: MacOS
# Python Version: 3.9.5

# For the bonus I added '^' and '%' functionality 

# import statements 
import os

# defining a function that will define the operations and the results
def expression(operator, num1, num2): 
    # checking for addition 
    if operator == '+':
        return num1+num2
    # checking for subtraction
    elif operator == '-':
        return num1-num2
    # checking for multiplication
    elif operator == '*':
        return num1*num2
    # checking for division 
    elif operator == '/':
        return num1/num2
    elif operator == '^':
        return pow(num2,num1)
    elif operator == '%':
        return num2%num1

# function that will calculate RPN
def RPNCalc (rpn, operators):
    # seperating the string splitting at space
    rpnSplit = rpn.split()
    
    #creating stack
    stack = []

    for i in rpnSplit:
        # checking if i is an operator
        if i in operators: 
            # popping the number and typecasting it to an int
            num2 = stack.pop()
            
            # popping the number and typecasting it to an int    
            num1 = stack.pop()

            # calculating the expression
            result = expression(i,num1, num2)

            # adding the result into the stack
            stack.append(result)
        
        else:
            # else, push the numbers back into stack
            stack.append(float(i))
        
    # return the last elemennt in stack -- result of rpn
    return (stack.pop())

operators = ['+', '-', '*', '/', '^', '%']

# opening file input_RPN.txt as read
inputFile = open('input_RPN_EC.txt', 'r')

# storing contents of file
fileContents = inputFile.readlines()

for line in fileContents:
    # storing contents of line in file on rpn
    rpn = line

    print(RPNCalc(rpn, operators))

# closing the input file
inputFile.close()
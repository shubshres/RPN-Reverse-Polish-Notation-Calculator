# RPN-Reverse-Polish-Notation-Calculator-
Created a RPN (Reverse Polish Notation) Calculator Using Python
Used Python to create a simple calculator that accepts Reverse Polish Notation (RPN) and displays the final answer (Intermediate steps or results need not be displayed).

It only accepts 4 operators “+”, “-“, “*”, “/”.

Input numbers will be single digits.

The input will be in postfix notation.

The input will be provided in a text file called input_RPN.txt. Your program should not ask the user for any input.

There will be one RPN expression in each line.

The code is able to read the file and print the result for each RPN in a new line. 

Example of RPN: 4 2 + and your output should be 6. This is a simple expression. More complex algebraic notations will be used to test your program like the one below. 

Example algebraic notation: ( 4 + 2 * 5 ) / ( 1 + 3 * 2 )

Translated into RPN: 4 2 5 * + 1 3 2 * + /

Code is able to read the input file from the same folder.

Extra credit (5 points each) -- Only Did Part B
A) Write a separate program that can input an algebraic expression and convert it to RPN and then evaluate the RPN. Print the RPN and the result in separate lines. If you are implementing extra credit, your file should be name as <netid>_EC.py. The input file name will be input_RPN_EC.txt and it will have algebraic expressions.
  
B) Add at least one more operator (unary subtraction, or modulo division, etc.). You must document what operators you are adding. Add which ones to comments and make sure to include that as well in your submission so the GTA knows to test using the extra scenarios.

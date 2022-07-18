"""
Creator: Clark Coberly
Date: 5/11/2022
Purpose: Grow skills as a programmer and have a little fun making a simple calculator.
"""

# Plan:

# User puts in a line of text that they would like to have calulated, split into it's various parts
operator_stack = []
expression = []
integer_stack = []
integers = ''
split_expression = False

print('-------------------------------------\n WELCOME TO YOUR FAVORITE CALCULATOR')
user_request = input('Type in your algebraic expression: ')

# Checks each element within the string to determine how the numbers should be split up and manipulated.
for i in range(len(user_request)):
    if user_request[i] in ('+', '-', '*', '//', '%', '^', '/'):
        operator_stack.append(user_request[i])
        split_expression = True

        # If there is not an operator than the number must be a continuation of the previous number

    # Checks to see if it is the last item in user_request and adds final integer to the integers.
    if i + 1 == int(len(user_request)):
        split_expression = True
        integers = (integers + user_request[i])

    if not split_expression:
        integers = (integers + user_request[i])
    
        
    else:
        expression.append(integers)
        expression.append(None)

        # Resets the previous statements to allow for another round of integers and operators
        split_expression = False

        assert split_expression == False, "Make sure that the above expression resets to False or it won't add numbers correctly"
        
        integers = ''

# Get rid of leftover None in list
expression.pop()

# Take the None sections of the problem and be able to replace them with their proper operator
for i in range(len(expression) - 1, 0, -1):
    if expression[i] == None:
        expression[i] = operator_stack.pop()
number1 = expression[0]
for i in range(len(expression) - 2):
    operator = expression[i + 1]
    number2 = expression[i + 2]

    number1 = eval(number1, operator, number2)
    print(number1)


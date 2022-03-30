"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, add_mult, add_cubes )


# Replace this with your code
    # repeat forever:
    # read input
    # tokenize input
    #     if the first token is "q":
    #         quit
    #     else:
    #         (decide which math function to call based on first token)
    #         if the first token is 'pow':
    #               call the power function with the other two tokens

    #         (...etc.)

# while is true
# input()
# .split(' ')
#     if token == 'q':
#         break
#     else:
#         if len(token) <= 2:
#             print('try again')
                
# operator = token[0]

while True:
    user_input = input('Enter your equation: \n > ')
    tokenization = user_input.split(' ')

    #if user wants to quit, enter q
    
    if tokenization[0].lower() == "q":
        break

    #handling enough valid arguments error    

    if len(tokenization) < 2:
        print('Try again! Calculation requires 2 or more arguments!')
        continue
        

    operator = tokenization[0]
    num1 = tokenization[1]

    #adding new variable 'num2' if there is a second number/argument
    
    if len(tokenization) > 2:
        num2 = tokenization[2]
        
    #adding new variable 'num3' if there is a third number/argument

    if len(tokenization) > 3:
        num3 = tokenization[3]

    #actual calls to arithmetic functions / doing the actual calculations

    if operator == '+':
        print(add(float(num1),float(num2)))
    elif operator == '-':
        print(subtract(float(num1), float(num2)))
    elif operator == '*':
        print(multiply(float(num1),float(num2)))
    elif operator == '/':
        print(divide(float(num1), float(num2)))
    elif operator == 'square':
        print(square(float(num1)))
    elif operator == 'cube':
        print(cube(float(num1)))
    elif operator == 'pow':
        print(power(float(num1), float(num2)))
    elif operator == 'mod':
        print(mod(float(num1), float(num2)))
    elif operator == "x+":
        print(add_mult(float(num1), float(num2), float(num3)))
    elif operator == "cubes+":
        print(add_cubes(float(num1), float(num2)))








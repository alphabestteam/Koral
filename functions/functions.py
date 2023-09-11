import math 
import random


def plus(num1 = 0, num2 = 0) -> int:
    # The function will gets 2 numbers
    # The function will return the sum value of the 2 input numbers

    return num1 + num2


def greet_name(name_input: str) -> None:
    # The function gets a string that contains a name
    # The function will print the str: "Hello {name} great to see you!"

    print(f"Hello {name_input}! Great to see you!")



def equationroots(a: int, b: int, c: int) -> int: 
    # The function gets 3 numbers, a , b and c 
    # The function returns the answer of the quadratic equation

    if a == 0:
        print("Wrong input! a can't be zero! ")
    
    else:
        discriminants  = b * b - 4 * a * c 
        sqrt = math.sqrt(abs(discriminants)) 

        if discriminants > 0: 
            print((-b + sqrt)/(2 * a)) 
            print((-b - sqrt)/(2 * a)) 
        
        elif discriminants == 0: 
            print(-b / (2 * a)) 

        else:
            print(- b / (2 * a), " + i", sqrt) 
            print(- b / (2 * a), " - i", sqrt) 


def int_random_between_inputs(num1_input: int, num2_input: int) -> int:
    # The function gets 2 numbers
    # the function returns a random int number between the input numbers.

    return random.randint(num1_input, num2_input)



def float_random_between_inputs(num1_input: float, num2_input: float) -> float:
    # The function gets 2 numbers
    # the function returns a random float number between the input numbers.

    return random.uniform(num1_input, num2_input)    

def sum_from_one_to_hundred() -> None:
    # The function will sum up from 1 to 100

    sum = 0
    for i in range(100):
        sum += i


def factorial(num_input: int) -> None:
    # The function will get a number input
    # The function will prints the factorial of the input number

    factorial = 1    
    if num_input < 0:    
        print(" Wrong Input! Factorial doesn't exist for negative numbers")    
    elif num_input == 0:    
        print("The factorial of 0 is 1")    
    else:    
        for i in range(1, num_input + 1):    
            factorial = factorial * i    
        print(f"The factorial of {num_input} is: {factorial}")    


def main():
    factorial(5)
    factorial(6)
    factorial(7)
    factorial(8)


if __name__ == "__main__":
    main()
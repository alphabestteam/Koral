def sum_from_one_to_hundred() -> None:
    # The function will sum up from 1 to 100

    sum = 0
    for i in range(100):
        sum += i
        
def is_primery(input_number: int) -> None:
  # The function gets a number input
  # The function will return if the number is primary or not 

  for i in range(2, input_number):
    if (input_number % i) == 0: # if there is a number that the number is dividing with him , its not a primary number
      return False
  return True


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
    print(is_primery(5))
    print(is_primery(6))
    print(is_primery(7))
    print(is_primery(14))
    print(is_primery(152))
    print(is_primery(60693))
    factorial(5)
    factorial(6)
    factorial(7)
    factorial(8)


if __name__ == "__main__":
    main()


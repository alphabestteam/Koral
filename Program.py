def sum_from_one_to_hundred():
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


def main():
    print(is_primery(5))
    print(is_primery(6))
    print(is_primery(7))
    print(is_primery(14))
    print(is_primery(152))
    print(is_primery(60693))


if __name__ == "__main__":
   main()
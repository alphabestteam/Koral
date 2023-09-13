N = 40

from Person1 import Person

"""
Exceptions:
"""


def is_error() -> None:
    while True:
        try:
            num1 = int(input('Enter an integer: '))
            num2 = int(input('Enter an integer: '))
            print(num1, num2)
            print("Finished Running")
            break
        except Exception:
            print('Enter a valid integer')


"""
List Comprehension:
"""


def squr_list():

    new_squr = [x*x for x in range(1, N)]


def is_above_18():

    new_list = [Person() for x in range(N)]
    person_override_list = [x for x in new_list if x.get_age() > 18]




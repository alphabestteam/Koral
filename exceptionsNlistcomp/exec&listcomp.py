N = 40

from Person import Person

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

    newsqur = [x*x for x in range(1, N)]


def is_above_18():

    newlist = [Person() for x in range(N) if Person.get_age > 18 ]


if __name__== "__main__":
    squr_list()
    


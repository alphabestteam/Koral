def words_length(*args) -> None:
    sum = 0
    for i in args:
        sum += len(i)
    print(sum)


def total_age(**kwargs) -> None:
    sum = 0
    for key, value in kwargs.items():
        print(f"the age of {key} is {value}")
        sum += value
    print(f"the sum of the ages is : {sum}")


def main():
    words_length("i" , "love", "mom" ,"alot")
    total_age(age1=10, age2=20, age3 = 30)
if __name__ == "__main__":
    main()
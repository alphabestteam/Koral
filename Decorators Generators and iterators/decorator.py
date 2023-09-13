import time

def timer(func):
    def time_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f"The function {func.__name__} took {total_time:.3f} seconds")

    return time_wrapper


@timer
def calc_sum_until_nums_squr(num):
    total = sum((number for number in range(0, num * num)))
    return total


if __name__ == "__main__":
    calc_sum_until_nums_squr(10)
    calc_sum_until_nums_squr(100)
    calc_sum_until_nums_squr(1000)
    calc_sum_until_nums_squr(10000)
from functools import wraps
import time


def measure_execution_time(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        start_timestamp = time.perf_counter()
        result = function(*args, **kwargs)
        end_timestamp = time.perf_counter()
        execution_time = end_timestamp - start_timestamp
        print(f"Function {function.__name__}{args} took {execution_time}")
        return result

    return wrapper


@measure_execution_time
def get_minimum_sorting_range(list_of_integers: list[int]) -> tuple[int, int]:
    index_range = len(list_of_integers) - 1
    first_unsorted_index = last_unsorted_index = -1

    if index_range > 1:
        for index in range(index_range):
            if list_of_integers[index] > min(list_of_integers[index:]):
                first_unsorted_index = index
                break
        for index in range(index_range, 0, -1):
            if list_of_integers[index] < max(list_of_integers[0:index]):
                last_unsorted_index = index
                break

    return first_unsorted_index, last_unsorted_index

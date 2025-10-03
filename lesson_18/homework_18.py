# генератор чётных чисел

def even_numbers_generator(n: int):
    i = 0
    while i <= n:
        yield i
        i += 2


print()
print("- Even numbers generator -")
for num in even_numbers_generator(10):
    print(num)
print("-" * 80)
print()


# генератор чисел Фибоначчи

def fibonacci_generator(n: int):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b


print("- Fibonacci generator -")
for num in fibonacci_generator(60):
    print(num)
print("-" * 80)
print()


# итератор обратного выведения элементов в списке

class ReverseListIterator:

    def __init__(self, data: list):
        self._data = data  # я так понимаю, что все переменные внутри итераторов должны быть защищенными или приватными?
        self._element_index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self._element_index == 0:
            raise StopIteration

        self._element_index -= 1
        return self._data[self._element_index]


my_list = [10, 20, 30, 40, 50]
print("- Reverse list iterator -")
for item in ReverseListIterator(my_list):
    print(item)
print("-" * 80)
print()


# итератор парных чисел в заданном диапазоне

class IteratorEvenInRange:

    def __init__(self, n: int):
        self._n = n
        self._current_num = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._current_num > self._n:
            raise StopIteration

        result = self._current_num
        self._current_num += 2
        return result


print("- Iterator of even numbers in given range -")
for num in IteratorEvenInRange(60):
    print(num)
print("-" * 35)
print()

# декоратор для вывода аргументов и результата функции

print("- Decorator for function arguments and function result -")
print()

def args_results_decorator(func):
    def wrapper(*args, **kwargs):
        args_str = [str(a) for a in args]
        kwargs_str = [f"{k}={v}" for k, v in kwargs.items()]

        joined_args = ", ".join(args_str + kwargs_str)

        print(f"Function arguments: ({joined_args})")

        result = func(*args, **kwargs)

        print(f"Function result: {result}")
        return result

    return wrapper


@args_results_decorator
def calculate_power(base, exponent=2):
    return base ** exponent


calculate_power(5, exponent=4)

print("-" * 80)
print()


# декоратор для отлова исключений

def catch_exceptions_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as exept:
            print(f"ERROR: Exception occurred: {exept}")

            return None

    return wrapper


@catch_exceptions_decorator
def simple_divide(a, b):
    return a / b


@catch_exceptions_decorator
def pick_index(data_list):
    return data_list[1000]


print("- Decorator for exeptions -")
print()

# success
result = simple_divide(10, 2)
print(f"Divide result: {result}")

# ZeroDivisionError
error_zero_division = simple_divide(10, 0)

# IndexError
index_error = pick_index([1, 2, 3])

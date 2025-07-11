my_list = list(range(15))

# я так поняла, что в условии ПАРНЫЕ числа - это чётные числа. Код написан для поиска и сложения чётных чисел.
even_numbers = []

for number in my_list:
    if number % 2 == 0:
        even_numbers.append(number)

sum_even_numbers = sum(even_numbers)
print()
print(f"Sum of even numbers: {sum_even_numbers}")



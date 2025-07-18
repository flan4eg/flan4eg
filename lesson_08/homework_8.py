def calculate_sum_of_numbers(numbers):
    final_sum = 0
    numbers_in_string = numbers.split(',')
    for number in numbers_in_string:
        try:
            final_sum += int(number)
        except ValueError:
            return "I can't do this!"
    return final_sum


my_list = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

for item in my_list:
    sum_of_numbers = calculate_sum_of_numbers(item)
    print()
    print(sum_of_numbers)
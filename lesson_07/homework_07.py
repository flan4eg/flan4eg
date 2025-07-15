# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
print()
print("Task 1:")

def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помилка, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15
print()
print("Task 2:")

# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_of_two_numbers(number1, number2):
    result = number1 + number2
    return result

number1 = 3
number2 = 5
print(f"Sum of your numbers is: {sum_of_two_numbers(number1, number2)}")

print()

# task 3
print("Task 3:")
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def arithmetic_mean(numbers):
    result = sum(numbers) / len(numbers)
    return result

my_numbers = [1, 2, 3, 4, 5]
print(f"Arithmetic mean of this list is {arithmetic_mean(my_numbers)}")
print()

# task 4
print("Task 4:")
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def string_reverse(users_string):
    return users_string[::-1]

users_string = input("Enter a string you want to reverse: ")
print(f"Your reversed text will be like this:{string_reverse(users_string)}")
print()

# # task 5
print("Task 5:")
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def max_len_word(words):
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

words_list = input("Enter a list of words you want to compare by length: ").split()
print(f"The longest word in your text is: {max_len_word(words_list)}")
print()

# task 6
print("Task 6:")
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    return str1.find(str2)

print("First case with find_substring function:")
str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7
print()

print("Second case with find_substring function:")
str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1
print()

# # task 7
""" Виведіть, скільки слів у тексті починається з Великої літери?    homework_04
"""
print("Task 7")

def capital_letter_word(words):
    words_count = 0
    for word in words:
        if word[0].isupper():
            words_count += 1
    return words_count

words_list = input("Enter a list of words with Capital letters: ").split()
print(f"There are {capital_letter_word(words_list)} capital letters in your text")
print()

# # task 8
""" Виведіть позицію, на якій слово Tom зустрічається вдруге   homework_04
"""
print("Task 8") # функция для поиска позиции любого слова во введенном тексте

def word_of_interest(text, find_me_word):
    word_search = text.find(find_me_word)
    if word_search != -1:
        new_start = word_search + len(find_me_word)
        word_search_2 = text.find(find_me_word, new_start)
        if word_search_2 == -1:
            print("The word '" + find_me_word + "' appears only once in your text")
        else:
            print(f"On this position your word appears at the second time: {word_search_2}")
    else:
        print("The word '" + find_me_word + "' doesn't appear in your text al all")

text = input("Enter your text were you want to search specifical word: ")
find_me_word = input("Enter the word you want to find it this text: ")
word_of_interest(text, find_me_word)
print()

# task 9
print("Task 9:")
'''Введите строку и посчитайте в ней количество уникальных символов,
если их больше 10 - выведите True, если менее 10 - выведите False        homework_6_1'''

def count_unic_symbols(users_string):
    amount_unic_symbols = len(set(users_string))
    if amount_unic_symbols >= 10:
        return True
    else:
        return False

users_string = input("Enter your string with 10 or more unic symbols: ")
print(count_unic_symbols(users_string))
print()

# task 10
'''      Функция ищет есть ли в строке буква "h"    homework_6_2   '''
print("Task 10:")

def find_h_letter():
    while True:
        users_word = input("Input word with 'h' letter: ")
        lower_h = users_word.lower()
        if 'h' in lower_h:
            print("Yes, this word has letter 'h'")
            break
        else:
            print("There is no 'h' letter in this word - input another word!")

find_h_letter()
print()


"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
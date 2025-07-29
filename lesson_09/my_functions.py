"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""

def find_substring(str1, str2):
    return str1.find(str2)


""" Виведіть, скільки слів у тексті починається з Великої літери?    homework_04
"""

def capital_letter_word(words):
    words_count = 0
    for word in words:
        if word[0].isupper():
            words_count += 1
    return words_count


""" Функция для поиска позиции любого слова во введенном тексте   homework_04
"""

def word_of_interest(text, find_me_word):
    word_search = text.find(find_me_word)
    if word_search != -1:
        new_start = word_search + len(find_me_word)
        word_search_2 = text.find(find_me_word, new_start)
        if word_search_2 == -1:
            return "The word '" + find_me_word + "' appears only once in your text"
        else:
            return "On this position your word appears at the second time: " + str(word_search_2)
    else:
        return "The word '" + find_me_word + "' doesn't appear in your text at all"


'''Введите строку и посчитайте в ней количество уникальных символов,
если их больше 10 - выведите True, если менее 10 - выведите False        homework_6_1'''

def count_unic_symbols(users_string):
    amount_unic_symbols = len(set(users_string))
    if amount_unic_symbols >= 10:
        return True
    else:
        return False


'''      Функция ищет есть ли в строке буква "h"    homework_6_2   '''

def find_h_letter(users_word):
    lower_h = users_word.lower()
    if 'h' in lower_h:
        return True
    else:
        return False


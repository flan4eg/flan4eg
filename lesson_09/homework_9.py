import unittest

from my_functions import find_substring, capital_letter_word, word_of_interest, count_unic_symbols

class MyTest(unittest.TestCase):

    def test_find_substring_positive(self):  # функция успешно находит сабстринг
        str1 = "little white mouse"
        str2 = "white"
        expected_result = 7
        self.assertEqual(find_substring(str1, str2), expected_result)

    def test_find_substring_negative(self):  # такого сабстринга нет
        str1 = "apple"
        str2 = "plum"
        expected_result = -1
        self.assertEqual(find_substring(str1, str2), expected_result)

    def test_capital_letter_word_positive(self):  # функция находит слова с Заглавными буквами
        my_list = ["Cat", "dog", "Bird", "Fish"]
        expected_result = 3
        self.assertEqual(capital_letter_word(my_list), expected_result)

    def test_capital_letter_word_negative(self):  # функция получает int вместо str, ожидаем TypeError
        not_word = 13
        with self.assertRaises(TypeError):
            capital_letter_word(not_word)

    def test_word_of_interest_positive_word_found_two_times(self):  # слово в тексте находится дважды
        my_text = "Tom and Jerry Tom"
        expected_result = "On this position your word appears at the second time: 14"
        self.assertEqual(word_of_interest(my_text, "Tom"), expected_result)

    def test_word_of_interest_positive_word_found_once(self):  # слово встречается в тексте один раз
        my_text = "Tom and Jerry"
        expected_message = "The word 'Tom' appears only once in your text"
        self.assertEqual(word_of_interest(my_text, "Tom"), expected_message)

    def test_word_of_interest_negative_word_not_found(self):  # слово не встречается в тексте
        my_text = "I see black cat"
        expected_message = "The word 'Tom' doesn't appear in your text at all"
        self.assertEqual(word_of_interest(my_text, "Tom"), expected_message)

    def test_count_unic_symbols_positive(self):  # больше 10 уникальных символов возвращает True
        my_string = "qwertyuiopasdfghjkl"
        self.assertTrue(count_unic_symbols(my_string))

    def test_count_unic_symbols_negative(self):  # менее 10 уникальных символов возвращает False
        my_string = "qwerty"
        self.assertFalse(count_unic_symbols(my_string))

    def test_count_unic_symbols_negative_empty_string(self):  # пустая строка возвращает False
        my_string = ""
        self.assertFalse(count_unic_symbols(my_string))



if __name__ == '__main__':
    unittest.main()
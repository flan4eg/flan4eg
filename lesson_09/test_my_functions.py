import pytest
from .my_functions import capital_letter_word, word_of_interest, count_unic_symbols, find_h_letter


def test_capital_letter_word_positive():
    my_list = ["Cat", "dog", "Bird", "Fish", "apple"]
    assert capital_letter_word(my_list) == 3

def test_capital_letter_word_negative_type_error():
    not_word = 13
    with pytest.raises(TypeError):
        capital_letter_word(not_word)

def test_capital_letter_word_negative_empty_list():
   assert capital_letter_word([]) == 0


def test_word_of_interest_positive_word_found_two_times():
    my_text = "Tom and Jerry Tom"
    expected_result = "On this position your word appears at the second time: 14"
    assert word_of_interest(my_text, "Tom") == expected_result

def test_word_of_interest_positive_word_found_once():
    my_text = "Tom and Jerry"
    expected_message = "The word 'Tom' appears only once in your text"
    assert word_of_interest(my_text, "Tom") == expected_message

def test_word_of_interest_negative_word_not_found():
    my_text = "I see black cat"
    expected_message = "The word 'Tom' doesn't appear in your text at all"
    assert word_of_interest(my_text, "Tom") == expected_message


def test_count_unic_symbols_positive():
    my_string = "qwertyuiopasdfg"
    assert count_unic_symbols(my_string) is True

def test_count_unic_symbols_negative():
    my_string = "qwerty"
    assert count_unic_symbols(my_string) is False

def test_count_unic_symbols_negative_duplicate():
    my_string = "aaaaabbbbbccccc"
    assert count_unic_symbols(my_string) is False

def test_count_unic_symbols_negative_empty_string():
    my_string = ""
    assert count_unic_symbols(my_string) is False


def test_find_h_letter_positive_lower():
    assert find_h_letter("hello") is True

def test_find_h_letter_positive_upper():
    assert find_h_letter("Horse") is True

def test_find_h_letter_negative():
    assert find_h_letter("apple") is False
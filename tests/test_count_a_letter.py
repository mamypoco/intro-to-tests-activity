from main import count_a_letter
import pytest

def test_demo_one():
    num_1 = 8
    num_2 = 9

    result = num_1 + num_2

    assert result == 17

def test_demo_two():
    num_1 = 18
    num_2 = 24

    result = num_1 + num_2

    assert result == 42
# Delete the demo tests and add your tests here 

def test_count_a_letter_in_sentence():
#arrange
    sentence = "Hello"
    letter = "l"
#act
    result = count_a_letter(sentence, letter) 
#assert
    assert result == 2


def test_count_a_letter_empty():
#arrange
    sentence = "world"
    letter = ""
#act
    result = count_a_letter(sentence, letter) 
#assert
    assert result == None


def test_count_a_letter_number():
#arrange
    sentence = "kindergarten"
    letter = "3"
#act
    result = count_a_letter(sentence, letter) 
#assert
    assert result is None

def test_count_a_letter_number_int():
#arrange
    sentence = "kindergarten"
    letter = 3
#act
    result = count_a_letter(sentence, letter) 
#assert
    assert result == "Please enter letter, not integer"

# Edge cases:
# - if we have empty word, input from user
# - if we have number instead of letter
# - "p" in "Hello" -> None
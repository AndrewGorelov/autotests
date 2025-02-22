import pytest

from src.simple_tests.FizzBuzz import fizz_buzz


def test_fizzbuzz():
    result = fizz_buzz(3)
    assert result == "Fizz"


def test_buzz():
    result = fizz_buzz(5)
    assert result == "Buzz"


def test_fizzbuzz_1():
    result = fizz_buzz(15)
    assert result == "FizzBuzz"


@pytest.mark.parametrize(
    ("number", "expected_result"), [(3, "Fizz"), (5, "Buzz"), (15, "FizzBuzz"), (4, 4)]
)
def test_fizzbuzz_withparams(number, expected_result):
    result = fizz_buzz(number)
    assert result == expected_result


@pytest.mark.parametrize(("number"), [0, -10, 101])
def test_fizzbuzz_invalid_number(number):
    with pytest.raises(ValueError):
        fizz_buzz(number)


from src.simple_tests.search_max import search_max


def test_search_max_1():
    x = search_max("0 5 15 90 3")
    assert x == 90

import pytest
from string_utils import StringUtils

stringUtils = StringUtils()

@pytest.mark.parametrize("string, result", [
    ("skypro", "Skypro"),
    ("the sky is blue", "The sky is blue"),
    ("1 января", "1 января"),
    ("", ""),
    (" ", " ")
])
def test_capitilize(string, result):
    assert stringUtils.capitilize(string) == result


@pytest.mark.parametrize("string, result", [
    (" skypro", "skypro"),
    (" the sky is blue", "the sky is blue"),
    ("    skypro", "skypro"),
    ("", ""),
    ("skypro ", "skypro ")
])
def test_trim(string, result):
    assert stringUtils.trim(string) == result
     

@pytest.mark.parametrize("string, delimeter, result", [
    ("Иван,Мария,Михаил,Ольга", ",", ["Иван", "Мария", "Михаил", "Ольга"]),
    ("Иван;Мария;Михаил;Ольга", ";", ["Иван", "Мария", "Михаил", "Ольга"]),
    ("Иван,Мария,Михаил,Ольга", None, ["Иван", "Мария", "Михаил", "Ольга"]),
    ("1:2:3:4:5", ":", ["1", "2", "3", "4", "5"]),
    ("a b c d", " ", ["a", "b", "c", "d"])
])
def test_to_list(string, delimeter, result):
    if delimeter is None:
        res = stringUtils.to_list(string)
    else:
        res = stringUtils.to_list(string, delimeter)
    assert res == result


@pytest.mark.parametrize("string, symbol, result", [
    ("Skypro", "S", True),
    ("Скайпро", "С", True),
    ("%%%!!!*", "%", True),
    ("12345", "2", True),
    (" ", " ", True),
    ("", "", True),
    ("Skypro", "j", False),
    ("SkyPro", "p", False),
    ("12345", "a", False), 
    ("1+2", "-", False)
])
def test_contains(string, symbol, result):
    res = stringUtils.contains(string, symbol)
    assert res == result
    

@pytest.mark.parametrize("string, symbol, result", [
    ("SkyProm", "m", "SkyPro"),
    ("День", "ь", "Ден"),
    ("12345", "4", "1235"),
    ("Hi!!!", "!", "Hi"),
    ("абв гд", " ", "абвгд"),
    ("ночь", "Н", "ночь"),
    ("morning", "v", "morning"),
    ("%###*&", " ", "%###*&"),
    ("AAA", "A", "")

])
def test_delete_symbol(string, symbol, result):
    res = stringUtils.delete_symbol(string, symbol)
    assert res == result
    

@pytest.mark.parametrize("string, symbol, result", [
    ("Skypro", "S", True),
    ("Скайпро", "С", True),
    ("%%%!!!*", "%", True),
    ("12345", "1", True),
    (" ", " ", True),
    ("", "", True),
    ("Skypro", "j", False),
    ("SkyPro", "s", False),
    ("12345", "a", False), 
    ("1+2", "-", False)
])
def test_starts_with(string, symbol, result):
    res = stringUtils.starts_with(string, symbol)
    assert res == result
    

@pytest.mark.parametrize("string, symbol, result", [
    ("Skypro", "o", True),
    ("Скайпро", "о", True),
    ("%%%!!!*", "*", True),
    ("12345", "5", True),
    (" ", " ", True),
    ("", "", True),
    ("Skypro", "O", False),
    ("SkyPro", "s", False),
    ("12345", "2", False), 
    ("1+2", "+", False)
])
def test_end_with(string, symbol, result):
    res = stringUtils.end_with(string, symbol)
    assert res == result
    

@pytest.mark.parametrize("string, result", [
    ("", True),
    (" ", True),
    ("     ", True),
    ("SkyPro", False),
    ("СкайПро", False),
    ("12345", False),
    ("    a", False),
    ("x     ", False),
    ("@%!$#.", False)
])
def test_is_empty(string, result):
    res = stringUtils.is_empty(string)
    assert res == result
    

@pytest.mark.parametrize("list, joiner, result", [
    ([1,2,3,4,5], None, "1, 2, 3, 4, 5"),
    (["Sky", "Pro"], ",", "Sky,Pro"),
    (["Sky", "Pro"], "-", "Sky-Pro"),
    (["Sky", "Pro"], "", "SkyPro"),
    (["Скай", "Про"], "+", "Скай+Про"),
    ([], None, ""),
    ([], ",", "")
])
def test_list_to_string(list, joiner, result):
    if joiner == None:
        res = stringUtils.list_to_string(list)
    else:
        res = stringUtils.list_to_string(list, joiner)
        assert res == result
        
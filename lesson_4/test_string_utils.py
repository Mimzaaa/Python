import pytest
from string_utils import StringUtils

letter = StringUtils()

def test_capitalize():
    """+"""
    assert letter.capitilize("august") == "August"
    assert letter.capitilize("stray kids") == "Stray kids"
    assert letter.capitilize("привет!") == "Привет!"
    assert letter.capitilize("запах505") == "Запах505"
    assert letter.capitilize("August") == "August"
    """-"""
    assert letter.capitilize("") == ""
    assert letter.capitilize(" ") == " "
    assert letter.capitilize("01234") == "01234"
    assert letter.capitilize("!!!!@$") =="!!!!@$"


def test_trim():
    """+"""
    assert letter.trim(" august") == "august"
    assert letter.trim("  stray kids") == "stray kids"
    assert letter.trim(" Пока! ") == "Пока! "
    """-"""
    assert letter.trim("") == ""
    assert letter.trim(" ") == ""


def test_to_list():
        """+"""
        assert letter.to_list("сентябрь,октябрь,ноябрь", ",") == ["сентябрь", "октябрь", "ноябрь"]
        assert letter.to_list("1,2,3,4", ",") == ["1", "2", "3", "4"]
        """-"""
        assert letter.to_list("", None,) == []
        assert letter.to_list("1 2 3", None,) == ["1", "2", "3"]


def test_contains():
    assert letter.contains("August", "A") == True
    assert letter.contains("August", "1") == False
    assert letter.contains("5778", "8") == True
    assert letter.contains("152/6783", "/") == True
    assert letter.contains("", "") == True
    assert letter.contains("Blue", "b") == False
    assert letter.contains("Purple", "E") == False


def test_delete_symbol():
    assert letter.delete_symbol("Pencil", "P") == "encil"
    assert letter.delete_symbol("Calculator", "u") == "Calclator"
    assert letter.delete_symbol("Red", "d") == "Re"
    assert letter.delete_symbol("StrayKids", "Kids") == "Stray"
    assert letter.delete_symbol("Kazan-Ivanovo", "-") == "KazanIvanovo"
    assert letter.delete_symbol("5673", "6") == "573"
    assert letter.delete_symbol("5678", "0") == "5678"
    assert letter.delete_symbol("ice cream", " ") == "icecream"
    assert letter.delete_symbol("", "0") == ""
    assert letter.delete_symbol("del", " ") == "del"


def test_starts_with():
    assert letter.starts_with("August", "A") == True
    assert letter.starts_with("November", "A") == False
    assert letter.starts_with(" puls", " ") == True
    assert letter.starts_with("!lost", "!") == True
    assert letter.starts_with("3456789", "3") == True
    assert letter.starts_with("5757", "7") == False
    assert letter.starts_with("", " ") == False
    assert letter.starts_with("", "") == True

def test_end_with():
    assert letter.end_with("Snow", "w") == True
    assert letter.end_with("snoW", "W") == True
    assert letter.end_with("global", "L") == False
    assert letter.end_with("CAT", "t") == False
    assert letter.end_with("23456789", "9") == True
    assert letter.end_with("4568", "4") == False
    assert letter.end_with("hello!", "!",) == True
    assert letter.end_with("hi ", " ") == True
    assert letter.end_with("", "") ==True
    assert letter.end_with("", " ") == False

def test_is_empty():
    assert letter.is_empty("") == True
    assert letter.is_empty(" ") == True
    assert letter.is_empty("!") == False
    assert letter.is_empty("Hi") == False
    assert letter.is_empty("123") == False

def test_list_to_string():
    assert letter.list_to_string([1, 2, 3]) == "1, 2, 3"
    assert letter.list_to_string(["hi", "hello", "world"]) == "hi, hello, world"
    assert letter.list_to_string(["hi", "hello", "world"], ":") == "hi:hello:world"
    assert letter.list_to_string(["mi,", "ma,", "mo"], ",") == "mi,,ma,,mo"
    
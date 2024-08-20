import pytest
from string_utils import StringUtils

letter = StringUtils()
space = StringUtils()
make = StringUtils()
capital = StringUtils()
dell = StringUtils()
go = StringUtils()
line = StringUtils()
convert = StringUtils()


def letter_capitalize():
    """+"""
    assert letter.capitilize("august") == "August"
    assert letter.capitilize("stray kids") == "Stray kids"
    assert letter.capitilize("привет!") == "Привет!"
    assert letter.capitilize("запах505") == "Запах505"
    assert letter.capitilize("August") == "August"
    """-"""
    assert letter.capitilize("") == ""
    assert letter.capitilize(None) == None
    assert letter.capitilize(" ") == " "
    assert letter.capitilize("01234") == "01234"
    assert letter.capitilize("!!!!@$") =="!!!!@$"


def space_trim():
    """+"""
    assert space.trim(" august") == "august"
    assert space.trim("  stray kids") == "stray kids"
    assert space.trim(" Пока! ") == "Пока! "
    """-"""
    assert space.trim("") == ""
    assert space.trim(" ") == ""


def to_list():
        """+"""
        assert make.to_list("сентябрь,октябрь,ноябрь", ",",) == ["сентябрь", "октябрь", "ноябрь"]
        assert make.to_list("0 2 5 7 9", ",",) == ["0", "2", "5", "7", "9"]
        assert make.to_list("1:2:3:4", ",",) == ["1", "2", "3", "4"]
        """-"""
        assert make.to_list("декабрь,январ,февраль", None,) == ["декабрь", "январь", "февраль"]
        assert make.to_list("1 2 3", None,) == ["1 2 3"]


def contains():
    assert capital.contains("August", "A") == True
    assert capital.contains("August", "1") == False
    assert capital.contains("5778", "8") == True
    assert capital.contains("152/6783", "/") == True
    assert capital.contains("", "") == True
    assert capital.contains("Blue", "b") == False
    assert capital.contains("Purple", "E") == False


def delete_symbol():
    assert dell.delete_symbol("Pencil", "P") == "encil"
    assert dell.delete_symbol("Calculator", "u") == "Calclator"
    assert dell.delete_symbol("Red", "d") == "Re"
    assert dell.delete_symbol("StrayKids", "Kids") == "Stray"
    assert dell.delete_symbol("Kazan-Ivanovo", "-") == "KazanIvanovo"
    assert dell.delete_symbol("5673", "6") == "573"
    assert dell.delete_symbol("5678", "0") == "5678"
    assert dell.delete_symbol("ice cream", " ") == "icecream"
    assert dell.delete_symbol("", "0") == ""
    assert dell.delete_symbol("del", " ") == "del"


def starts_with():
    assert go.starts_with("August", "A") == True
    assert go.starts_with("November", "A") == False
    assert go.starts_with(" puls", " ") == True
    assert go.starts_with("!lost", "!") == True
    assert go.starts_with("3456789", "3") == True
    assert go.starts_with("5757", "7") == False
    assert go.starts_with("", " ") == False
    assert go.starts_with("", "") == True

def end_with():
    assert go.end_with("Snow", "w") == True
    assert go.end_with("snoW", "W") == True
    assert go.end_with("global", "L") == False
    assert go.end_with("CAT", "t") == False
    assert go.end_with("23456789", "9") == True
    assert go.end_with("4568", "4") == False
    assert go.end_with("hello!", "!",) == True
    assert go.end_with("hi ", " ") == True
    assert go.end_with("", "") ==True
    assert go.end_with("", " ") == False

def is_empty():
    assert line.is_empty("") == True
    assert line.is_empty(" ") == True
    assert line.is_empty("!") == False
    assert line.is_empty("Hi") == False
    assert line.is_empty("123") == False

def list_to_string():
    assert convert.list_to_string([1, 2, 3]) == "1, 2, 3"
    assert convert.list_to_string(["hi", "hello", "world"]) == "hi, hello, world"
    assert convert.list_to_string(["hi", "hello", "world"], ":") == "hi:hello:world"
    assert convert.list_to_string(["mi,", "ma,", "mo"], ",") == "mi,,ma,,mo"
    
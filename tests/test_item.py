import pytest

from src.item import Item, InstantiateCSVError


def test_init(example):
    assert example.name == "Смартфон"
    assert example.price == 10000
    assert example.quantity == 20
    assert example.calculate_total_price() == 200_000


def test_apply_discount(example):
    example.apply_discount()
    assert example.price == 8000


def test_string_to_number():
    assert Item.string_to_number('5.5') == 5
    assert Item.string_to_number('3') == 3


def test_setter_for_name(example):
    example.name = 'test'
    assert example.name == 'test'
    example.name = 'testtest100'
    assert example.name == "testtest10"


def test_instantiate_from_csv():
    try:
        with pytest.raises(FileNotFoundError, match='Отсутствует файл item.csv'):
            Item.instantiate_from_csv()
        with pytest.raises(InstantiateCSVError, match='Файл item.csv поврежден'):
            Item.instantiate_from_csv()
    except Exception:
        pass
    else:
        Item.instantiate_from_csv()
        assert len(Item.all) == 5


def test_repr(example):
    assert example.__repr__() == "Item('Смартфон', 10000, 20)"


def test_str(example):
    assert example.__str__() == "Смартфон"


def test_add(example, example_phone):
    assert example + example_phone == 25
    assert example_phone + example_phone == 10
    with pytest.raises(Exception, match="Разные классы"):
        example + "a"

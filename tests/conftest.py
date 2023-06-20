import pytest
from src.item import Item


@pytest.fixture
def example():
    Item.pay_rate = 0.8
    return Item("Смартфон", 10000, 20)
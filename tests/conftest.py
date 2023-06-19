import pytest
from src.item import Item


@pytest.fixture
def example():
    return Item("Смартфон", 10000, 20)
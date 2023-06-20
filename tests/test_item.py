"""Здесь надо написать тесты с использованием pytest для модуля item."""


def test_item_class(example):
    assert example.name == "Смартфон"
    assert example.price == 10000
    assert example.quantity == 20
    assert example.calculate_total_price() == 200_000
    example.apply_discount()
    assert example.price == 8000

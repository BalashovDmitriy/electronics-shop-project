from src.item import Item


def test_item_class(example):
    assert example.name == "Смартфон"
    assert example.price == 10000
    assert example.quantity == 20
    assert example.calculate_total_price() == 200_000
    example.apply_discount()
    assert example.price == 8000
    assert Item.string_to_number('5.5') == 5
    assert Item.string_to_number('3') == 3
    example.name = 'test'
    assert example.name == 'test'
    example.name = 'testtest100'
    assert example.name == "testtest10"
    Item.instantiate_from_csv()
    assert len(Item.all) == 5

def test_phone_init(example_phone):
    assert example_phone.name == 'iPhone 14'
    assert example_phone.price == 120_000
    assert example_phone.quantity == 5
    assert example_phone.number_of_sim == 2


def test_phone_str(example_phone):
    assert str(example_phone) == 'iPhone 14'


def test_phone_repr(example_phone):
    assert repr(example_phone) == "Phone('iPhone 14', 120000, 5, 2)"


def test_phone_number_of_sim_setter(example_phone):
    example_phone.number_of_sim = 1
    assert example_phone.number_of_sim == 1

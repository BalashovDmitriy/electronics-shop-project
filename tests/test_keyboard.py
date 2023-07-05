def test_keyboard_init(example_keyboard):
    assert str(example_keyboard) == "Dark Project KD87A"
    assert str(example_keyboard.language) == "EN"


def test_change_lang(example_keyboard):
    example_keyboard.change_lang()
    assert str(example_keyboard.language) == "RU"
    example_keyboard.change_lang()
    assert str(example_keyboard.language) == "EN"


def text_mixin(example_keyboard):
    example_keyboard.change_lang().change_lang()
    assert str(example_keyboard.language) == "EN"

from src.item import Item


class Mixin:

    def change_lang(self):
        if self._language == 'EN':
            self._language = 'RU'
        else:
            self._language = 'EN'
        return self


class KeyBoard(Item, Mixin):

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self._language = 'EN'

    @property
    def language(self):
        return self._language

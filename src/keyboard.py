from src.item import Item


class Mixin:

    def change_lang(self):
        if self.language == 'EN':
            self.language = 'RU'
        else:
            self.language = 'EN'
        return self


class KeyBoard(Item, Mixin):

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self.language = 'EN'

    @property
    def language(self):
        return self.language

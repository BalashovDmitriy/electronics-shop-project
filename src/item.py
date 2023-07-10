import csv
import os


class InstantiateCSVError(Exception):

    def __init__(self, message):
        print(message)


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        super().__init__()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) > 10:
            new_name = new_name[:10]
        self.__name = new_name

    @classmethod
    def instantiate_from_csv(cls):
        file = "../src/items.csv"
        if not os.path.exists(file):
            raise FileNotFoundError('Отсутствует файл item.csv')
        with open(file, encoding='CP1251') as file:
            dict_ = csv.DictReader(file, delimiter=",")
            for row in dict_:
                if len(row) < 3:
                    raise InstantiateCSVError('Файл item.csv поврежден')
                Item.all.append(Item(row['name'], Item.string_to_number(row['price']),
                                     Item.string_to_number(row['quantity'])))

    @staticmethod
    def string_to_number(str_):
        return int(float(str_))

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        raise Exception('Разные классы')

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        return self.__name

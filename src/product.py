from src.base_poduct import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    """ Класс «Продукты» """
    name: str
    description: str
    price: float
    quantity: int
    color: str

    def __init__(self, name, description, price, quantity, color=None):
        self.name = name
        self.description = description
        self.__price = price
        if quantity >= 0:
            self.quantity = quantity
        else:
            raise ValueError('Товар с нулевым количеством не может быть добавлен')
        self.color = color
        super().__init__()

    def __str__(self):
        """ Выводит строку формата Название продукта, __ руб. Остаток: __ шт."""
        return f'{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        """ Полная стоимость всех товаров на складе """
        if type(other) is Product:
            return (self.price * self.quantity) + (other.price * other.quantity)
        raise TypeError

    @classmethod
    def new_product(cls, data: dict):
        """ Распаковываем словарь и передаем его параметры в класс """
        try:
            return cls(**data)
        except Exception as e:
            return {e}

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        """ Проверка что цена выше нуля и не равна нулю """
        if new_price <= 0:
            print('Цена не должна быть нулевая или отрицательная')
        else:
            self.__price = new_price


if __name__ == "__main__":
    product = Product('apple', 'fruit', 5, 6)
    product3 = Product('apple', 'fruit', 5, 10)
    #
    # print(product.name)
    # print(product.description)
    # print(product.price)
    # print(product.quantity)
    # print(product.color)

    my_dict = {"name": "carrot", "description": "vegetable", "price": 4, "quantity": 15}
    product2 = Product.new_product(my_dict)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)
    print(product2.color)

    # product2.price = 0
    # print(product2.price)

    print(product + product3)
    print(product, product3)

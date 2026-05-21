class Product:
    """ Класс «Продукты» """
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f'{self.name}, {self.__price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        return (self.price * self.quantity) + (other.price * other.quantity)

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

    my_dict = {"name": "carrot", "description": "vegetable", "price": 4, "quantity": 15}
    product2 = Product.new_product(my_dict)

    # print(product2.name)
    # print(product2.description)
    # print(product2.price)
    # print(product2.quantity)
    #
    # product2.price = 0
    # print(product2.price)

    print(product,product3)

from src.product import Product


class Smartphone(Product):
    """ Котегория товаров, класс Смартфоны """

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity, color)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory

    def __add__(self, other):
        """ Полная стоимость категории Смартфоны """
        if isinstance(other, Smartphone):
            return (self.price * self.quantity) + (other.price * other.quantity)
        raise TypeError


class LawnGrass(Product):
    """ Категория товаров класс Трава газонная """

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity, color)
        self.country = country
        self.germination_period = germination_period

    def __add__(self, other):
        """ Полная стоимость категории Трава газонная """
        if isinstance(other, LawnGrass):
            return (self.price * self.quantity) + (other.price * other.quantity)
        raise TypeError


if __name__ == '__main__':
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 10, 2, 98.2, "15", 512, "Gray space")
    smartphone3 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 10, 3, 90.3, "Note 11", 1024, "Синий")
    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 10, 4, "Россия", "7 дней", "Зеленый")
    grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 10, 5, "США", "5 дней", "Темно-зеленый")

    print(smartphone2 + smartphone3)
    print(grass1 + grass2)
    print(smartphone2 + grass1)

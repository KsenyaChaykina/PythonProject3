from src.product import Product


class Category:
    """ Класс «Категории» """
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def add_product(self, product: Product):
        if issubclass(product.__class__, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    def __str__(self):
        total_products = 0
        for product in self.__products:
            total_products += product.quantity
        return f'{self.name}, количество продуктов: {total_products}'

    @property
    def products(self):
        """ Выводит список товаров в виде строк """
        products_str = ''
        for product in self.__products:
            products_str += f'{str(product)}\n'
        return products_str

    @products.setter
    def products(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1


if __name__ == "__main__":
    product1 = Product('apple', 'fruit', 15, 60)
    product2 = Product('tomato', 'vegetable', 10, 10)
    product3 = Product('candies', "sweets", 13, 20)

    category = Category('food', 'vegetable', [product1, product2, product3])
    category2 = Category('food', 'vegetable', [product1, product2])

    # print(category.name)
    # print(category.description)
    # print(category.products)
    #
    # print(category.category_count)
    # print(Category.product_count)

    product4 = Product('candies', "sweets", 10, 15)
    # category.products = product4

    # print(category.products)
    # print(Category.product_count)

    print(category, category2)

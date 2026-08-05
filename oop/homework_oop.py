class Product:

    def __init__(self, name: str, id_number: int, price: float, category: str, in_stock: int ):
        self.name = name
        self.id_number = id_number
        self.price = price
        self.category = category
        self.in_stock = in_stock

    def change_price(self, new_price: float):
        self.price = new_price

    def quantity_in_stock(self, quantity: int):
        self.in_stock = quantity

    def __str__(self):
        return f"Name: {self.name}, ID number: {self.id_number}, price: {self.price}₴, in_stock: {self.in_stock}."


class Customer:

    def __init__(self, name: str, email: str, id_number: int):
        self.name = name
        self.email = email
        self.id_number = id_number
        self.order_list = []

    def new_order(self, new_order: list):
        self.order_list.append(new_order)

    def __str__(self):
        return f"Name: {self.name}, email: {self.email}, ID number: {self.id_number}"

class Order:

    def __init__(self):
         self.list_of_products = []
         self.total_price = 0

    def add_product(self, product: Product):
         self.list_of_products.append(product)
         self.calc_total_price()

    def calc_total_price(self):
        total_price = 0
        for product in self.list_of_products:
            total_price += product.price
        self.total_price = total_price
        return self.total_price

products = []

with open("list_of_products.txt", "r") as file:
    for line in file:
        name, id_number, price, category, in_stock = line.strip().split(",")
        product = Product(name, int(id_number), float(price), category, int(in_stock))
        products.append(product)


customers = []

with open("customers.txt", "r") as file:
    for line in file:
        name, email, id_number = line.strip().split(",")
        customer = Customer(name, email, int(id_number))
        customers.append(customer)

class Store:

    def __init__(self, products: list, customers: list):
        self.products = products
        self.customers = customers

    def add_product(self, product: Product):
        for prod in self.products:
            if product.id_number == prod.id_number:
                print("The product already exists!")
                return
        self.products.append(product)
        with open("list_of_products.txt", "a") as file:
            file.write(f"{product.name},{product.id_number},{product.price},{product.category},{product.in_stock}\n")

    def add_customer(self, customer: Customer):
        for cust in self.customers:
            if customer.id_number == cust.id_number:
                print("Customer already added!")
                return
        self.customers.append(customer)
        with open("customers.txt", "a") as file:
            file.write(f"{customer.name},{customer.email},{customer.id_number}\n")
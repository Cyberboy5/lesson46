
class Product:
    def __init__(self,name,price,quantity) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def get_product_info(self) -> str:
        return f"""

    Name:{self.name}
    Price:{self.price}
    Quantity:{self.quantity}"""

    def update_quantity(self, quantity: int) -> None:
        self.quantity = quantity
    
    def apply_discount(self, percentage: int) -> None:
        self.price -= self.price * (percentage /100)
        return self.price

    def calculate_total_value(self) -> float:
        return self.price * self.quantity
    

class Telefon(Product):
    def __init__(self, name, price, quantity,brand,model) -> None:
        super().__init__(name, price, quantity)
        self.brand = brand
        self.model = model

    def get_product_info(self) -> str:
        return f"""{super().get_product_info()}

    BAuthor{self.brand}
    Model:{self.model}"""


class Laptop(Product):
    def __init__(self, name, price, quantity,brand,processor) -> None:
        super().__init__(name, price, quantity)
        self.brand = brand
        self.processor = processor

    def get_user_info(self) -> str:
        return f"""{super().get_product_info()}

    Brand:{self.brand}
    Processor:{self.processor}"""


class Book(Product):
    def __init__(self, name, price, quantity,author,genre) -> None:
        super().__init__(name, price, quantity)
        self.author = author
        self.genre = genre

    def get_user_info(self) -> str:
        return f"""{super().get_product_info()}

    Author:{self.author}
    Genre:{self.genre}"""


class User:
    def __init__(self,name,user_id) -> None:
        self.name = name
        self.user_id = user_id
        self.cart = []

    def get_user_info(self):
        return f"""
    Name:{self.name}
    User_ID:{self.user_id}
    Cart:{self.cart}"""

    def add_to_cart(self, product: Product) -> None:
        self.cart.append(product)

    def view_cart(self) -> str:
        data = ''
        for product in self.cart:
            data += product.get_user_info()
        return data
    

class Onlayn_dokon_tizimi:
    def __init__(self) -> None:
        self.products = []
        self.users = []

    def add_product(self, product: Product) -> None:
        self.products.append(product)

    def add_user(self, user: User) -> None:
        self.users.append(user)

    def view_products(self) -> str:
        data = ''
        for product in self.products:
            data += product.get_user_info()
        return data

    def view_user_cart(self, user_id: str) -> str:
        data = ''   
        for user in self.users:
            if user.user_id == user_id:
                data += user.get_user_info()
        return data
    


phone = Laptop("HP",999.99,10,"Apple","12")
book = Book("Uluq Gatsby",15.99,5,"F. Scott Fitzgerald","Klassika")

user = User(name="Alice", user_id="F001")

shopping_system = Onlayn_dokon_tizimi()
shopping_system.add_product(phone)
shopping_system.add_product(book)

shopping_system.add_user(user)

user.add_to_cart(phone)
user.add_to_cart(book)

print(phone.apply_discount(10))
print(book.apply_discount(20))

# print(user.view_cart())
# print(shopping_system.view_products())





    
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def display_info(self):
        print(f"portals parfums: {self.name}")
        print(f"250: {self.price} USD")
        print(f"20: {self.quantity}")
        print(f"250: {self.calculate_total_price()} USD")


class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def get_salary_info(self):
        return f"Заробітня плата {self.name}: {self.salary} грн."

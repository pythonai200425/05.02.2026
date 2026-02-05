# from typing import override  # python 3.12 +
from typing_extensions import override  # python 3.10

from datetime import datetime

class Car:
    def __init__(self, brand, model, price, color):
        self.brand = brand
        self.model = model
        self.price = price
        self.color = color

    @override
    def __str__(self):
        #return datetime.now().strftime("%H:%M:%S")
        return f"[Car] brand: {self.brand}, model: {self.model}, price: {self.price}, color: {self.color}"


ferrari = Car('ferrari', 'testa rosa', 500_000, 'red')

lamburgini = Car('lamgurgini', 'Revuelto', 600_000, 'white')

print(ferrari)
print(lamburgini)

# class bank-account
#     f_name, l_name, bank_name, balance
#     __str__, __init__
#    create 2 bank accounts and print them

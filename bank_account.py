
class BankAccount:
    def __init__(self, f_name, l_name, bank_name, balance):
        self.f_name = f_name
        self.l_name = l_name
        self.bank_name = bank_name
        self.balance = balance
        self.deposit(100)

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            print(f'Withdrawn {amount} , left in balance {self.balance}')
        else:
            print(f'Insufficient balance. cannot withdraw {amount:,} from {self.f_name}')

    def deposit(self, amount):
        self.balance += amount
        print(f'Deposit {amount} for {self.f_name}, now balance= {self.balance:,}')

    def __str__(self):
        return f"[BankAccount] first name: {self.f_name}, last name: {self.l_name}, bank name: {self.bank_name}, balance: {self.balance}"

asif = BankAccount("Asif", "Moshe", "discont", 300_000)
angela = BankAccount("Angela", "Brook", "mizrahi", 20_000)

print(asif)
print(angela)

# angela.balance += 10_000  # USUALLY DONT
angela.deposit(100)
angela.withdraw(30_000)

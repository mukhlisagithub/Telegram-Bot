# Masala: BankAccount nomli class yaratib, account_number, balance, data_of_opening va customer_name atributlar, deposit, withdraw,
# check_balance, kabi metodlarni qoshing
#          5 ta object yarating;
#          har bir dastlabki attributlarni konstructor yordamida toldiring;
#          Mijozni bank malumotlarini chiqarish funksiyasini chaqiring;
#          Balansni deposit orqali toldiring;
#          Balansni holatini tekshiring
#          Malum bir miqdorda pul yeching


from faker import Faker
fake = Faker()

class BankAccount:
    def __init__(self, name, acc_number, balance, doo):
        self.customer_name = name
        self.account_number = acc_number
        self.balance = balance
        self.date_of_opening = doo

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def check_balance(self):
        return f"Balance: ${self.balance}"

    def printInfo(self):
        return f'Name: {self.customer_name}, AN: {self.account_number}, Balance: ${self.balance}, DoO: {self.date_of_opening}'

if __name__ == "__main__":
    f = Faker()
    accounts = []
    print(dir(fake))  # dir => berilgan ozgaruvchi yoki obyektni barcha attribut va parameterlarinikorish mumkin
    for i in range(5):
        # name, number, balance, date = input().split()  => faker siz varianti
        accounts.append(BankAccount(f.first_name(), f.ssn(), f.random_number(), f.date() ))
        print(accounts[i].printInfo())
        # accounts.append(BankAccount())
    name = input("Name: ")
    person = None
    for i in range(5):
        if accounts[i].customer_name == name:
            person = accounts[i]
            break
    print(person.printInfo())
    person.deposit(int(input('Deposit: ')))
    print(person.check_balance())
    person.withdraw(int(input('Amount to Withdraw: ')))
    print(person.check_balance())
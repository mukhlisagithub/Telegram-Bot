# Masala: BankAccount nomli class yaratib, account_number, balance, data_of_opening va customer_name atributlar, deposit, withdraw,
# check_balance, kabi metodlarni qoshing
#          5 ta object yarating;
#          har bir dastlabki attributlarni konstructor yordamida toldiring;
#          Mijozni bank malumotlarini chiqarish funksiyasini chaqiring;
#          Balansni deposit orqali toldiring;
#          Balansni holatini tekshiring
#          Malum bir miqdorda pul yeching


class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Mablag' yetarli emas!")

    def check_balance(self):
        print("Current Balance:", self.balance)


obj1 = BankAccount('1111111', 500, '2020.01.01', 'Ali Valiyev')
obj2 = BankAccount('2222222', 1000,'2020.02.02', 'Hasan Hasanov')
obj3 = BankAccount('3333333', 2000, '2020.03.03', 'Husan Husanov')
obj4 = BankAccount('4444444', 3000, '2020.04.04', 'Akrom Aliyev')
obj5 = BankAccount('5555555', 5000, '2020.05.05', 'Vali Aliyev')
# print(obj4.account_number)


# Mijozni bank malumotlarini chiqarish funksiyasini chaqiring;
def customer_info(account):
    print("account number: ", account.account_number)
    print("balance: ", account.balance)
    print("date_of_opening: ", account.date_of_opening)
    print("customer_name: ", account.customer_name)
    print()

customer_info(obj1)
customer_info(obj2)
customer_info(obj3)
customer_info(obj4)
customer_info(obj5)



# Balansni deposit orqali toldiring;
obj1.deposit(500)
obj2.deposit(1000)
obj3.deposit(2000)
obj4.deposit(3000)
obj5.deposit(5000)



# Balansni holatini tekshiring
obj1.check_balance()
obj2.check_balance()
obj3.check_balance()
obj4.check_balance()
obj5.check_balance()




# Malum bir miqdorda pul yeching
obj1.withdraw(100)
obj2.withdraw(200)
obj3.withdraw(300)
obj4.withdraw(400)
obj5.withdraw(500)




# Balansni holatini tekshiring
obj1.check_balance()
obj2.check_balance()
obj3.check_balance()
obj4.check_balance()
obj5.check_balance()
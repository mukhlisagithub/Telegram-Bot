# Masala: Restoran nomli Class yarating. Class da menu_items, book_table, customer_orders nomli atributlar, hamda add_item_to_menu,
# book_tables va customer_order nomli metodlari bolsin. Quyidagi topshiriqlarni bajaring:
#     Menuga yangi element qoshish;
#     Table band qilish(book_table);
#     Mijozdan zakazlarni olish (customer orders);
#     Menuni korsatish;
#     Band qilingan tablelaeni korsatish;
#     Barcha buyurtmalarni chiqarish;
# Malumotlani saqlash uchun list yoki dict dan foydalanish mumkin

# ustoz yechbergan usullari;

from random import randint

class Restoran:
    def __init__(self):
        self.menu_items = []
        self.book_table = []
        self.customer_orders = []


    def add_item_to_menu(self, food):
        self.menu_items.append(food)

    def book_tables(self, table_number):
        self.book_table.append(table_number)

    def customer_order(self, order):
        self.customer_orders.append(order)

    def printDetails(self):
        for i in range(len(self.customer_orders)):
            print(f'Customer: {i+1} Table: {self.book_table[i]} Order: {self.customer_orders[i]}')

if __name__ == "__main__":
    restoran = Restoran()
    for i in range(1, 11):
        restoran.add_item_to_menu('food' + str(i))
    for i in range(5):
        restoran.book_tables(randint(1,20))
    for i in range(5):
        restoran.customer_order(restoran.menu_items[randint(0,9)])
    restoran.printDetails()
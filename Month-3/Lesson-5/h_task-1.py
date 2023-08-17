# Masala: Restoran nomli Class yarating. Class da menu_items, book_table, customer_orders nomli atributlar, hamda add_item_to_menu,
# book_tables va customer_order nomli metodlari bolsin. Quyidagi topshiriqlarni bajaring:
#     Menuga yangi element qoshish;
#     Table band qilish(book_table);
#     Mijozdan zakazlarni olish (customer orders);
#     Menuni korsatish;
#     Band qilingan tablelaeni korsatish;
#     Barcha buyurtmalarni chiqarish;
# Malumotlani saqlash uchun list yoki dict dan foydalanish mumkin


class Reataurant:
    def __init__(self):
        self.menu_items = []
        self.booked_tables = []
        self.customer_order = []

    def add_item_to_menu(self, item):
        self.menu_items.append(item)


    def book_table(self, table):
        self.book_table.append(table)


    def customer_order(self,order):
        self.customer_orders.append(order)


    def menu(self):
        print("Menu items: ")
        for item in self.menu_items:
            print(item)
        print()

    def booked_tables(self):
        print("Booked tables:")
        for table in self.book_table:
            print(table)
        print()

    def customer_orders(self):
        print("Customer Orders: ")
        for order in self.customer_orders:
            print(order)
        print()


restarant = Reataurant()



# Menuga yangi element qoshish;
restarant.add_item_to_menu('Kebab')
restarant.add_item_to_menu('Somsa')
restarant.add_item_to_menu('Salad')
restarant.add_item_to_menu('Pizza')



# Table band qilish(book_table);
# restarant.book_table(1)
# restarant.book_table(2)
# restarant.book_table(3)











# attribut => def init ichidagi metodlarga aytiladi
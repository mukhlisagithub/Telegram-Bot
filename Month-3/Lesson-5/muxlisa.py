class Restaurant:
    def __init__(self):
        self.menu_items = []
        self.booked_tables = []
        self.customer_orders = []

    def add_item_to_menu(self, item):
        self.menu_items.append(item)

    def book_table(self, table_number):
        self.booked_tables.append(table_number)

    def customer_order(self, order):
        self.customer_orders.append(order)

    def display_menu(self):
        print("Menu Items:")
        for item in self.menu_items:
            print(item)
        print()

    def display_booked_tables(self):
        print("Booked Tables:")
        for table in self.booked_tables:
            print(table)
        print()

    def display_customer_orders(self):
        print("Customer Orders:")
        for order in self.customer_orders:
            print(order)
        print()


# Creating a restaurant object
restaurant = Restaurant()

# Adding items to the menu
restaurant.add_item_to_menu("Burger")
restaurant.add_item_to_menu("Pizza")
restaurant.add_item_to_menu("Pasta")
restaurant.add_item_to_menu("Salad")

# Booking tables
restaurant.book_table(1)
restaurant.book_table(2)
restaurant.book_table(3)

# Taking customer orders
restaurant.customer_order("Table 1: Burger, Pizza")
restaurant.customer_order("Table 2: Pasta, Salad")
restaurant.customer_order("Table 3: Burger, Salad")

# Displaying menu
restaurant.display_menu()

# Displaying booked tables
restaurant.display_booked_tables()

# Displaying customer orders
restaurant.display_customer_orders()

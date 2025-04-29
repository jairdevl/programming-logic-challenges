class Product:
    def __init__(self, name, description, price, category):
        self.name = name
        self.description = description
        self.price = price
        self.category = category

class Order:
    def __init__(self, products):
        self.products = products
        self.status = "pending"

class OrderManagementSystem:
    def __init__(self):
        self.products = {}
        self.orders = []
        self.sales = {}
        self.total_earnings = 0

    def add_product(self, name, description, price, category):
        if name in self.products:
            print("Error: The product already exists in the menu.")
            return
        if price <= 0:
            print("Error: The price must be greater than zero.")
            return
        self.products[name] = Product(name, description, price, category)
        print(f"Product '{name}' added to the menu.")

    def place_order(self, products):
        order = Order(products)
        self.orders.append(order)
        for product in products:
            if product.name in self.products:
                self.total_earnings += product.price
                if product.name in self.sales:
                    self.sales[product.name] += 1
                else:
                    self.sales[product.name] = 1
        print("Order placed successfully.")
    
    def check_order_status(self, order_id):
        if order_id < len(self.orders):
            return self.orders[order_id].status
        else:
            print("Error: Invalid order ID.")
            return None

    def change_order_status(self, order_id, new_status):
        if order_id < len(self.orders):
            self.orders[order_id].status = new_status
            print(f"Order {order_id} status changed to '{new_status}'.")
        else:
            print("Error: Invalid order ID.")

    def generate_report(self):
        print("Sales Report:")
        print(f"Total Earnings: ${self.total_earnings:.2f}")
        print("Best-selling products:")
        for product, count in sorted(self.sales.items(), key=lambda x: x[1], reverse=True):
            print(f"{product}: {count} sold")
        print(f"Total orders: {len(self.orders)}")

def main():
    system = OrderManagementSystem()

    while True:
        print("\nOptions:")
        print("1. Add product")
        print("2. Place order")
        print("3. Check order status")
        print("4. Change order status")
        print("5. Generate report")
        print("6. Exit")
        option = input("Select an option: ")

        if option == '1':
            name = input("Product name: ")
            description = input("Product description: ")
            price = float(input("Product price: "))
            category = input("Product category: ")
            system.add_product(name, description, price, category)

        elif option == '2':
            products = []
            while True:
                name = input("Product name (or 'end' to finish): ")
                if name.lower() == 'end':
                    break
                if name in system.products:
                    products.append(system.products[name])
                else:
                    print("Product not found in the menu.")
            system.place_order(products)

        elif option == '3':
            order_id = int(input("Order ID: "))
            status = system.check_order_status(order_id)
            print(f"Order {order_id} status: {status}")

        elif option == '4':
            order_id = int(input("Order ID: "))
            new_status = input("New status (pending, in preparation, delivered): ")
            system.change_order_status(order_id, new_status)

        elif option == '5':
            system.generate_report()

        elif option == '6':
            print("Exiting the system.")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
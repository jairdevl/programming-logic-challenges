class Wine: 
    def __init__(self, name, variety, year, region, price): 
        self.name = name 
        self.variety = variety
        self.year = year
        self.region = region
        self.price = price

    def __repr__(self):
        return f"Wine(name={self.name}, variety={self.variety}, year={self.year}, region={self.region}, price={self.price})"

class WineManagement:
    def __init__(self):
        self.wines = []
        self.sales = []

    def add_wine(self, name, variety, year, region, price):
        if not isinstance(year, int) or year <= 0:
            print("Error: Year in the harvest must be a positive integer. ")
            return
        if price <= 0:
            print("Error: Price must be greater than zero. ")
            return
        if any(wine.name == name and wine.year == year for wine in self.wines):
            print("Error: Wine already exists. ")
            return
        new_wine = Wine(name, variety, year, region, price)
        self.wines.append(new_wine)
        print(f"Wine added: {new_wine} successfully. ")

    def delete_wine(self, name, year):
        for wine in self.wines:
            if wine.name == name and wine.year == year:
                self.wines.remove(wine)
                print(f"Wine deleted: {wine} successfully.")
                return
        print("Error: Wine not found. ")

    def consult_wine(self, variety=None, region=None):
        results = [wine for wine in self.wines if (variety is None or wine.variety == variety) and (region is None or wine.region == region)]
        if results:
            print("Wines found: ")
            for wine in results:
                print(wine)
        else:
            print("No wines found with the given criteria. ")

    def register_sale(self, name, year, quantity):
        for wine in self.wines:
            if wine.name == name and wine.year == year:
                total_sale = wine.price * quantity
                self.sales.append((wine, quantity, total_sale))
                print(f"Sale registered: {wine} successfully.")
                return
        print("Error: Wine not found.")    

    def daily_report(self):
        total_wines = len(self.wines)
        total_value = sum(wine.price for wine in self.wines)
        total_sales = sum(sale[2] for sale in self.sales)

        if self.sales:
            most_sold_wine = max(set(sale[0] for sale in self.sales), key=lambda wine: sum(v[1] for v in self.sales if v[0] == wine))
            quantity_sold = sum(v[1] for v in self.sales if v[0] == most_sold_wine)
        else:
            most_sold_wine = None
            quantity_sold = 0

        print("\nDaily Report:")
        print(f"Total number of wines: {total_wines}")
        print(f"Total value of wines: {total_value}")
        print(f"Total revenue generated: {total_sales}")
        if most_sold_wine:
            print(f"Most sold wine: {most_sold_wine} with {quantity_sold} units sold.")
        else:
            print("No sales recorded.")
def main():
    wine_management = WineManagement()

    while True:
        print("\nOptions:")
        print("1. Add wine")
        print("2. Delete wine")
        print("3. Consult wines")
        print("4. Register sale")
        print("5. Daily report")
        print("6. Exit")
        
        option = input("Select an option: ")

        if option == "1":
            name = input("Wine name: ")
            variety = input("Wine variety: ")
            year = int(input("Wine year: "))
            region = input("Wine region: ")
            price = float(input("Wine price: "))
            wine_management.add_wine(name, variety, year, region, price)
        elif option == "2":
            name = input("Wine name: ")
            year = int(input("Wine year: "))
            wine_management.delete_wine(name, year)
        elif option == "3":
            variety = input("Wine variety: ")
            region = input("Wine region: ")
            wine_management.consult_wine(variety if variety else None, region if region else None)
        elif option == "4":
            name = input("Wine name: ")
            year = int(input("Wine year: "))
            quantity = int(input("Quantity sold: "))
            wine_management.register_sale(name, year, quantity)

        elif option == "5":
            wine_management.daily_report()

        elif option == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
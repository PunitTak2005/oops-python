class Item:
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments. 
        assert price >= 0
        assert quantity >= 0, "Quantity must be a non-negative number."
        
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)

print(item1.calculate_total_price())
print(item2.calculate_total_price())

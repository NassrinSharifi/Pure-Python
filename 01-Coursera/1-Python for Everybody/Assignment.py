
class Item:
    def __init__(self, name: str, price:float, quantity=0):
        #run validations to recieved arguments
        assert  price >=0 , f"{price} is not equal or greater than zero"
        assert  quantity >=0 , f"{quantity} is not equal or greater than zero"
        # assign to self object
        print(f"I'm created :{name}")
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

item = Item("laptop",100,-3)
print(item.calculate_total_price())

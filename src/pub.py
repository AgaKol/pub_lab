class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = ["fanta"]
        self.stock = {}

    def increase_till(self, drink_price):
        self.till += drink_price

# write function to sell a drink,

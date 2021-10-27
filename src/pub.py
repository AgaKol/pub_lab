class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []
        self.stock = {}

    def increase_till(self, drink_price):
        self.till += drink_price

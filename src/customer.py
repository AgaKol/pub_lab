class Customer:
    def __init__(self, name, age, wallet):
        self.name = name
        self.age = age
        self.wallet = wallet
        self.drunkness = 0

    def reduce_wallet(self, drink_price):
        self.wallet -= drink_price

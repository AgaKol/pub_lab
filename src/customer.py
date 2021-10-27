class Customer:
    def __init__(self, name, age, wallet, drunkness):
        self.name = name
        self.age = age
        self.wallet = wallet
        self.drunkness = drunkness

    def reduce_wallet(self, drink_price):
        self.wallet -= drink_price

    def enough_money(self, drink):
        if self.wallet >= drink.price:
            return True
        else:
            return False

    def buy_drink(self, drink):
        if self.enough_money(drink):
            self.reduce_wallet(drink.price)
            self.drunkness += drink.alcohol_level

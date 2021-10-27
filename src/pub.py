class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = ["fanta"]
        self.stock = {}

    def increase_till(self, drink_price):
        self.till += drink_price

    def customer_of_age(self, customer):
        if customer.age >= 18:
            return True
        return False

    def customer_sober(self, customer):
        if customer.drunkness <= 5:
            return True
        return False

    def serve_customer(self, customer, drink):
        if self.customer_sober(customer) == True and self.customer_of_age(customer) == True:
            self.increase_till(drink.price)
            customer.buy_drink(drink)
        return False

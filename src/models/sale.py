from uuid import uuid4


class Sale:
    def __init__(self, customer, products):
        self.customer = customer
        self.products = products
        self.id = uuid4()

    def __str__(self):
        return str(self.id)

    def get_total(self):
        total = 0
        for product in self.products:
            total += product.price

        return total


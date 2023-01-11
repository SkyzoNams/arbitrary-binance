
class Action:
    def __init__(self, symbol1=None, symbol2=None, order_type=None, quantity=None, price=None):
        self.symbol1 = symbol1
        self.symbol2 = symbol2
        self.order_type = order_type
        self.price = price
        self.amount = None
        self.primary_amount = None

    def set_amount(self, amount):
        self.amount = "{:.7f}".format(amount)

    def set_primary_amount(self, primary_amount):
        if isinstance(primary_amount, str):
            self.primary_amount = primary_amount
        else:
            self.primary_amount = "{:.7f}".format(primary_amount)
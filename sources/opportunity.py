from aiohttp.hdrs import TRAILER
from sources.action import Action

class Opportunity:
    def __init__(self, action1=Action(), action2=Action(), action3=Action()):
        self.action1 = action1
        self.action2 = action2
        self.action3 = action3
        self.rate = None
        self.viable = None

    def is_viable(self):
        return False #to implement
    
    def set_action2(self, pair_obj):
        symbol1 = pair_obj['symbol'][:3]
        if self.action1.symbol2 == symbol1:
            self.action2 = Action(symbol1=symbol1, symbol2=pair_obj['symbol'][3:], order_type='SELL', quantity=None, price=float(pair_obj['price']))
        else:
            self.action2 = Action(symbol1=symbol1, symbol2=pair_obj['symbol'][3:], order_type='BUY', quantity=None, price=float(pair_obj['price']))

    def find_and_set_action3(self, market_data):
        for pair_obj in market_data:
            if self.action2.order_type == 'BUY':
                if pair_obj['symbol'].count(self.action1.symbol1) > 0 and pair_obj['symbol'].count(self.action2.symbol1) > 0:
                    self.set_action3(pair_obj)
            else:
                if pair_obj['symbol'].count(self.action1.symbol1) > 0 and pair_obj['symbol'].count(self.action2.symbol2) > 0:
                    self.set_action3(pair_obj)

    def set_action3(self, pair_obj):
        symbol1 = pair_obj['symbol'][:3]
        if symbol1 == self.action1.symbol1:
            self.action3 = Action(symbol1=symbol1, symbol2=pair_obj['symbol'][3:], order_type='SELL', quantity=None, price=float(pair_obj['price']))
        else:
            self.action3 = Action(symbol1=symbol1, symbol2=pair_obj['symbol'][3:], order_type='BUY', quantity=None, price=float(pair_obj['price']))

        
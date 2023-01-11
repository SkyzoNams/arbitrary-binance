from binance import Client

class Binance_API:
    def __init__(self, config):
        self.is_demo = config.demo_mode
        if self.is_demo:
            self.client = Client(config.binance_api['key'], config.binance_api['secret'])
        else:
            self.client = Client(config.binance_test_api['key'], config.binance_test_api['secret'])
            self.client = Client.API_URL = config.binance_test_api['api_url']


    def place_buy_oder(self, symbol, quantity):
        order = self.client.create_order(
            symbol = symbol,
            side = Client.SIDE_BUY,
            type = Client.ORDER_TYPE_MARKET,
            quantity=quantity)
        return order

    def place_sell_oder(self, symbol, quantity):
        order = self.client.create_order(
            symbol = symbol,
            side = Client.SIDE_SELL,
            type = Client.ORDER_TYPE_MARKET,
            quantity=quantity)
        return order

    def list_market_values(self):
        return self.client.get_all_tickers()

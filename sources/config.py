from sources.utils.utils import load_json_file

class Config_Loader:
    def __init__(self):
        config_json = load_json_file('config/config.json')
        self.demo_mode = config_json['demo_mode']
        self.max_amount = config_json['max_amount']
        self.min_profit_percent = config_json['min_profit_percent']
        self.blacklist = config_json['blacklist']
        self.binance_api = config_json['binance_api']
        self.binance_test_api = config_json['binance_test_api']
        self.exchange_fee_percent = config_json['exchange_fee_percent']
        self.starting_symbol = config_json['starting_symbol']
        self.starting_symbol_amount = config_json['starting_symbol_amount']
        self.order_timeout_second = config_json['order_timeout_second']
from sources.binance_api import Binance_API
from sources.detector import Detector
from sources.triangulator import Triangulator

class   Engine:
    def __init__(self, loaded_config):
        self.config = loaded_config
        self.binance_api = Binance_API(self.config)
        self.detector = Detector(self.config)
        self.triangulator = Triangulator(self.binance_api)

    def run(self):
        while 42:
            market = self.binance_api.list_market_values()
            opportunity = self.detector.opportunity(market)
            if opportunity is not None:
                self.triangulator.apply_opportunity(opportunity)
                # attendre la fin d'un ordre pour en placer un autre
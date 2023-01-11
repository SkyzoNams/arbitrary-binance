from sources.controler import Controler
from sources.opportunities import Opportunities
from sources.triangulator import Triangulator

class   Detector:
    def __init__(self, config):
        self.controler = Controler(config)
        self.opportunities = Opportunities()
        self.triangulator = Triangulator(config)

    def opportunity(self, market):
        for pair in market:
            if self.controler.is_invalid_pair(pair):
                return None
            if self.controler.is_blacklisted(pair) is False:
                if self.controler.is_starting_symbol(pair) is True: # peut être enlever les starting symbol
                    self.opportunities.add_starting_opportunity(pair)
                else:
                    self.opportunities.add_to_existing_opportunity(pair, market)
                self.detect_viable_opportunity()
        return None

    def detect_viable_opportunity(self):
        for opportunity in self.opportunities.opportunities_list:
            if opportunity.action3.symbol2 is not None and opportunity.viable is None:
                self.triangulator.calculate_vability(opportunity)
                if opportunity.viable is True:
                    print('An opportunity was found. Rate: ', str(opportunity.rate))
                    print(opportunity.action1.symbol1, '/', opportunity.action1.symbol2, ' amount: ', str(opportunity.action1.amount))
                    print(opportunity.action2.symbol1, '/', opportunity.action2.symbol2, ' amount: ', str(opportunity.action2.amount))
                    print(opportunity.action3.symbol1, '/', opportunity.action3.symbol2, ' amount: ', str(opportunity.action3.amount))
                    print('___________________________')
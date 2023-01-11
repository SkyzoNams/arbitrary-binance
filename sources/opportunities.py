from multiprocessing.sharedctypes import copy
from sources.action import Action
from sources.opportunity import Opportunity
from copy import copy

class Opportunities:
    def __init__(self):
        self.opportunities_list = []

    def add_starting_opportunity(self, pair_obj):
        self.opportunities_list.append(Opportunity(action1=Action(symbol1=pair_obj['symbol'][:3], symbol2=pair_obj['symbol'][3:], order_type='SELL', quantity=None, price=float(pair_obj['price'])), action2=Action(), action3=Action()))

    def add_to_existing_opportunity(self, pair_obj, market_data):
        new_opportunities = []
        for opportunity in self.opportunities_list:
            if opportunity.action1.symbol2 in pair_obj['symbol']:
                if opportunity.action2.symbol1 is None: 
                    opportunity.set_action2(pair_obj)
                    opportunity.find_and_set_action3(market_data)
                else:
                    new_opportunity = self.create_new_opportunity(opportunity)
                    new_opportunity.set_action2(pair_obj)
                    new_opportunity.find_and_set_action3(market_data)
                    new_opportunities.append(new_opportunity)
        self.opportunities_list = self.opportunities_list + new_opportunities
        return None

    def create_new_opportunity(self, opportunity):
       return Opportunity(action1=copy(opportunity.action1), action2=Action(), action3=Action())
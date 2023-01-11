
class Triangulator:
    def __init__(self, config):
        self.config = config

    def calculate_vability(self, opportunity):
        self.define_action_amount(opportunity.action1, None)
        self.define_action_amount(opportunity.action2, opportunity.action1)
        self.define_action_amount(opportunity.action3, opportunity.action2)
        self.define_viability(opportunity)

    def define_action_amount(self, action, previous_action):
        if previous_action is None:
            self.define_starting_amount(action)
        else:
            self.define_next_amount(action, previous_action)

    def define_starting_amount(self, action):
            if action.order_type == 'SELL':
                action.set_primary_amount(self.config.starting_symbol_amount[action.symbol1])
                action.set_amount(self.minus_exchange_fees(float(action.primary_amount) * action.price))
            else:
                action.set_primary_amount(self.config.starting_symbol_amount[action.symbol2])
                action.set_amount(self.minus_exchange_fees(float(action.primary_amount * action.price)))

    def define_next_amount(self, action, previous_action):
        action.set_primary_amount(previous_action.amount)
        if action.order_type == 'SELL':
            action.set_amount(self.minus_exchange_fees(float(previous_action.amount) * action.price))
        else:
            action.set_amount(self.minus_exchange_fees(action.price / float(previous_action.amount)))

    def define_viability(self, opportunity):
        opportunity.rate = (float(opportunity.action3.amount) - float(opportunity.action1.primary_amount)) / float(opportunity.action1.primary_amount)
        if opportunity.rate > self.config.min_profit_percent:
            opportunity.viable = True
        else:
            opportunity.viable = False

    def minus_exchange_fees(self, amount):
        return amount * self.config.exchange_fee_percent
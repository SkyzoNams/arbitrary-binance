
class Controler:
    def __init__(self, config):
        self.blacklist = config.blacklist
        self.starting_symbol = config.starting_symbol

    def is_starting_symbol(self, pair):
        if pair['symbol'][:3] in self.starting_symbol:
            return True
        return False

    def is_blacklisted(self, pair):
        if pair['symbol'][:3] in self.blacklist or pair['symbol'][3:] in self.blacklist:
            return True
        return False

    def is_invalid_pair(self, pair):
        return len(pair['symbol']) > 6
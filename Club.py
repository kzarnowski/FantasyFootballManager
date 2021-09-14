from Squad import Squad
from random import shuffle


class Club:
    def __init__(self, name, players):
        self.name = name
        self.players = players
        self.squad = self.random_squad()

    def __repr__(self):
        return self.name

    def random_squad(self):
        # TODO: generate team based on dictionary and with all positions
        shuffle(self.players['defenders'])
        shuffle(self.players['strikers'])
        players_list = self.players['defenders'][:5] + self.players['strikers'][:5]
        return Squad(self, players_list)

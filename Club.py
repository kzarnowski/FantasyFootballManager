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
        team = {}
        for pos in self.players:
            shuffle(self.players[pos])
            if pos == 'goalkeeper':
                n = 1
            elif pos == 'midfielder':
                n = 4
            else:
                n = 3
            team[pos] = self.players[pos][-n:]
        return Squad(self, team)

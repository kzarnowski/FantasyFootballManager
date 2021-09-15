from Team import Team
from random import shuffle


class Club:
    def __init__(self, name, players):
        self.name = name
        self.players = players
        self.squad, self.bench = self.random_squad()

    def __repr__(self):
        return self.name

    def random_squad(self):
        """ Returns a pair of dictionaries: an active squad and benched players """
        squad = {}
        bench = {}
        for pos in self.players:
            shuffle(self.players[pos])
            if pos == 'goalkeeper':
                n = 1
            elif pos == 'midfielder':
                n = 4
            else:
                n = 3
            squad[pos] = self.players[pos][-n:]
            bench[pos] = self.players[pos][:-n]
        return Team(self, squad), Team(self, bench)

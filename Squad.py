from statistics import mean


class Squad:
    def __init__(self, club, players):
        self.club = club
        self.players = players

    def __repr__(self):
        res = str(self.club)
        for k, v in self.players.items():
            res += f'\n{k}:\t {v}'
        return res

    @property
    def attack(self):
        return int(mean([p.ovr for p in self.players['striker']]))

    @property
    def defence(self):
        return int(mean([p.ovr for p in self.players['defender']]))

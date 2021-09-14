from statistics import mean
import Players


class Squad:
    def __init__(self, club, players):
        self.club = club
        self.defenders = [p for p in players if isinstance(p, Players.Defender.Defender)]
        self.strikers = [p for p in players if isinstance(p, Players.Striker.Striker)]

    def __repr__(self):
        res = str(self.club)
        for p in self.strikers + self.defenders:
            res += '\n' + str(p)
        return res

    @property
    def attack(self):
        return int(mean([p.ovr for p in self.strikers]))

    @property
    def defence(self):
        return int(mean([p.ovr for p in self.defenders]))

from statistics import mean


class Team:
    def __init__(self, club, players):
        self.club = club
        self.defenders = [p for p in players if p.position == 'defender']
        self.strikers = [p for p in players if p.position == 'striker']
        self.score = 0

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

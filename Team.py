from statistics import mean


class Team:
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

    def get_tired(self):
        for pos in self.players.values():
            for player in pos:
                player.get_tired()

    def change_condition(self, change):
        for pos in self.players.values():
            for player in pos:
                player.change_condition(change)

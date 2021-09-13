from Team import Team
from random import shuffle


class Club:
    def __init__(self, name, players):
        self.name = name
        self.players = players
        self.team = self.random_team(players)

    def __repr__(self):
        return self.name

    def random_team(self, players):
        # TODO: better randomization
        strikers = 0
        defenders = 0
        shuffle(players)
        squad = []
        for p in players:
            if strikers < 5 and p.position == 'striker':
                squad.append(p)
            if defenders < 5 and p.position == 'defender':
                squad.append(p)
            if strikers == defenders == 5:
                break
        return Team(self, squad)

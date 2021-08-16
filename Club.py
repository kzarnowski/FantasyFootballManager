from Team import Team


class Club:
    def __init__(self, name, players):
        self.name = name
        self.players = players
        self.team = None

    def __repr__(self):
        return self.name


from Players.Player import Player


class Goalkeeper(Player):
    def __init__(self, player_id, firstname, lastname, age, ovr):
        super().__init__(player_id, firstname, lastname, age, ovr)
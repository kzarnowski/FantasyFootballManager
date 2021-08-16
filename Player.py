class Player:
    def __init__(self, player_id, firstname, lastname, age, ovr, position):
        self.id = player_id
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.ovr = ovr
        self.position = position

    @property
    def name(self):
        return f'{self.firstname} {self.lastname}'

    def __repr__(self):
        return f'{self.name}, Age: {self.age}, OVR: {self.ovr}'

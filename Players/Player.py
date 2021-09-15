from configuration import MATCH_DURATION, BASE_CONDITION_CHANGE


class Player:
    def __init__(self, player_id, firstname, lastname, age, ovr):
        self.id = int(player_id)
        self.firstname = firstname
        self.lastname = lastname
        self.age = int(age)
        self.ovr = int(ovr)
        self.condition = 100

    @property
    def name(self):
        return f'{self.firstname} {self.lastname}'

    def __repr__(self):
        return f'{self.name}, Age: {self.age}, OVR: {self.ovr}, COND: {self.condition}'

    def get_tired(self):
        """ Condition loss per minute, older players get tired faster. Rounded to 0.5 """
        # TODO Find appropriate exponential function
        # self.condition -= round(2 * (BASE_CONDITION_LOSS + self.age - 25) / MATCH_DURATION) / 2
        match_loss = 0.3274 * self.age ** 2 - 6.1 * self.age + BASE_CONDITION_CHANGE + 27
        self.condition -= match_loss / MATCH_DURATION
        self.check_condition()

    def change_condition(self, change):
        self.condition += change - self.age + 25
        self.check_condition()

    def check_condition(self):
        if self.condition > 100:
            self.condition = 100
        elif self.condition < 0:
            self.condition = 0




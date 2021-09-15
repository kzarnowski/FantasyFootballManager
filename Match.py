from random import gauss, random
from configuration import RND, MATCH_DURATION, BASE_CONDITION_CHANGE


class Match:
    def __init__(self, home, away):
        self.home = home
        self.away = away
        self.result = [0, 0]

    def __repr__(self):
        return f'{self.home} vs {self.away} : {self.result}'

    def kick_off(self):
        print(f'Home: {self.home} - ATK: {self.home.squad.attack} - DEF: {self.home.squad.defence}')
        print(f'Away: {self.away} - ATK: {self.away.squad.attack} - DEF: {self.away.squad.defence}')
        for i in range(MATCH_DURATION):
            self.result[0] += self.shoot(self.home.squad, self.away.squad)
            self.result[1] += self.shoot(self.away.squad, self.home.squad)
            self.home.squad.get_tired()
            self.away.squad.get_tired()

        self.home.bench.change_condition(BASE_CONDITION_CHANGE * 4)
        self.away.bench.change_condition(BASE_CONDITION_CHANGE * 4)

        ###

        ###

        print(self, '\n')
        return self.result

    @staticmethod
    def shoot(atk_team, def_team):
        # print(f'Attacking team: {atk_team.club}')
        atk_power = atk_team.attack + int(gauss(0, RND * 2))
        def_power = def_team.defence + int(gauss(0, RND * 2))
        # print(f'Attack stats: {atk_power} -> {def_power}')
        chance = random() < 0.025
        if chance:
            if atk_power > def_power:
                # print('Goal!')
                scored = True
            elif atk_power == def_power:
                penalty_shoot = random() < 0.65
                if penalty_shoot:
                    # print('Penalty goal!')
                    scored = True
                else:
                    # print('Penalty miss!')
                    scored = False
            else:
                # print('No goal!')
                scored = False
        else:
            scored = False
        return scored

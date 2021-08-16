from random import gauss, random
from configuration import RND


class Match:
    def __init__(self, home_team, away_team):
        self.home_team = home_team
        self.away_team = away_team

    def __repr__(self):
        return f'{self.home_team} vs {self.away_team}'

    def kick_off(self):
        for round in range(5):
            self.shoot(self.home_team, self.away_team)
            self.shoot(self.away_team, self.home_team)
        print(f'Result: {str(self.home_team.club)}: {self.home_team.score} vs '
              f'{str(self.away_team.club)}: {self.away_team.score}')

    @staticmethod
    def shoot(atk_team, def_team):
        print(f'Attacking team: {atk_team}')
        atk_power = atk_team.attack + gauss(0, RND * 2)
        def_power = def_team.defence + gauss(0, RND * 2)
        if atk_power > def_power:
            atk_team.score += 1
            print('Goal!')
        elif atk_power == def_power:
            penalty_shoot = random() < 0.65
            if penalty_shoot:
                atk_team.score += 1
                print('Penalty goal!')
            else:
                print('Penalty miss!')
        else:
            print('No goal!')

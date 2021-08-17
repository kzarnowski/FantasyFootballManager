from random import gauss, random
from configuration import RND


class Match:
    def __init__(self, home_team, away_team):
        self.home_team = home_team
        self.away_team = away_team

    def __repr__(self):
        return f'{self.home_team} vs {self.away_team}'

    def kick_off(self):
        print(f'Home: {self.home_team.club} - ATK: {self.home_team.attack} - DEF: {self.home_team.defence}')
        print(f'Away: {self.away_team.club} - ATK: {self.away_team.attack} - DEF: {self.away_team.defence}')
        for i in range(5):
            self.shoot(self.home_team, self.away_team)
            self.shoot(self.away_team, self.home_team)
        print(f'Result: {str(self.home_team.club)}: {self.home_team.score} vs '
              f'{str(self.away_team.club)}: {self.away_team.score}')
        return self.home_team.score, self.away_team.score

    @staticmethod
    def shoot(atk_team, def_team):
        print(f'Attacking team: {atk_team.club}')
        atk_power = atk_team.attack + int(gauss(0, RND * 2))
        def_power = def_team.defence + int(gauss(0, RND * 2))
        print(f'Attack stats: {atk_power} -> {def_power}')
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

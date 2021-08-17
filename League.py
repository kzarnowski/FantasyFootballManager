from Match import Match

class League:
    def __init__(self, clubs):
        self.clubs = clubs
        self.standings = dict.fromkeys(clubs, 0)
        self.calendar = {
            1: ((clubs[0], clubs[1]), (clubs[2], clubs[3])),
            2: ((clubs[2], clubs[0]), (clubs[3], clubs[1])),
            3: ((clubs[0], clubs[3]), (clubs[1], clubs[2])),
            4: ((clubs[3], clubs[0]), (clubs[2], clubs[1])),
            5: ((clubs[0], clubs[2]), (clubs[1], clubs[3])),
            6: ((clubs[1], clubs[0]), (clubs[3], clubs[2])),
        }

    def __repr__(self):
        res = f'Club\t\tPoints\n'
        for club, points in self.standings.items():
            res += f'{club.name}\t\t{points}\n'
        return res

    def play_season(self):
        for matchday in range(1, 7):
            for c in self.clubs:
                c.team = c.random_team(c.players)
            games = [
                Match(self.calendar[matchday][0][0].team, self.calendar[matchday][0][1].team),
                Match(self.calendar[matchday][1][0].team, self.calendar[matchday][1][1].team)
            ]
            for g in games:
                result = g.kick_off()
                self.standings[g.home_team.club] += result[0]
                self.standings[g.away_team.club] += result[1]
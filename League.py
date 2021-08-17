from Match import Match

class League:
    def __init__(self, clubs):
        self.clubs = clubs
        self.standings = dict.fromkeys(clubs, 0)
        self.calendar = {
            1: ((0, 1), (2, 3)),
            2: ((2, 0), (3, 1)),
            3: ((0, 3), (1, 2)),
            4: ((3, 0), (2, 1)),
            5: ((0, 2), (1, 3)),
            6: ((1, 0), (3, 2)),
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
            games = []
            for pair in range(len(self.clubs)//2):
                games.append(Match(self.clubs[self.calendar[matchday][pair][0]], self.clubs[self.calendar[matchday][pair][1]]))
            for g in games:
                result = g.kick_off()
                self.standings[g.home] += result[0]
                self.standings[g.away] += result[1]

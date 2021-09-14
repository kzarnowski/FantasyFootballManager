from Match import Match


class League:
    def __init__(self, clubs):
        self.clubs = clubs
        self.standings = {club: {'points': 0, 'scored': 0, 'conceded': 0} for club in self.clubs}
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
                c.squad = c.random_squad()
            games = []
            for pair in range(len(self.clubs)//2):
                games.append(Match(self.clubs[self.calendar[matchday][pair][0]], self.clubs[self.calendar[matchday][pair][1]]))
            for g in games:
                result = g.kick_off()
                if result[0] > result[1]:
                    self.standings[g.home]['points'] += 3
                elif result[0] < result[1]:
                    self.standings[g.away]['points'] += 3
                else:
                    self.standings[g.home]['points'] += 1
                    self.standings[g.away]['points'] += 1

                self.standings[g.home]['scored'] += result[0]
                self.standings[g.home]['conceded'] += result[1]
                self.standings[g.away]['scored'] += result[1]
                self.standings[g.away]['conceded'] += result[0]

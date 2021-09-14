import csv
from random import shuffle

from League import League
from Club import Club
from Players.Striker import Striker
from Players.Midfielder import Midfielder
from Players.Defender import Defender
from Players.Goalkeeper import Goalkeeper


def random_team(players):
    team = dict.fromkeys(players.keys(), [])
    for pos in players:
        shuffle(players[pos])
        n = 3 if pos == 'goalkeepers' else 10
        team[pos] = players[pos][-n:]
        del players[pos][-n:]
    return team


if __name__ == '__main__':
    all_players = {
        'goalkeepers': [],
        'defenders': [],
        'midfielders': [],
        'strikers': []
    }

    with open('players_data.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            position = row[5]
            if position == 'striker':
                all_players['strikers'].append(Striker(*row[:-1]))
            elif position == 'midfielder':
                all_players['midfielders'].append(Midfielder(*row[:-1]))
            elif position == 'defender':
                all_players['defenders'].append(Defender(*row[:-1]))
            elif position == 'goalkeeper':
                all_players['goalkeepers'].append(Goalkeeper(*row[:-1]))

    SuperLeague = League([
        Club('Barca', random_team(all_players)),
        Club('Juve', random_team(all_players)),
        Club('City', random_team(all_players)),
        Club('Real', random_team(all_players))
    ])
    print(SuperLeague)
    SuperLeague.play_season()
    print(SuperLeague)

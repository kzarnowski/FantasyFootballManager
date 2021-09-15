import csv
from random import shuffle

from League import League
from Club import Club
from Players.Striker import Striker
from Players.Midfielder import Midfielder
from Players.Defender import Defender
from Players.Goalkeeper import Goalkeeper


def random_team(players):
    team = {}
    for pos in players:
        shuffle(players[pos])
        n = 3 if pos == 'goalkeeper' else 10
        team[pos] = players[pos][-n:]
        del players[pos][-n:]
    return team


if __name__ == '__main__':
    all_players = {
        'goalkeeper': [],
        'defender': [],
        'midfielder': [],
        'striker': []
    }

    with open('players_data.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            position = row[5]
            if position == 'striker':
                all_players['striker'].append(Striker(*row[:-1]))
            elif position == 'midfielder':
                all_players['midfielder'].append(Midfielder(*row[:-1]))
            elif position == 'defender':
                all_players['defender'].append(Defender(*row[:-1]))
            elif position == 'goalkeeper':
                all_players['goalkeeper'].append(Goalkeeper(*row[:-1]))

    SuperLeague = League([
        Club('Barca', random_team(all_players)),
        Club('Juve', random_team(all_players)),
        Club('City', random_team(all_players)),
        Club('Real', random_team(all_players))
    ])
    print(SuperLeague.clubs[0].squad)
    print(SuperLeague.clubs[0].bench)
    print(SuperLeague)
    SuperLeague.play_season()
    print(SuperLeague)

    print(SuperLeague.clubs[0].squad)

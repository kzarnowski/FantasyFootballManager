import csv

from League import League
from Club import Club
from Players.Striker import Striker
from Players.Midfielder import Midfielder
from Players.Defender import Defender
from Players.Goalkeeper import Goalkeeper

def random_players(all_players):
    results = dict.fromkeys(all_players.keys(), [])



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
        Club('Barca', all_players[0:50]),
        Club('Juve', all_players[50:100]),
        Club('City', all_players[100:150]),
        Club('Real', all_players[150:200])
    ])
    print(SuperLeague)
    SuperLeague.play_season()
    print(SuperLeague)
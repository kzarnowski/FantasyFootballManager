import csv

from League import League
from Player import Player
from Team import Team
from Club import Club
from Match import Match

if __name__ == '__main__':
    all_players = []
    with open('players_data.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            all_players.append(Player(*row))

    C1 = Club('Barca', all_players[0:50])
    C2 = Club('Juve', all_players[50:100])
    C3 = Club('City', all_players[100:150])
    C4 = Club('Real', all_players[150:200])
    SuperLeague = League([C1, C2, C3, C4])
    SuperLeague.play_season()
    print(SuperLeague)
    #GAME = Match(C1.team, C2.team)
    #GAME.kick_off()


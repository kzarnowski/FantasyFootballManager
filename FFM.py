import csv
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

    C1 = Club('Club 1', all_players[0:50])
    C2 = Club('Club 2', all_players[50:100])
    GAME = Match(C1.team, C2.team)
    #GAME.kick_off()


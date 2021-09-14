# FantasyFootballManager

It's a multifunctional project, which contains topics like software programming, data analysis, databases and statistical modelling. The main idea is based on computer games like FIFA or Football Manager. There is a database of players, grouped into clubs. Clubs take a part in leagues and play games with each other.

## v1


### CLUB
Have some sample players. Has a function to generate random squad from all available players for every matchday.

### SQUAD
By now 10 players (5 defenders, 5 strikers), in the future 11 players (goalkeeper, 3 defenders, 3 midfielders, 3 strikers). A squad is set randomly for every match. Squad has attributes like attack and defence, for now it is just an average of appropriate players ovr.

### PLAYER
Has attributes like ID, name, age and ovr. The ovr is just a basic rating, theoritcally 0-100 but for now there are no players with ovr < 60. Player.py is an abstract superclass, and there are subclasses for each position (Goalkeeper, Defender, Midfielder, Striker). For now, positions don't give any special actions.

### MATCH
For every match, there is a home and away team. For now, there are no benefits of being the home team. There is 5 rounds, clubs take turns. In every turn one club is trying to score a goal. For a shot to be successful, attacking power has to be higher than the other club defensive power. These powers are squad's attributes with some gauss random error for every turn. If powers are equal, there is some random chance to score a penalty goal.

<b>configuration.py</b> - for now it just defines how big are possible random errors during a match

### LEAGUE
Consist of 4 clubs, they play a season. Club plays two matches with every other one, home and away. Matches order is defined in league calendar. In league standings there are points (win: 3, draw: 1, lose: 0), goals scored and goals conceded.


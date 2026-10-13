from striker import Striker
from defender import Defender
from goalkeeper import GoalKeeper
from midfielder import Midfielder
from team import Team
from manager import Manager

striker = Striker('Cristiano Ronaldo', 1, 95)
midfielder = Midfielder('Declan Rice', 2, 93)
goalkeeper = GoalKeeper('David Raya', 3, 92)
defender = Defender('Sergio Ramos', 4, 89)
team = Team('Manchester United')
manager = Manager('Mourinho')

players = [striker, midfielder, goalkeeper, defender]
for player in players:
    print(player)
    print(player.train())
    print(player.recover())

team.sign_player(striker)
team.sign_player(defender)
print(team)
team.release_player('Sergio Ramos')
print(team)

print(manager)
manager.find_team(team)
print(manager)
from striker import Striker
from defender import Defender
from goalkeeper import GoalKeeper
from midfielder import Midfielder
from team import Team
from manager import Manager
from match import Match
from league import League


# Create the league
league = League("Premier League")

# Create teams
arsenal = Team("Arsenal")
man_utd = Team("Manchester United")
chelsea = Team("Chelsea")

# Add teams to the league dictionary
league.add_team(arsenal)
league.add_team(man_utd)
league.add_team(chelsea)


# Create players
striker = Striker("Cristiano Ronaldo", 1, 95, 25_000_000)
midfielder = Midfielder("Declan Rice", 2, 93, 25_000_000)
goalkeeper = GoalKeeper("David Raya", 3, 92, 25_000_000)
defender = Defender("Sergio Ramos", 4, 89, 25_000_000)
player_1 = Striker("Trash", 5, 12, 20)


# Sign players to their teams
arsenal.sign_player(goalkeeper)
arsenal.sign_player(player_1)

man_utd.sign_player(striker)

chelsea.sign_player(midfielder)
chelsea.sign_player(defender)


# Demonstrate dictionary lookup
print("Team lookup:")
print(league.get_team("Arsenal"))

print(league.get_team("Manchester United"))

# Demonstrate list comprehension across all teams
all_players = league.get_all_players()

print("\nAll players in the league:")
for player in all_players:
    print(player.get_name())

match1 = Match(arsenal, man_utd)
print(match1.simulate())

match2 = Match(arsenal, chelsea)
print(match2.simulate())

match3 = Match(man_utd, chelsea)
print(match3.simulate())

print(league.standings())
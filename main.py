from manager import Manager
from league import League


# My creative project is a Football Manager Simulator where you can create a team, and simulate matches within a league.
# The game does not consider promotion or relegation for teams within a league.
# Create the league.
premier_league = League('Premier League')

# Create the teams within the league
arsenal = premier_league.create_team('Arsenal')
manchester_united = premier_league.create_team('Manchester United')
chelsea = premier_league.create_team('Chelsea')
everton = premier_league.create_team('Everton')

# Give each of the teams a manager (they control player signing/releasing).
mikel_arteta = Manager('Mikel Arteta')
michael_carrick = Manager('Michael Carrick')
xabi_alonso = Manager('Xabi Alonso')
david_moyes = Manager('David Moyes')

mikel_arteta.join_team(arsenal)
michael_carrick.join_team(manchester_united)
xabi_alonso.join_team(chelsea)
david_moyes.join_team(everton)

# Create the players within the league.
david_raya = premier_league.create_player(
    'Goalkeeper', 'David Raya', 1, 93, 100000)
declan_rice = premier_league.create_player(
    'Midfielder', 'Declan Rice', 2, 94, 140000)
bukayo_saka = premier_league.create_player(
    'Striker', 'Bukayo Saka', 3, 95, 175000)
harry_maguire = premier_league.create_player(
    'Defender', 'Harry Maguire', 4, 89, 92000)
jordan_pickford = premier_league.create_player(
    'Goalkeeper', 'Jordan Pickford', 5, 87, 85000)
jack_grealish = premier_league.create_player(
    'Midfielder', 'Jack Grealish', 6, 93, 100000)
emi_martinez = premier_league.create_player(
    'Goalkeeper', 'Emi Martinez', 7, 87, 80000)
cole_palmer = premier_league.create_player(
    'Midfielder', 'Cole Palmer', 8, 89, 96000)
joao_pedro = premier_league.create_player(
    'Striker', 'Joao Pedro', 9, 78, 64000)

# View the league free agents.
for player in premier_league.get_free_agents():
    print(player)

# Sign the players to their teams using the manager capabilities.
mikel_arteta.sign_player(david_raya)
mikel_arteta.sign_player(declan_rice)
mikel_arteta.sign_player(bukayo_saka)

michael_carrick.sign_player(harry_maguire)

xabi_alonso.sign_player(jordan_pickford)
xabi_alonso.sign_player(jack_grealish)

david_moyes.sign_player(emi_martinez)
david_moyes.sign_player(cole_palmer)
david_moyes.sign_player(joao_pedro)

# The teams and their statistics can then be displayed.
print(arsenal)
print(manchester_united)
print(chelsea)
print(everton)

# Some matches can then be simulated.
MATCHES = [
    [arsenal, manchester_united], [arsenal, chelsea],
    [arsenal, everton], [manchester_united, chelsea],
    [manchester_united, everton], [chelsea, everton]
]

# Display the simulated outcome for each match.
for match in MATCHES:
    result = premier_league.create_match(
        match[0].team_name, match[1].team_name).simulate()
    print(result)

# Display the league standings.
print(premier_league.standings())

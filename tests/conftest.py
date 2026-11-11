from manager import Manager
from team import Team
from player import Player
from striker import Striker
from midfielder import Midfielder
from match import Match
from league import League
from goalkeeper import GoalKeeper
from defender import Defender
import pytest


@pytest.fixture
def league():
    return League('League 1')


@pytest.fixture
def manager():
    return Manager('Manager 1')

@pytest.fixture
def manager_2():
    return Manager('Existing Manager')


@pytest.fixture
def team():
    return Team('Team 1', 'League 1')


@pytest.fixture
def team2():
    return Team('Team 2', 'League 1')


@pytest.fixture
def striker():
    return Striker('Striker', 2, 90, 100000)


@pytest.fixture
def midfielder():
    return Midfielder('Midfielder', 3, 80, 100000)


@pytest.fixture
def defender():
    return Defender('Defender', 4, 70, 1000)


@pytest.fixture
def goalkeeper():
    return GoalKeeper('Goalkeeper', 5, 95, 100000)


@pytest.fixture
def match():
    # Create the league.
    league = League('Test League')

    # Create the managers for each team.
    manager = Manager('Manager 1')
    manager_2 = Manager('Manager 2')

    # Create the teams.
    team = league.create_team('Team 1')
    team2 = league.create_team('Team 2')

    # Create and sign the players.
    player = league.create_player('Striker', 'Player 1', 1, 100, 100000)
    player2 = league.create_player('Striker', 'Player 2', 2, 90, 100000)
    manager.join_team(team)
    manager_2.join_team(team2)
    manager.sign_player(player)
    manager_2.sign_player(player2)

    return Match(team, team2)


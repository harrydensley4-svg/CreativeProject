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
def manager():
    return Manager('Manager 1')

@pytest.fixture
def team():
    return Team('Team 1')

@pytest.fixture
def team2():
    return Team('Team 2')

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
def match(team, team2, striker, midfielder):
    team.sign_player(striker)
    team2.sign_player(midfielder)
    return Match(team, team2)

@pytest.fixture
def league():
    return League('League 1')

@pytest.fixture
def player():
    return Player('Player', 1, 90, 10)
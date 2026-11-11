from match import Match
import random
import pytest


class TestMatch:
    def test_initial_scores(self, match):
        assert match._Match__team_1_score == 0
        assert match._Match__team_2_score == 0

    def test_match_with_no_players(self, team, team2):
        assert Match(team, team2).simulate() == False

    def test_match_with_no_players_team_1(self, team, team2, manager, league):
        striker = league.create_player('Striker', 'Name', 1, 100, 100000)
        manager.join_team(team2)
        manager.sign_player(striker)
        assert Match(team, team2).simulate() == False

    def test_match_with_no_players_team_2(self, team, team2, manager, league):
        striker = league.create_player('Striker', 'Name', 1, 100, 100000)
        manager.join_team(team)
        manager.sign_player(striker)
        assert Match(team, team2).simulate() == False

    def test_create_match_with_wrong_type_team_1(self, team2):
        with pytest.raises(TypeError):
            Match('Team 1', team2)

    def test_create_match_with_wrong_type_team_2(self, team):
        with pytest.raises(TypeError):
            Match(team, 'Team 2')

    def test_match_simulate_draw(self, match):
        random.seed(1)
        assert match.simulate() == 'Team 1: 2-Team 2: 2'

    def test_match_simulate_team_1_win(self, match):
        random.seed(3)
        assert match.simulate() == 'Team 1: 2-Team 2: 1'

    def test_match_simulate_team_1_loss(self, match):
        random.seed(2)
        assert match.simulate() == 'Team 1: 0-Team 2: 2'

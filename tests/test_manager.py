import pytest
from manager import Manager


class TestManager:
    def test_name_property(self, manager):
        assert manager.name == 'Manager 1'

    def test_manager_team(self, manager):
        assert str(manager) == "Manager: Manager 1 | Team: None"

    def test_manager_team_wrong_type(self, manager):
        manager.join_team('Team 1')
        assert str(manager) == "Manager: Manager 1 | Team: None"

    def test_manager_find_team(self, manager, team):
        manager.join_team(team)
        assert str(manager) == "Manager: Manager 1 | Team: Team 1"

    def test_manager_find_team_already_with_team(self, manager, team, team2):
        manager.join_team(team)
        assert manager.join_team(team2) == False

    def test_manager_leave_team_no_team(self, manager):
        assert manager.leave_team() == False

    def test_team_already_has_manager(self, manager, manager_2, team):
        manager_2.join_team(team)
        assert manager.join_team(team) == False

    def test_manager_leave_team(self, manager, team):
        manager.join_team(team)
        assert manager.leave_team() == True

    def test_manager_sign_player(self, manager, league, team):
        player = league.create_player('Striker', 'Name', 1, 100, 100000)
        manager.join_team(team)
        assert manager.sign_player(player) == True

    def test_manager_sign_player_without_team(self, manager, league):
        player = league.create_player('Striker', 'Name', 1, 100, 100000)
        assert manager.sign_player(player) == False

    def test_manager_release_player(self, manager, league, team):
        player = league.create_player('Striker', 'Name', 1, 100, 100000)
        manager.join_team(team)
        manager.sign_player(player)
        assert manager.release_player(player) == True

    def test_manager_release_player_without_team(self, manager, league, team):
        player = league.create_player('Striker', 'Name', 1, 100, 100000)
        manager.join_team(team)
        manager.sign_player(player)
        manager.leave_team()
        assert manager.release_player(player) == False

import pytest
from manager import Manager

class TestManager:
    def test_name_property(self, manager):
        assert manager.name == 'Manager 1'

    def test_manager_team(self, manager, team):
        assert str(manager) == "Manager: Manager 1 | Team: None"

        manager.find_team('Team 1')
        assert str(manager) == "Manager: Manager 1 | Team: None"

        manager.find_team(team)
        assert str(manager) == "Manager: Manager 1 | Team: Team 1"

    def test_manager_leave_team(self, manager):
        manager.leave_team()
        assert str(manager) == "Manager: Manager 1 | Team: None"

    
from striker import Striker
from league import League


class TestTeam:
    def test_team_name(self, team):
        assert team.team_name == "Team 1"

    def test_team_not_a_player_signing(self, team):
        assert team.sign_player('Not a Player') == False

    def test_signing_exceeding_salary_cap(self, team):
        expensive_striker = Striker('Expensive Striker', 2, 100, 150000000)
        assert team.sign_player(expensive_striker) == False

    def test_signing_a_player_on_another_team(self, team, striker):
        striker.team = 'Another team'

        assert team.sign_player(striker) == False
        assert striker not in team.players

    def test_release_player_not_of_type_player(self, striker, team):
        team.sign_player(striker)
        assert team.release_player('Striker') == False

    def test_team_string_empty(self, team):
        result = str(team)

        assert "Team 1" in result
        assert "Salary Remaining : 120000000" in result
        assert "Team Rating : None" in result

    def test_team_insufficient_salary(self, manager, league, team, striker):
        player = league.create_player('Striker', 'Name', 1, 100, team.salary_cap + 1)
        manager.join_team(team)
        assert team.sign_player(player) == False

    def test_team_sign_not_type_player(self, manager, team):
        manager.join_team(team)
        assert team.sign_player('This Player') == False

    def test_team_player_not_in_league(self, manager, team):
        laliga = League('La Liga')
        player = laliga.create_player('Striker', 'Name', 1, 100, 10000)
        manager.join_team(team)
        assert player.league != team.league
        assert team.sign_player(player) == False

    def test_team_player_already_signed(self, manager, league, team):
        player = league.create_player('Striker', 'Name', 1, 100, 10000)
        manager.join_team(team)
        team.sign_player(player)
        assert team.sign_player(player) == False

    def test_player_already_contracted(self, manager, league, team):
        player = league.create_player('Striker', 'Name', 1, 100, 10000)
        manager.join_team(team)
        player.team = 'Team 2'
        assert team.sign_player(player) == False

    def test_release_player_without_manager(self, team, league, manager):
        player = league.create_player('Striker', 'Name', 1, 100, 10000)
        manager.join_team(team)
        team.sign_player(player)
        manager.leave_team()
        assert team.release_player(player) == False     

    def test_release_player_incorrect_type(self, team, league, manager):
        # Create a player to avoid the no players on team error.
        player = league.create_player('Striker', 'Name', 1, 100, 10000)
        manager.join_team(team)
        team.sign_player(player)
        assert team.release_player('This Player') == False     

    def test_release_player_not_found(self, team, league, manager):
        player = league.create_player('Striker', 'Name', 1, 100, 10000)
        defender = league.create_player('Defender', 'Defender', 2, 100, 10000)
        manager.join_team(team)
        team.sign_player(player)
        assert team.release_player(defender) == False     


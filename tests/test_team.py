class TestTeam:
    def test_team_name(self, team):
        assert team.team_name == "Team 1"

    def test_team_signing(self, team, striker):
        salary_cap = team.salary_cap
        team.sign_player(striker)
        assert striker in team.players
        assert striker.team == team.team_name
        assert team.salary_cap == salary_cap - striker.salary

    def test_team_not_a_player_signing(self, team):
        assert team.sign_player('Not a Player') is False

    def test_team_duplicate_player(self, team, striker):
        team.sign_player(striker)

        assert team.sign_player(striker) is False
        assert len(team.players) == 1

    def test_signing_a_player_on_another_team(self, team, striker):
        striker.team = 'Another team'

        assert team.sign_player(striker) is False
        assert striker not in team.players

    def test_release_player(self, team, striker):
        assert team.release_player(striker) is False

        team.sign_player(striker)
        assert team.release_player(striker) is True
        assert striker not in team.players

    def test_team_rating(self, team, striker):
        assert team.team_rating() is False
        team.sign_player(striker)
        assert team.team_rating() == 90

    def test_team_string_empty(self, team):
        result = str(team)

        assert "Team 1" in result
        assert "Salary Remaining : 120000000" in result
        assert "Team Rating : False" in result

    def test_team_string_with_player(self, team, striker):
        team.sign_player(striker)

        result = str(team)

        assert striker.name in result
        assert "Team Rating : 90" in result
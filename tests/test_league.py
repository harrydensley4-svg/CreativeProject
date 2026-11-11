from match import Match


class TestLeague:
    def test_league_with_no_teams(self, league):
        assert len(league.teams) == 0

    def test_league_add_team(self, league):
        league.create_team('New Team')
        assert len(league.teams) == 1

    def test_league_add_duplicate_team(self, league):
        league.create_team('Duplicate')
        league.create_team('Duplicate')
        assert len(league.teams) == 1

    def test_league_add_multiple_teams(self, league):
        league.create_team('Team 1')
        league.create_team('Team 2')
        assert len(league.teams) == 2

    def test_league_remove_teams(self, league):
        league.create_team('Team 1')
        assert league.remove_team('Team 1') == True

    def test_leagure_remove_team_not_found(self, league):
        assert league.remove_team('Not Found') == False

    def test_league_get_all_players_with_no_players(self, league):
        assert league.get_all_players() == []

    def test_add_player_wrong_type(self, league):
        assert league.create_player(True, 'Name', 1, 100, 95) == None

    def test_create_striker(self, league):
        assert str(league.create_player('Striker', 'Name', 1, 100, 96)
                   ) == 'Player 1: Name | Rating: 100 | Salary: 96'

    def test_create_defender(self, league):
        assert str(league.create_player('Defender', 'Name', 1, 100, 96)
                   ) == 'Player 1: Name | Rating: 100 | Salary: 96'

    def test_create_midfielder(self, league):
        assert str(league.create_player('Midfielder', 'Name', 1, 100,
                   96)) == 'Player 1: Name | Rating: 100 | Salary: 96'

    def test_create_goalkeeper(self, league):
        assert str(league.create_player('Goalkeeper', 'Name', 1, 100,
                   96)) == 'Player 1: Name | Rating: 100 | Salary: 96'

    def test_league_standings_no_teams(self, league):
        assert league.standings() is None

    def test_league_get_team(self, league):
        league.create_team('Team 1')
        assert str(league.get_team(
            'Team 1')) == f'Team : Team 1 | None | Salary Remaining : 120000000 | Team Rating : None' + '\n'

    def test_league_standings(self, league):
        league.create_team('Team 1')
        league.create_team('Team 2')
        # Shows that the standings contain the two teams
        assert len(league.standings()) == 2
        # It is difficult to assert it against the actual standings output since matches are randomly simulated.

    def test_league_create_player_invalid_position(self, league):
        assert league.create_player('Quarterback', 'Tom Brady', 9, 10, 10000) == None

    def test_league_remove_empty_team(self, league):
        league.create_team('Team 1')
        assert league.remove_team('Team 1') == True

    def test_league_remove_team_players_free_agency(self, league, manager):
        player = league.create_player('Striker', 'Name', 1, 100, 100000)
        team = league.create_team('Team 1')
        manager.join_team(team)
        manager.sign_player(player)
        assert len(league.get_free_agents()) == 0
        assert league.remove_team('Team 1') == True
        assert len(league.get_free_agents()) == 1

    def test_create_duplicate_player(self, league):
        league.create_player('Striker', 'Name', 1, 100, 100000)
        assert league.create_player('Striker', 'Name', 1, 100, 100000) == None

    def test_league_find_player(self, league):
        player = league.create_player('Striker', 'Name', 1, 100, 100000)
        result = league.find_player('Name')
        assert result == [player]

    def test_league_create_working_match_instance(self, league, team, team2):
        team = league.create_team('Team 1')
        team2 = league.create_team('Team 2')
        league.create_match('Team 1', 'Team 2')
        assert len(league.get_matches()) == 1

    def test_league_create_match_team_not_found(self, league, team, team2):
        assert league.create_match(team, team2) == None

    def test_league_create_match_duplicate_team(self, league):
        team = league.create_team('Team 1')
        assert league.create_match('Team 1', 'Team 1') == None


class TestLeague:
    def test_league_with_no_teams(self, league):
        assert len(league.teams) == 0

    def test_league_add_team(self, league, team):
        league.add_team(team)
        assert len(league.teams) == 1

    def test_league_add_duplicate_team(self, league, team):
        league.add_team(team)
        league.add_team(team)
        assert len(league.teams) == 1

    def test_league_add_multiple_teams(self, league, team, team2):
        league.add_team(team)
        league.add_team(team2)
        assert len(league.teams) == 2

    def test_league_get_all_players_with_no_players(self, league):
        pass

    def test_league_standings_no_teams(self, league):
        assert league.standings() is None
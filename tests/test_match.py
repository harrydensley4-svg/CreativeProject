class TestMatch:
    def test_initial_scores(self, match):
        assert match._Match__team_1_score == 0
        assert match._Match__team_2_score == 0

    def test_match_simulation(self, match):
        # How do I test simulation when it involves a random variable
        #assert 1 <= match.team_1_expected_goals() <= 100
        #assert 1 <= match.team_2_expected_goals() <= 100
        pass

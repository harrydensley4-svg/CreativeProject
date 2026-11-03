class TestGoalKeeper:
    def test_goalkeeper_recover(self, goalkeeper):
        assert goalkeeper.recover() == f'{goalkeeper.name} Strecthed. '

    def test_goalkeeper_train(self, goalkeeper):
        assert goalkeeper.train() == f'{goalkeeper.name} Practiced Saving. '
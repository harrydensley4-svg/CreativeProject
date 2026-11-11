class TestGoalKeeper:
    def test_goalkeeper_train(self, goalkeeper):
        assert goalkeeper.train() == f'{goalkeeper.name} Practiced Saving. Stamina: {goalkeeper.stamina} | Rating: {goalkeeper.rating}'

    def test_goalkeeper_recover(self, goalkeeper):
        assert goalkeeper.recover() == f'{goalkeeper.name} Stretched. Stamina: {goalkeeper.stamina} | Rating: {goalkeeper.rating}'

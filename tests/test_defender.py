class TestDefender:
    def test_defender_recover(self, defender):
        assert defender.recover() == f'{defender.name} Got a Massage. '

    def test_defender_train(self, defender):
        assert defender.train() == f'{defender.name} Practiced Defending. '
class TestDefender:
    def test_defender_recover(self, defender):
        assert defender.recover() == f'{defender.name} Got a Massage. Stamina: {defender.stamina} | Rating: {defender.rating}'

    def test_defender_train(self, defender):
        assert defender.train() == f'{defender.name} Practiced Defending. Stamina: {defender.stamina} | Rating: {defender.rating}'

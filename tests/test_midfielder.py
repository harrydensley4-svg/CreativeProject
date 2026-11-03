class TestMidfielder:
    def test_midfielder_recover(self, midfielder):
        assert midfielder.recover() == f'{midfielder.name} Had a Nap. '

    def test_midfielder_train(self, midfielder):
        assert midfielder.train() == f'{midfielder.name} Practiced Passing. '
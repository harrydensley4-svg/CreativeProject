class TestStriker:
    def test_striker_recovery_polymorphism(self, striker):
        assert str(striker.recover()) == f'{striker.name} Had An Ice Bath. Stamina: {striker.stamina} | Rating: {striker.rating}'

    def test_striker_practice_polymorphism(self, striker):
        assert str(striker.train()) == f'{striker.name} Practiced Shooting. Stamina: {striker.stamina} | Rating: {striker.rating}'

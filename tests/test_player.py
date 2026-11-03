from player import Player


class ConcretePlayer(Player):
    def train(self):
        pass

    def recover(self):
        pass


class TestPlayer:
    def test_player_name(self):
        player = ConcretePlayer("Ronaldo", 1, 95, 25_000_000)
        assert player.name == "Ronaldo"

    def test_player_id(self):
        player = ConcretePlayer("Ronaldo", 1, 95, 25_000_000)
        assert player.player_id == 1

    def test_player_rating(self):
        player = ConcretePlayer("Ronaldo", 1, 95, 25_000_000)
        assert player.rating == 95

    def test_player_salary(self):
        player = ConcretePlayer("Ronaldo", 1, 95, 25_000_000)
        assert player.salary == 25_000_000

    def test_player_team(self):
        player = ConcretePlayer("Ronaldo", 1, 95, 25_000_000)
        assert player.team is None

        player.team = "Manchester United"
        assert player.team == "Manchester United"

    def test_player_string(self):
        player = ConcretePlayer("Ronaldo", 1, 95, 25_000_000)

        assert str(player) == (
            "Player 1: Ronaldo | Rating: 95 | Salary: 25000000"
        )

    def test_train(self):
        player = ConcretePlayer("Ronaldo", 1, 95, 25_000_000)
        assert player.train() is None

    def test_recover(self):
        player = ConcretePlayer("Ronaldo", 1, 95, 25_000_000)
        assert player.recover() is None
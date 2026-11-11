from player import Player
import pytest


class TestPlayer:
    def test_abstract_player_class_instance(self):
        with pytest.raises(TypeError):
            Player('Name', 1, 90, 100)

    def test_get_player_id(self, striker):
        assert striker.player_id == 2

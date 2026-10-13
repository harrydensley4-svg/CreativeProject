from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, name, player_id, rating):
        self.__name = name
        self.__player_id = player_id
        self.__rating = rating

    def get_name(self):
        return self.__name

    def get_player_id(self):
        return self.__player_id

    def get_rating(self):
        return self.__rating

    name = property(get_name)
    player_id = property(get_player_id)
    rating = property(get_rating)

    @abstractmethod
    def train(self):
        pass

    @abstractmethod
    def recover(self):
        pass

    def __str__(self):
        return f'Player {self.__player_id}: {self.__name} | Rating: {self.__rating}'
from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, name, player_id, rating, salary, team=None):
        self.__name = name
        self.__player_id = player_id
        self.__rating = rating
        self.__salary = salary
        self.__team = team

    def get_name(self):
        return self.__name

    def get_player_id(self):
        return self.__player_id

    def get_rating(self):
        return self.__rating

    def get_salary(self):
        return self.__salary

    def get_team(self):
        return self.__team

    def set_team(self, team):
        self.__team = team

    name = property(get_name)
    player_id = property(get_player_id)
    rating = property(get_rating)
    salary = property(get_salary)
    team = property(get_team, set_team)

    @abstractmethod
    def train(self):
        pass

    @abstractmethod
    def recover(self):
        pass

    def __str__(self):
        return f'Player {self.__player_id}: {self.__name} | Rating: {self.__rating} | Salary: {self.__salary}'
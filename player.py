from abc import ABC, abstractmethod


class Player(ABC):
    """
    An abstract class representing a soccer player.
    Provides common attributes and functionality for different player positions.

    Attributes:
    -----------
    name (str): The name of the player.
    player_id (int): A unique identifier for the player.
    rating (int): The players overall rating.
    salary (int/float): The players salary.
    team (str): The name of the team that the player belongs to.
    MAX_RATING (int = 100): The maximum rating of the player.
    MAX_STAMINA (int = 100): The maximum stamina of the player.

    Methods:
    --------
    get_name():
        Returns the name of the player.

    get_player_id():
        Returns the unique identifier for the player.

    get_rating():
        Returns the players rating.

    set_rating(rating):
        updates the players rating. This will be used in the train and recover methods.

    get_salary():
        Returns the players salary.

    get_team():
        Returns the name of the team that the player belongs to.

    set_team(team_name):
        Sets the players team.

    get_stamina():
        Gets the players current stamina

    set_stamina(stamina):
        Updates the players stamina. This will be used in the train and recover methods.

    train():
        An abstract method that defines how a player trains.

    recover():
        An abstract method that defines how a player recovers.

    """
    MAX_RATING = 100
    MAX_STAMINA = 100

    def __init__(self, name, player_id, rating, salary):
        self.__name = name
        self.__player_id = player_id
        self.__rating = rating
        self.__salary = salary
        self.__team = None
        self.__league = None
        self.__stamina = self.MAX_STAMINA

    def get_name(self):
        """Returns the name of the player."""
        return self.__name

    def get_player_id(self):
        """Returns the unique player identifier."""
        return self.__player_id

    def get_rating(self):
        """Returns the rating of the player."""
        return self.__rating

    def set_rating(self, rating):
        """Updates the rating of the player."""
        self.__rating = rating

    def get_salary(self):
        """Returns the players salary."""
        return self.__salary

    def get_team(self):
        """Returns the team that the player is signed to."""
        return self.__team

    def set_team(self, team_name):
        """Sets the team that the player is signed to."""
        self.__team = team_name

    def get_league(self):
        """Get the league that the player belongs to."""
        return self.__league

    def set_league(self, league_name):
        """Set the league that the player belongs to."""
        self.__league = league_name

    def get_stamina(self):
        """Gets the stamina of the player."""
        return self.__stamina

    def set_stamina(self, stamina):
        """Updates the players stamina."""
        self.__stamina = stamina

    stamina = property(get_stamina, set_stamina)
    league = property(get_league, set_league)
    name = property(get_name)
    player_id = property(get_player_id)
    rating = property(get_rating, set_rating)
    salary = property(get_salary)
    team = property(get_team, set_team)

    @abstractmethod
    def train(self):
        """Returns the training method specific to the player type."""
        pass

    @abstractmethod
    def recover(self):
        """Returns the recovery method specific to the player type."""
        pass

    def __str__(self):
        """Returns a readable string description."""
        return f'Player {self.__player_id}: {self.__name} | Rating: {self.__rating} | Salary: {self.__salary}'


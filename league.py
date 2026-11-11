from striker import Striker
from defender import Defender
from goalkeeper import GoalKeeper
from midfielder import Midfielder
from team import Team
from match import Match


class DuplicateTeamError(Exception):
    def __init__(self, message="This Team Already Exists"):
        super().__init__(message)


class TeamNotFoundError(Exception):
    def __init__(self, message="This Team Does Not Exist"):
        super().__init__(message)


class DuplicatePlayerError(Exception):
    def __init__(self, message="This Player Already Exists"):
        super().__init__(message)


class InvalidPositionError(Exception):
    def __init__(self, message="This Position is Invalid"):
        super().__init__(message)


class League:
    """
    A class representing a soccer league

    Attributes:
    -----------
    name (str): the name of the league

    Methods:
    --------
    create_team(team):
        Creates a specific team within the league.

    get_team(team_name):
        Given the team_name, returns the team.

    get_teams():
        Returns a list of all the teams within the league.

    remove_team(team_name):
        Removes the team from the league.

    create_player(position, name, player_id, rating, salary):
        Given the position it creates a player instance. 

    get_all_players()
        Returns all the players within the league.

    get_free_agents()
        Returns all the players within the league that are not signed to a team.

    find_player(player_name)
        Given the player names, returns the player.

    create_match(team_1_name, team_2_name)
        Returns a match instance between the two teams. This can then be simulated. 

    standings()
        Returns the league standings which takes the form of a list of dictionaries. 
    """

    def __init__(self, name):
        self.__name = name
        self.__teams = {}
        self.__players = {}
        self.__matches = []

    def create_team(self, team_name):
        """
        Creates a Team instance within the league.

        Parameters:
        -----------
        team_name : str
            The name of the team being created.

        Returns:
        --------
        Team
            Returns the Team instance.
            returns False if the team already exists.

        """
        try:
            if team_name in self.__teams:
                raise DuplicateTeamError()
            else:
                team = Team(team_name, self.__name)
                self.__teams[team_name] = team
                return team
        except DuplicateTeamError as e:
            print(f'{e.__class__.__name__}: {e}')
            return False

    def get_team(self, team_name):
        """
        Gets a specific team within the league.

        Parameters:
        -----------
        team_name: str
            The name of the team to be found.

        Returns:
        --------
        Team
            If the team_name can be found in the list it returns the Team.

        """
        return self.__teams.get(team_name)

    def remove_team(self, team_name):
        """
        Removes a team from the league.

        Parameters:
        -----------
        team_name : str
            The name of the team being removed.

        Returns:
        --------
        bool
            Returns True if the team is removed.
            If the team is not found in the list of teams, it returns False.
        """
        try:
            team = self.__teams.get(team_name)
            if team is None:
                raise TeamNotFoundError()
            # The players in a team do not get removed they just become free agents
            for player in list(team.players):
                team.release_player(player)
            del self.__teams[team_name]
            return True
        except TeamNotFoundError as e:
            print(f'{e.__class__.__name__}: {e}')
            return False

    def get_teams(self):
        """Get the list of all the teams in the league"""
        return self.__teams.copy()

    teams = property(get_teams)

    def create_player(self, position, name, player_id, rating, salary):
        """
        Create a player instance.

        Parameters:
        -----------
        position: str
            The position of the player, this corresponds to the class of player being created.

        name: str
            The name of the player.

        player_id: int
            A unique identifier for the player. 
            This will be the key in the player dictionary.

        rating: int
            The rating of the player (how good they are).

        salary: int | float
            The players salary.

        Returns:
        --------
        Player
            Returns a player instance depending on the position entered.
            Returns none if the player already exists, or the position inputted does not exist.
        """
        try:
            if not isinstance(position, str):
                raise TypeError('Player Position Should Be A String')
            if player_id in self.__players:
                raise DuplicatePlayerError()

            if position.lower() == 'striker':
                player = Striker(name, player_id, rating, salary)
            elif position.lower() == 'defender':
                player = Defender(name, player_id, rating, salary)
            elif position.lower() == 'goalkeeper':
                player = GoalKeeper(name, player_id, rating, salary)
            elif position.lower() == 'midfielder':
                player = Midfielder(name, player_id, rating, salary)
            else:
                raise InvalidPositionError()
            player.league = self.__name
            self.__players[player_id] = player
            return player
        except Exception as e:
            print(f'{e.__class__.__name__}: {e}')
            return None

    def get_all_players(self):
        """Get the list of all the players in the league"""
        return list(self.__players.values())

    def get_free_agents(self):
        """Get the list of all players in the league not assigned to a team"""
        return [p for p in self.__players.values() if p.team is None]

    def find_player(self, player_name):
        """
        Find a specific player.

        Parameters:
        -----------
        player_name: str
            The name of the player to be found.

        Returns:
        --------
        Player
            If the player exists within the league, it returns the player object. 
            Otherwise it returns None.
        """
        return [
            player
            for player in self.get_all_players()
            if player.get_name() == player_name
        ]

    def create_match(self, team_1_name, team_2_name):
        """
        Create a match instance between two teams.

        Parameters:
        -----------
        team_1_name: str
            The name of the first team in the match

        team_2_name: str
            The name of the second team in the match

        Returns:
        --------
        Match
            Returns the match instance if both teams are found and they are not the same.
            Otherwise, it returns None.

        """
        try:
            team_1 = self.__teams.get(team_1_name)
            team_2 = self.__teams.get(team_2_name)
            if team_1 is None or team_2 is None:
                raise TeamNotFoundError()
            if team_1 is team_2:
                raise DuplicateTeamError()
            match = Match(team_1, team_2)
            self.__matches.append(match)
            return match
        except Exception as e:
            print(f'{e.__class__.__name__}: {e}')
            return None

    def get_matches(self):
        """Get the list of matches within the league"""
        return self.__matches

    def standings(self):
        """
        Gets the standings for the teams in the league

        Each win is equal to 3 points, draw is equal to 1 point and loss is equal to 0 points.

        Returns:
        --------
        List[]
            Returns a list of the teams and their results ordered by who has the most points.
        """
        if len(self.__teams) == 0:
            return None
        standings = []
        for team in self.__teams.values():
            wins = team.wins
            draws = team.draws
            losses = team.losses

            standings.append({
                'Team': team.team_name,
                'Played': wins + draws + losses,
                'Wins': wins,
                'Draws': draws,
                'Losses': losses,
                'Points': 3*wins + draws  # Wins are worth three points and draws are worth one
            })

        # This is sorted by points, so that the team with the most points is at the top.
        standings.sort(key=lambda row: row['Points'], reverse=True)
        return standings

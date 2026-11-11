from player import Player


class InsufficientSalaryError(Exception):
    def __init__(self, message="This exceeds the salary cap"):
        super().__init__(message)


class PlayerAlreadyContractedError(Exception):
    def __init__(self, message="This Player already has a team"):
        super().__init__(message)


class PlayerAlreadySignedError(Exception):
    def __init__(self, message="This Player is already on your team"):
        super().__init__(message)


class PlayerNotFoundError(Exception):
    def __init__(self, message="This Player is not on your Team"):
        super().__init__(message)


class NoPlayersOnTeamError(Exception):
    def __init__(self, message="This Team has no Players"):
        super().__init__(message)


class PlayerNotInLeagueError(Exception):
    def __init__(self, message="This Player is not in your league"):
        super().__init__(message)


class NoManagerError(Exception):
    def __init__(self, message="This team has no manager"):
        super().__init__(message)


class Team:
    """
    This class represents a soccer team.
    Manages the teams match results, salary cap, players, and statistics.
    They can sign and release players. 

    Attributes:
    -----------
    team_name (str): The name of the team.
    league_name (str): The name of the league that the team belongs to.

    Methods:
    --------
    get_team_name():
        Returns the name of the team.

    get_players():
        Returns a list of the players signed to the team.

    get_results():
        Returns a list of the teams simulated matches.

    get_wins():
        Returns the number of wins from the teams simulated matches.

    set_wins():
        Sets the number of matches won.

    get_losses():
        Returns the number of losses from the teams simulated matches.

    set_losses():
        Sets the number of matches lost.

    get_draws():
        Returns the number of draws from the teams simulated matches.

    set_draws():
        Sets the number of matches drawn.

    get_salary_cap():
        Returns the remaining team salary cap.

    sign_player(player):
        After validation, signs a player to the team.

    release_player(player):
        Removes a player from the team, restoring their salary to the salary cap.

    team_rating():
        Calculates the average rating of all the players in the team.
    """

    def __init__(self, team_name, league_name):
        self.__team_name = team_name
        self.__league = league_name
        self.__salary_cap = 120000000
        self.__players = []
        self.__results = []
        self.__wins = 0
        self.__losses = 0
        self.__draws = 0
        self.__manager = None

    def get_team_name(self):
        """Get the name of the team."""
        return self.__team_name

    def get_players(self):
        """Gets the list of players signed to the team."""
        return self.__players

    def get_results(self):
        """Gets the list of results."""
        return self.__results

    def get_wins(self):
        """Gets the number of wins."""
        return self.__wins

    def set_wins(self, wins):
        """Sets the number of wins."""
        self.__wins = wins

    def get_losses(self):
        """Gets the number of losses."""
        return self.__losses

    def set_losses(self, losses):
        """Sets the number of losses."""
        self.__losses = losses

    def get_draws(self):
        """Gets the number of draws."""
        return self.__draws

    def set_draws(self, draws):
        """Sets the number of draws."""
        self.__draws = draws

    def get_salary_cap(self):
        """Gets the salary cap."""
        return self.__salary_cap

    def get_league(self):
        """Gets the name of the league that the team belongs to."""
        return self.__league

    def get_manager(self):
        """Gets the team manager."""
        return self.__manager

    def set_manager(self, manager):
        """Sets the team manager."""
        self.__manager = manager

    manager = property(get_manager, set_manager)
    league = property(get_league)
    wins = property(get_wins, set_wins)
    losses = property(get_losses, set_losses)
    draws = property(get_draws, set_draws)
    team_name = property(get_team_name)
    players = property(get_players)
    results = property(get_results)
    salary_cap = property(get_salary_cap)

    def sign_player(self, player):
        """
        Sign a player to the team.

        Parameters:
        -----------
        player: Player
            The player that will be signed to the team.

        Returns:
        --------
        bool
            If the player can be added to the team, it returns true.
            If the team has no manager, the player belongs to a different league, 
            or the player is already signed ot a team, it returns false.
        """
        try:
            if self.__manager is None:
                raise NoManagerError()
            if not isinstance(player, Player):
                raise TypeError("Should be of Type Player")
            if player.league != self.__league:
                raise PlayerNotInLeagueError()
            if player in self.__players:
                raise PlayerAlreadySignedError()
            # Checks that the player they are signing is a free agent, if they already belong to a team they can not be signed
            if player.team is not None:
                raise PlayerAlreadyContractedError()
            if player.salary > self.__salary_cap:
                raise InsufficientSalaryError()
            else:
                self.__players.append(player)
                player.team = self.__team_name
                self.__salary_cap -= player.salary
                return True
        except Exception as e:
            print(f'{e.__class__.__name__}: {e}')
            return False

    def release_player(self, player):
        """
        Release a player from a team.

        Parameters:
        -----------
        player: Player
            The player that will be removed from the team.

        Returns:
        --------
        bool
            If the player can be removed, it returns true. 
            If the player can not be found, or the team does not have a manager, 
            it returns false.
        """
        try:
            if len(self.__players) == 0:
                raise NoPlayersOnTeamError()
            if self.__manager is None:
                raise NoManagerError()
            if not isinstance(player, Player):
                raise TypeError("Not type Player")
            if player not in self.__players:
                raise PlayerNotFoundError()
            else:
                self.__players.remove(player)
                self.__salary_cap += player.salary
                player.team = None
                return True
        except Exception as e:
            print(f'{e.__class__.__name__}: {e}')
            return False

    def team_rating(self):
        """
        Calculates the average rating of each player on the team.
        This is used as a metric for determining team strength, 
        which is important for the simulations.

        Returns:
        --------
        float
            Returns the average rating of the players on the team.
        """
        try:
            if len(self.__players) == 0:
                raise NoPlayersOnTeamError()
            else:
                team_rating = sum(
                    player.rating for player in self.__players)/len(self.__players)
                return team_rating
        except NoPlayersOnTeamError as e:
            print(f'{e.__class__.__name__}: {e}')
            return None

    def __str__(self):
        """Returns a readable string description."""
        player_list = ''
        for player in self.__players:
            player_list += str(player) + '\n'
        return f'Team : {self.__team_name} | {self.__manager} | Salary Remaining : {self.__salary_cap} | Team Rating : {self.team_rating()}' + '\n' + f'{player_list}'

from team import Team


class ManagerHasTeamError(Exception):
    def __init__(self, message="This Manager is already assigned to a team"):
        super().__init__(message)


class ManagerHasNoTeamError(Exception):
    def __init__(self, message="This Manager has no Team"):
        super().__init__(message)


class TeamHasManagerError(Exception):
    def __init__(self, message="This team already has a manager"):
        super().__init__(message)


class Manager:
    """
    This class represents a soccer manager.
    It Manages the assignment of a manager to a soccer team.

    Attributes:
    -----------
    name (str): The namr of the manager

    Methods:
    --------
    get_name():
        Returns the name of the manager

    find_team(team):
        If they are not currently assigned to a team, assigns the manager to a team.

    leave_team():
        Removes the manager from their assigned team.

    __str__():
        Returns a string representation of the manager.

    """

    def __init__(self, name):
        self.__team = None
        self.__name = name

    def get_name(self):
        """Returns the name of the manager."""
        return self.__name

    name = property(get_name)

    def join_team(self, team):
        """
        Join a specific team.

        Parameters:
        -----------
        team: Team
            This represents the team that the manager will join

        Returns:
        --------
        bool
            If the team can be joined, it returns true and the self.__team value is updated.
            If the manager already has a team, or the team already has a manager, 
            it returns false.
        """
        try:
            if not isinstance(team, Team):
                raise TypeError('Should be of type Team')
            if self.__team is not None:
                raise ManagerHasTeamError()
            if team.manager is not None:
                raise TeamHasManagerError()
            else:
                self.__team = team
                team.manager = self
                return True
        except Exception as e:
            print(f'{e.__class__.__name__}: {e}')
            return False

    def leave_team(self):
        """
        Leave the team that the manager is currently assigned to.

        Returns:
        --------
        bool
            Returns true and the manager has no team. 
            If the manager already has no team, then it returns false.
        """
        try:
            if self.__team == None:
                raise ManagerHasNoTeamError()
            else:
                self.__team.manager = None
                self.__team = None
                return True
        except Exception as e:
            print(f'{e.__class__.__name__}: {e}')
            return False

    def sign_player(self, player):
        """
        Sign a player to the team that the manager is controlling.
        Uses the functionality described within the Team class. 

        Parameters:
        -----------
        player: Player
            The player that the manager would like to sign.

        Returns:
        --------
        bool
            If the manager is currently signed to a team, it returns true and the player is signed.
            Otherwise it returns false. 
        """
        try:
            if self.__team is None:
                raise ManagerHasNoTeamError()
            else:
                return self.__team.sign_player(player)
        except ManagerHasNoTeamError as e:
            print(f'{e.__class__.__name__}: {e}')
            return False

    def release_player(self, player):
        """
        Release a player from a team.
        Uses the functionality described in the Team class.

        Parameters:
        -----------
        player: Player
            The player that the manager would like to release.

        Returns:
        --------
        bool
            If the manager is currently signed to a team, then player is released and it returns true. 
            Otherwise, if the validation fails within the team class method, then it returns false. 

        """
        try:
            if self.__team is None:
                raise ManagerHasNoTeamError()
            else:
                return self.__team.release_player(player)
        except ManagerHasNoTeamError as e:
            print(f'{e.__class__.__name__}: {e}')
            return False

    def __str__(self):
        """Returns a readable string description."""
        if self.__team:
            return f'Manager: {self.__name} | Team: {self.__team.team_name}'
        else:
            return f'Manager: {self.__name} | Team: None'

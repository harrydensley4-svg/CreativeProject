from team import Team

class ManagerHasTeamError(Exception):
    def __init__(self, message = "This Manager is already assigned to a team"):
        super().__init__(message)

class ManagerHasNoTeamError(Exception):
    def __init__(self, message = "This Manager has no Team"):
        super().__init__(message)

class Manager:
    def __init__(self, name):
        self.__team = None
        self.__name = name

    def get_name(self):
        return self.__name

    name = property(get_name)

    def find_team(self, team):
        try:
            if not isinstance(team, Team):
                raise TypeError('Should be of type Team')
            if self.__team is not None:
                raise ManagerHasTeamError()
            else:
                self.__team = team
                return True
        except Exception as e:
            print(f'{e.__class__.__name__}: {e}')
            return False

    def leave_team(self):
        try:
            if self.__team == None:
                raise ManagerHasNoTeamError()
            else:
                self.__team = None
                return True
        except Exception as e:
            print(f'{e.__class__.__name__}: {e}')
            return False

    def __str__(self):
        if self.__team:
            return f'Manager: {self.__name} | Team: {self.__team.team_name}'
        else:
            return f'Manager: {self.__name} | Team: None'
from team import Team

class Manager:
    def __init__(self, name):
        self.__name = name
        self.__team = None

    def get_name(self):
        return self.__name

    name = property(get_name)

    def find_team(self, team):
        if isinstance(team, Team):
            self.__team = team

    def __str__(self):
        if self.__team:
            return f'Manager: {self.__name} | Team: {self.__team.team_name}'
        else:
            return f'Manager: {self.__name} | Team: None'
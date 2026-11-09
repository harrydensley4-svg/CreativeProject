from player import Player
from striker import Striker
from defender import Defender
from goalkeeper import GoalKeeper
from midfielder import Midfielder
from team import Team

class DuplicateTeamError(Exception):
    def __init__(self, message = "This Team Already Exists"):
        super().__init__(message)

class TeamNotFoundError(Exception):
    def __init__(self, message = "This Team Does Not Exist"):
        super().__init__(message)


class League:
    def __init__(self, name):
        self.__name = name
        self.__teams = {}

    def add_team(self, team):
        try:
            if team.team_name in self.__teams:
                raise DuplicateTeamError()
            if not isinstance(team, Team):
                raise TypeError('Should be of type Team')
            else:
                self.__teams[team.team_name] = team
                return True
        except Exception as e:
            print(f'{e.__class__.__name__}: {e}')
            return False

    def get_team(self, team_name):
        return self.__teams.get(team_name)

    def remove_team(self, team_name):
        try:
            if team_name not in self.__teams:
                raise TeamNotFoundError()
            else:
                del self.__teams[team_name]
                return True
        except TeamNotFoundError as e:
            print(f'{e.__class__.__name__}: {e}')

    def get_teams(self):
        return self.__teams.copy()

    teams = property(get_teams)

    def create_player(self, position, name, player_id, rating, salary):
        try:
            if not isinstance(position, str):
                raise TypeError('Player Position Should Be A String')
            if position.lower() == 'striker':
                player = Striker(name, player_id, rating, salary)
                return player
            elif position.lower() == 'defender':
                player = Defender(name, player_id, rating, salary)
                return player
            elif position.lower() == 'goalkeeper':
                player = GoalKeeper(name, player_id, rating, salary)
                return player
            elif position.lower() == 'midfielder':
                player = Midfielder(name, player_id, rating, salary)
                return player    
        except TypeError as e:
            print(e)
            return None
   

    def get_all_players(self):
        return [
            player
            for team in self.__teams.values()
            for player in team.get_players()
        ]

    def find_player(self, player_name):
        return [
            player
            for player in self.get_all_players()
            if player.get_name() == player_name
        ]

    def standings(self):
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
                'Points': 3*wins + draws # Wins are worth three points and draws are worth one
            })

        # This is sorted by points, so that the team with the most points is at the top.
        standings.sort(key=lambda row: row['Points'], reverse=True)
        return standings
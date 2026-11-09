from player import Player

class InsufficientSalaryError(Exception):
    def __init__(self, message = "This exceeds the salary cap"):
        super().__init__(message)

class PlayerAlreadyContractedError(Exception):
    def __init__(self, message = "This Player already has a team"):
        super().__init__(message)

class PlayerAlreadySignedError(Exception):
    def __init__(self, message = "This Player is already on your team"):
        super().__init__(message)

class PlayerNotFoundError(Exception):
    def __init__(self, message = "This Player is not on your Team"):
        super().__init__(message)

class NoPlayersOnTeamError(Exception):
    def __init__(self, message = "This Team has no Players"):
        super().__init__(message)

class Team:
    def __init__(self, team_name):
        self.__team_name = team_name
        self.__salary_cap = 120000000
        self.__players = []
        self.__results = []
        self.__wins = 0
        self.__losses = 0
        self.__draws = 0

    def get_team_name(self):
        return self.__team_name

    def get_players(self):
        return self.__players

    def get_results(self):
        return self.__results

    def get_wins(self):
        return self.__wins

    def set_wins(self, wins):
        self.__wins = wins

    def get_losses(self):
        return self.__losses

    def set_losses(self, losses):
        self.__losses = losses

    def get_draws(self):
        return self.__draws

    def set_draws(self, draws):
        self.__draws = draws

    def get_salary_cap(self):
        return self.__salary_cap

    wins = property(get_wins, set_wins)
    losses = property(get_losses, set_losses)
    draws = property(get_draws, set_draws)
    team_name = property(get_team_name)
    players = property(get_players)
    results = property(get_results)
    salary_cap = property(get_salary_cap)

    def __find_player(self, name):
        for player in self.__players:
            if player.name == name:
                return player
        return None

    def sign_player(self, player):
        try:
            if not isinstance(player, Player):
                raise TypeError("Should be of Type Player")
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
        try:
            if len(self.__players) == 0:
                raise NoPlayersOnTeamError()
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
        try:
            if len(self.__players) == 0:
                raise NoPlayersOnTeamError()
            else:
                team_rating = sum(player.rating for player in self.__players)/len(self.__players)
                return team_rating
        except NoPlayersOnTeamError as e:
            print(f'{e.__class__.__name__}: {e}')
            return False

    def __str__(self):
        player_list = ''
        for player in self.__players:
            player_list += str(player) + '\n'
        return f'Team : {self.__team_name} | Salary Remaining : {self.__salary_cap} | Team Rating : {self.team_rating()}' + '\n' + f'{player_list}'
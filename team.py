from player import Player

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

    wins = property(get_wins, set_wins)
    losses = property(get_losses, set_losses)
    draws = property(get_draws, set_draws)

    def get_salary_cap(self):
        return self.__salary_cap

    def __find_player(self, name):
        for player in self.__players:
            if player.name == name:
                return player
        return None

    def sign_player(self, player):
        if not isinstance(player, Player):
            return False

        if player in self.__players:
            return False

        # Checks that the player they are signing is a free agent, if they already belong to a team they can not be signed
        if player.team is not None:
            return False

        if player.salary > self.__salary_cap:
            print('Not enough salary cap remaining')
            return False
        
        self.__players.append(player)
        player.team = self.__team_name
        self.__salary_cap -= player.salary

    def release_player(self, player):
        if player not in self.__players:
            return False

        self.__players.remove(player)
        self.__salary_cap += player.salary
        player.team = None
        return True

    def team_rating(self):
        if len(self.__players) != 0:
            team_rating = sum(player.rating for player in self.__players)/len(self.__players)
            return team_rating
        else:
            print('This team has no players')
            return False

    name = property(get_team_name)
    players = property(get_players)
    results = property(get_results)
    salary_cap = property(get_salary_cap)

    def __str__(self):
        player_list = ''
        for player in self.__players:
            player_list += str(player) + '\n'
        return f'Team : {self.__team_name} | Salary Remaining : {self.__salary_cap} | Team Rating : {self.team_rating()}' + '\n' + f'{player_list}'
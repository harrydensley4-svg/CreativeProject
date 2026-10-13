from player import Player

class Team:
    def __init__(self, team_name):
        self.__team_name = team_name
        self.__players = []
        self.__results = []

    def get_team_name(self):
        return self.__team_name

    def get_players(self):
        return self.__players

    def get_results(self):
        return self.__results

    def __find_player(self, name):
        for player in self.__players:
            if player.name == name:
                return player
        return None

    def sign_player(self, player):
        if isinstance(player, Player):
            self.__players.append(player)
        else:
            return False

    def release_player(self, name):
        player = self.__find_player(name)
        if player == None:
            return False
        self.__players.remove(player)
        return True

    team_name = property(get_team_name)
    players = property(get_players)
    results = property(get_results)

    def play_game(self):
        #TODO: make some game logic based on the players in the team, this can then be appended to the results
        pass

    def __str__(self):
        player_list = ''
        for player in self.__players:
            player_list += str(player) + '\n'
        return f'Team : {self.__team_name}' + '\n' + f'{player_list}'
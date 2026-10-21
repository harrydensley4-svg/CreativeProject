class League:
    def __init__(self, name):
        self.__name = name
        self.__teams = {}

    def add_team(self, team):
        if team.name in self.__teams:
            return False

        self.__teams[team.name] = team
        return True

    def get_team(self, team_name):
        return self.__teams.get(team_name)

    def remove_team(self, team_name):
        if team_name not in self.__teams:
            return False

        del self.__teams[team_name]
        return True

    def get_teams(self):
        return self.__teams.copy()

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
        standings = []
        for team in self.__teams.values():
            wins = team.wins
            draws = team.draws
            losses = team.losses

            standings.append({
                'Team': team.name,
                'Played': wins + draws + losses,
                'Wins': wins,
                'Draws': draws,
                'Losses': losses,
                'Points': 3*wins + draws # Wins are worth three points and draws are worth one
            })

        # This is sorted by points, so that the team with the most points is at the top.
        standings.sort(key=lambda row: row['Points'], reverse=True)
        return standings
import random
from team import Team

class EmptyTeamError(Exception):
    def __init__(self, message = "This Team has no players"):
        super().__init__(message)

class Match:
    """
        Attempt to simulate games given the teams, and their average ratings (?)
    """
    def __init__(self, team_1, team_2):
        if not isinstance(team_1, Team) and not isinstance(team_2, Team):
            raise TypeError("Should be Type Team")
        self.__team_1 = team_1 # Team object
        self.__team_2 = team_2 # Team object
        self.__team_1_score = 0
        self.__team_2_score = 0

    def simulate(self):
        # First ensures that both teams actually have players added to their list
        try:
            if len(self.__team_1.players) == 0:
                raise EmptyTeamError(f'{self.__team_1.team_name} has no players')
            if len(self.__team_2.players) == 0:
                raise EmptyTeamError(f'{self.__team_2.team_name} has no players')
            else:
                home_rating = self.__team_1.team_rating()
                away_rating = self.__team_2.team_rating()
                self.__team_1_score = self.team_1_expected_goals()
                self.__team_2_score = self.team_2_expected_goals()

                team_1_result = (f"{self.__team_1.team_name}: {self.__team_1_score}-{self.__team_2.team_name}: {self.__team_2_score}")
                team_2_result = (f"{self.__team_2.team_name}: {self.__team_2_score}-{self.__team_1.team_name}: {self.__team_1_score}")

                self.__team_1.results.append(team_1_result)
                self.__team_2.results.append(team_2_result)

                if self.__team_1_score > self.__team_2_score:
                    self.__team_1.wins += 1
                    self.__team_2.losses += 1
                elif self.__team_1_score < self.__team_2_score:
                    self.__team_1.losses += 1
                    self.__team_2.wins += 1
                else:
                    self.__team_1.draws += 1
                    self.__team_2.draws += 1

                return f"{self.__team_1.team_name}: {self.__team_1_score}-{self.__team_2.team_name}: {self.__team_2_score}"
        except Exception as e:
            print(f'{e.__class__.__name__}: {e}')
            return False

    def team_1_expected_goals(self):
        goals_1 = 0
        # This provides the chance that the team will score every minute based on their respective ratings
        scoring_chance = (self.__team_1.team_rating()/self.__team_2.team_rating())
        # Every minute of the game they have a chance to score based on the scoring chance provided above
        for i in range(90):
            if random.randint(0,100) < scoring_chance:
                goals_1 +=1

        return goals_1

    def team_2_expected_goals(self):
        goals_2 = 0
        scoring_chance = (self.__team_2.team_rating()/self.__team_1.team_rating())
        #Every minute of the game
        for i in range(90):
            if random.randint(0,100) < scoring_chance:
                goals_2 +=1

        return goals_2
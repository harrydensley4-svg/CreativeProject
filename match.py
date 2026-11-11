import random
from team import Team


class EmptyTeamError(Exception):
    def __init__(self, message="This Team has no players"):
        super().__init__(message)


class Match:
    """
        A class representing a specific Match event between two teams.
        It simulates games given the teams, and their average ratings.

        Attributes:
        -----------
        team_1 (Team): The first team participating in the match.
        team_2 (Team): The second team participating in the match.

        Methods:
        --------
        simulate():
            Simulates the match and updates team statistics.
        get_team_1():
            Returns the first team.
        get_team_2():
            Returns the second team.
    """

    def __init__(self, team_1, team_2):
        if not isinstance(team_1, Team) or not isinstance(team_2, Team):
            raise TypeError("Should be Type Team")
        self.__team_1 = team_1  # Team object
        self.__team_2 = team_2  # Team object
        self.__team_1_score = 0
        self.__team_2_score = 0

    def get_team_1(self):
        """Gets the first team in the match."""
        return self.__team_1

    def get_team_2(self):
        """Gets the second team in the match."""
        return self.__team_2

    team_1 = property(get_team_1)
    team_2 = property(get_team_2)

    def simulate(self):
        """
        Simulate the match based on relative team ratings.
        This uses the privated helper method __team_expected_goals()

        Returns:
        --------
        str
            Returns a string displaying the match outcome. 
            If the teams contain no players, it returns False.

        """
        try:
            if len(self.__team_1.players) == 0:
                raise EmptyTeamError(
                    f'{self.__team_1.team_name} has no players')
            if len(self.__team_2.players) == 0:
                raise EmptyTeamError(
                    f'{self.__team_2.team_name} has no players')

            self.__team_1_score = self.__team_expected_goals(
                self.__team_1, self.__team_2)
            self.__team_2_score = self.__team_expected_goals(
                self.__team_2, self.__team_1)

            team_1_result = (
                f"{self.__team_1.team_name}: {self.__team_1_score}-{self.__team_2.team_name}: {self.__team_2_score}")
            team_2_result = (
                f"{self.__team_2.team_name}: {self.__team_2_score}-{self.__team_1.team_name}: {self.__team_1_score}")

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
        except EmptyTeamError as e:
            print(f'{e.__class__.__name__}: {e}')
            return False

    def __team_expected_goals(self, attacking_team, defending_team):
        """
        Calculates the expected goals for the attacking team based on the rating of the defending team.

        Parameters:
        -----------
        attacking_team: Team
            The team that is undergoing attack.

        defending_team: team
            The team that is defending.

        Returns:
        --------
        int
            Returns the goals scored by the attacking team over the 90 minute game.

        """
        goals = 0
        # This provides the chance that the team will score every minute based on their respective ratings
        scoring_chance = (attacking_team.team_rating() /
                          defending_team.team_rating())
        # Every minute of the game they have a chance to score based on the scoring chance provided above
        for i in range(90):
            if random.randint(0, 100) < scoring_chance:
                goals += 1

        return goals

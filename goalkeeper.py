from player import Player


class GoalKeeper(Player):
    """
    A class to represent a Goalkeeper player archetype.
    This inherits from the Player class.

    Attributes:
    -----------
    RATING_GAIN (int = 2): The rating improvement from one training session.
    STAMINA_COST (int = 12): The stamina cost of one training session.
    STAMINA_GAIN (int = 9): The stamina gained from a recovery session.

    Methods:
    --------
    train():
        Implements the abstract train method.

    recover():
        Implements the abstract recover method.
    """

    RATING_GAIN = 2
    STAMINA_COST = 12
    STAMINA_GAIN = 9

    def train(self):
        """
        Represents the players indvidual training. 
        It improves the players rating and reduces their overall stamina.

        Returns
        --------
        str
            Returns the specific goalkeeper training plan.
        """
        if (self.stamina > self.STAMINA_COST ):
            self.stamina -= self.STAMINA_COST
            self.rating = min(self.MAX_RATING, self.rating + self.RATING_GAIN)
            return f'{self.name} Practiced Saving. Stamina: {self.stamina} | Rating: {self.rating}'

    def recover(self):
        """
        Represents the goalkeeper recovery programme.
        This improves their stamina.

        Returns
        --------
        str
            Returns the specific goalkeeper recovery plan.
        """
        self.stamina = min(self.MAX_STAMINA, self.stamina + self.STAMINA_GAIN)
        return f'{self.name} Stretched. Stamina: {self.stamina} | Rating: {self.rating}'

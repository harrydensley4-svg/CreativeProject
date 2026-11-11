from player import Player


class Midfielder(Player):
    """
    A class to represent a Midfielder player archetype.
    This inherits from the Player class.

    Attributes:
    -----------
    RATING_GAIN (int = 3): The rating points gained from a training session
    STAMINA_COST (int = 25): The stamina lost from a training session
    STAMINA_GAIN (int = 7): The stamina gained from a recovery session

    Methods:
    --------
    train():
        Implements the abstract train method.

    recover():
        Implements the abstract recover method.
    """
    RATING_GAIN = 3
    STAMINA_COST = 25
    STAMINA_GAIN = 7

    def train(self):
        """
        Represents the players indvidual training. 
        It improves the players rating and reduces their overall stamina.

        Returns
        --------
        str
            Returns the specific midfielder training plan.
        """
        if (self.stamina > self.STAMINA_COST ):
            self.stamina -= self.STAMINA_COST
            self.rating = min(self.MAX_RATING, self.rating + self.RATING_GAIN)
            return f'{self.name} Practiced Passing. Stamina: {self.stamina} | Rating: {self.rating}'

    def recover(self):
        """
        Represents the midfielder recovery programme.
        This improves their stamina.

        Returns
        --------
        str
            Returns the specific midfielder recovery plan.
        """
        self.stamina = min(self.MAX_STAMINA, self.stamina + self.STAMINA_GAIN)
        return f'{self.name} Had A Nap. Stamina: {self.stamina} | Rating: {self.rating}'

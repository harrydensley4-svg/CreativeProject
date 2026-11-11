from player import Player


class Striker(Player):
    """
    A class to represent a Striker player archetype.
    This inherits from the Player class.

    Attributes:
    -----------
    RATING_GAIN (int = 2): The rating points gained from a training session
    STAMINA_COST (int = 15): The stamina lost from a training session
    STAMINA_GAIN (int = 8): The stamina gained from a recovery session

    Methods:
    --------
    train():
        Implements the abstract train method.

    recover():
        Implements the abstract recover method.
    """
    RATING_GAIN = 2
    STAMINA_COST = 15
    STAMINA_GAIN = 8

    def train(self):
        """
        Represents the players indvidual training. 
        It improves the players rating and reduces their overall stamina.

        Returns
        --------
        str
            Returns the specific striker training plan.
        """
        if (self.stamina > self.STAMINA_COST ):
            self.stamina -= self.STAMINA_COST
            self.rating = min(self.MAX_RATING, self.rating + self.RATING_GAIN)
            return f'{self.name} Practiced Shooting. Stamina: {self.stamina} | Rating: {self.rating}'

    def recover(self):
        """
        Represents the strikers recovery programme.
        This improves their stamina.

        Returns
        --------
        str
            Returns the specific striker recovery plan.
        """
        self.stamina = min(self.MAX_STAMINA, self.stamina + self.STAMINA_GAIN)
        return f'{self.name} Had An Ice Bath. Stamina: {self.stamina} | Rating: {self.rating}'

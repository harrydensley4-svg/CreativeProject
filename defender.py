from player import Player


class Defender(Player):
    """
    A class to represent a Defender player archetype.
    This inherits from the Player class.

    Attributes:
    -----------
    RATING_GAIN (int = 1): The rating gain from a training session.
    STAMINA_COST (int = 6): The stamina cost of one training session.
    STAMINA_GAIN (int = 3): The stamina gained from one recovery session.

    Methods:
    --------
    train():
        Implements the abstract train method.

    recover():
        Implements the abstract recover method.
    """
    RATING_GAIN = 1
    STAMINA_COST = 6
    STAMINA_GAIN = 3

    def train(self):
        """
        Represents the players indvidual training. 
        It improves the players rating and reduces their overall stamina.

        Returns
        --------
        str
            Returns the specific defender training plan.
        """
        if (self.stamina > self.STAMINA_COST ):
            self.stamina -= self.STAMINA_COST
            self.rating = min(self.MAX_RATING, self.rating + self.RATING_GAIN)
            return f'{self.name} Practiced Defending. Stamina: {self.stamina} | Rating: {self.rating}'

    def recover(self):
        """
        Represents the defenders recovery programme.
        This improves their stamina.

        Returns
        --------
        str
            Returns the specific defender recovery plan.
        """
        self.stamina = min(self.MAX_STAMINA, self.stamina + self.STAMINA_GAIN)
        return f'{self.name} Got a Massage. Stamina: {self.stamina} | Rating: {self.rating}'
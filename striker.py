from player import Player

class Striker(Player):
    #TODO: make training improve skills, but lower health/stamina -> if health gets too low the player gets injured
    def train(self):
        return f'{self.name} Practiced Shooting. '

    def recover(self):
        return f'{self.name} Had An Ice Bath. '
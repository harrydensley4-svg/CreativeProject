from player import Player

class Midfielder(Player):
    def train(self):
        return f'{self.name} Practiced Passing. '

    def recover(self):
        return f'{self.name} Had a Nap. '
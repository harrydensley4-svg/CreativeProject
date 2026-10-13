from player import Player

class GoalKeeper(Player):
    def train(self):
        return f'{self.name} Practiced Saving. '

    def recover(self):
        return f'{self.name} Strecthed. '
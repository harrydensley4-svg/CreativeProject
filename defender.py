from player import Player

class Defender(Player):
    def train(self):
        return f'{self.name} Practiced Defending. '

    def recover(self):
        return f'{self.name} Got a Massage. '
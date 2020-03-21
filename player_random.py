import random


class PlayerRandom(object):

    def get_action(self, game):
        actions = game.available_moves()
        return random.choice(actions)

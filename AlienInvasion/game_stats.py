"""
Provides Game Stats Class for Alien Invasion game.

Manages the current stats of the game: amount of lives.
"""


class GameStats():

    def __init__(self, ship_limit):
        """Sets ship lives"""
        self.ships_left = ship_limit
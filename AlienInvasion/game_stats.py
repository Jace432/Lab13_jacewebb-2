"""
Provides Game Stats Class for Alien Invasion game.

Manages the current stats of the game: amount of lives, high score, max score,
current score, and current level.
"""

import json

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class GameStats():
    """Class for Game Stats"""
    def __init__(self, game: "AlienInvasion"):
        """Initializes the same stats"""
        self.game      = game
        self.settings  = game.settings
        self.max_score = 0
        self.init_saved_scores()
        self.reset_stats() 

    def reset_stats(self):
        """Resets stats that can change during game"""
        self.ships_left = self.settings.starting_ship_count
        self.score = 0 
        self.level = 1

    def init_saved_scores(self):
        """Initializes high score from file"""
        self.path = self.settings.scores_file
        if self.path.exists() and self.path.stat.__sizeof__() > 20:
            contents = self.path.read_text()
            scores   = json.loads(contents)
            self.hi_score = scores.get("hi_score", 0)
        else:
            self.hi_score = 0
            self.saved_scores()

    def saved_scores(self):
        """Saves high score to JSON file"""
        scores = {
            "hi_score" : self.hi_score
        }
        contents = json.dumps(scores, indent=4)
        try:
            self.path.write_text(contents)
        except FileNotFoundError as e:
            print(f"File Not Found: {e}")

    def update(self, collisions):
        """Updates the scores"""
        self._update_score(collisions)
        self._update_max_score() 
        self._update_hi_score()

    def _update_max_score(self):
        """Updates max score from current game"""
        if self.score > self.max_score:
            self.max_score = self.score

    def _update_hi_score(self):
        """Updates the all time high score"""
        if self.score > self.hi_score:
            self.hi_score = self.score

    def _update_score(self, collisions):
        """Updates current score"""
        for alien in collisions.values():
            self.score += self.settings.alien_points
    
    def update_level(self):
        """Updates game level"""
        self.level += 1



"""
Provides the Settings Class for the Alien Invasion Game.

Settings Class stores the games parameters for the screen size, FPS, file paths
for assests, ship settings, bullet settings, alien and alien fleet, and 
difficulty settings.
"""

from pathlib import Path
class Settings:
    """Class for the settings of the Alien Invasion Game"""
    
    def __init__(self):
        """Controls the settings of the game assets; size, sound, images, etc"""
        self.name: str = "Alien Invasion"
        self.screen_w  = 1200
        self.screen_h  = 800
        self.FPS       = 60
        self.bg_file   = Path.cwd() / "Assets" / "images"  / "Namek-png.png"
        self.difficulty_scale = 1.1
        self.scores_file = Path.cwd() / "Assets" / "file" / "scores.json"
        
        self.ship_file  = Path.cwd() / "Assets" / "images" / "goku.png"
        self.ship_w     = 150
        self.ship_h     = 100

        self.bullet_file   = Path.cwd() / "Assets" / "images" / "kame.png"
        self.laser_sound   = Path.cwd() / "Assets" / "sound" / "kame-sound.mp3"
        self.impact_sound  = Path.cwd() / "Assets" / "sound" / "explosion-312361.mp3"

        self.alien_file  = Path.cwd() / "Assets" / "images" / "kindpng_1560246.png"
        self.alien_w          = 40
        self.alien_h          = 40
        self.fleet_direction  = 1
        
    def initialize_dynamic_settings(self):
        """Initializes the dynamic settings"""
        self.ship_speed = 5
        self.starting_ship_count = 3
            
        self.bullet_w      = 25
        self.bullet_h      = 80
        self.bullet_speed  = 7 
        self.bullet_amount = 5
            
        self.fleet_speed      = 2
        self.fleet_drop_speed = 40
        self.alien_points     = 50
    
    def increase_difficulty(self):
        """Manges the increasing of difficulty"""
        self.ship_speed   *= self.difficulty_scale
        self.bullet_speed *= self.difficulty_scale
        self.fleet_speed  *= self.difficulty_scale




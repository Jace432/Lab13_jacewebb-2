"""
Provides Alien class for representing an alien in the Alien Invasion game.

Manages creating an alien and is responsible for its movement, boundaries, 
and drawing of the alien.
"""

import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_fleet import AlienFleet

class Alien(Sprite):
    """Class for an alien"""
    def __init__(self, fleet: "AlienFleet", x: float, y: float) -> None:
        """Initializes and creates alien"""
        super().__init__()
        self.fleet      = fleet
        self.screen     = fleet.game.screen
        self.boundaries = fleet.game.screen.get_rect()
        self.settings   = fleet.game.settings

        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(self.image, 
            (self.settings.alien_w, self.settings.alien_h)
            )
        
        self.rect        = self.image.get_rect()
        self.rect.x      = x
        self.rect.y      = y
        
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        
    def update(self) -> None:
        """Updates the alien position based on fleet direction and speed"""
        temp_speed  = self.settings.fleet_speed

        self.x     += temp_speed * self.fleet.fleet_direction
        self.rect.x = self.x
        self.rect.y = self.y

    def check_edges(self) -> bool:
        """Checks if the alien has reached the boudaries"""
        return (self.rect.right >= self.boundaries.right or 
        self.rect.left <= self.boundaries.left)


    def draw_alien(self) -> None:
        """Draws the alien on screen"""
        self.screen.blit(self.image, self.rect)
        
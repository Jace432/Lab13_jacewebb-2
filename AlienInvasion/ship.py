"""
Provides Ship Class for the Alien Invasion Game.

Ship Class manages the controls, movement, and overall interaction of the ship,
the arsenal, and the alien fleet.
"""

import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal

class Ship:
    """Class for the spaceship in Alien Invasion Game"""
    
    
    def __init__(self, game: "AlienInvasion", arsenal: "Arsenal") -> None:
        """Initialize ship and position """
        self.game        = game
        self.settings    = game.settings
        self.screen      = game.screen
        self.boundaries  = self.screen.get_rect()
        
        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(self.image, 
            (self.settings.ship_w, self.settings.ship_h)
            )
        
        self._center_ship()
        self.moving_right   = False
        self.moving_left    = False
        self.arsenal        = arsenal

    def _center_ship(self):
        """Finds the center of the ship"""
        self.rect           = self.image.get_rect()
        self.rect.midbottom = self.boundaries.midbottom
        self.x              = float(self.rect.x)
    
    def update(self) -> None:
        """Updates ship position and arsenal"""
        self._update_ship_movement()
        self.arsenal.update_arsenal()


        self.rect.x = self.x

    def _update_ship_movement(self):
        """Updates ship movement and ensures ship stays on screen"""
        temp_speed = self.settings.ship_speed
        if self.moving_right and self.rect.right < self.boundaries.right:
            self.x += temp_speed
        if self.moving_left and self.rect.left > self.boundaries.left:
            self.x -= temp_speed

    def draw(self) -> None:
        """Draws the ship on screen"""
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire(self) -> bool:
        """Tells arsenal to fire bullet"""
        return self.arsenal.fire_bullet()
    
    def check_collisions(self, other_group):
        """Checks for collisions of the ship with other group"""
        if pygame.sprite.spritecollideany(self, other_group):
            self._center_ship()
            return True
        return False
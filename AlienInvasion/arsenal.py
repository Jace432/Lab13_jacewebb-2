"""
Provides Arsenal Class for controling and managing bullets for the
Alien Invasion Game.

Arsenal Class handles the creation, updating, drawing, and firing bullets. 
Ensures bullets do not exceed the limit and they stay on screen.
"""

import pygame
from typing import TYPE_CHECKING
from bullet import Bullet

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Arsenal:
    """Controls the ship's arsenal/bullets"""
    def __init__(self, game: "AlienInvasion") -> None:
        """Initialize arsenal"""
        self.game     = game
        self.settings = game.settings
        self.arsenal  = pygame.sprite.Group()

    def update_arsenal(self) -> None:
        """Updates position of bullets and removes off-screen bullets"""
        self.arsenal.update()
        self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self) -> None:
        """Removes bullets that go off-screen"""
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0:
                self.arsenal.remove(bullet)

    def draw(self) -> None:
        """Draws bullets on screen"""
        for bullet in self.arsenal:
            bullet.draw_bullet()
    
    def fire_bullet(self) -> bool:
        """Controls the firing of bullets; no more than max amount on screen"""
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False

    

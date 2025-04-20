"""
Provides Button Class for Alien Invasion game.

Button class manages the "Play" button. Responsible for drawing the button, 
what the button says, and clicking the button.
"""

import pygame.font
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    

class Button:
    """Class for Button and its attributes"""
    def __init__(self, game: "AlienInvasion", msg):
        """Initializes the button font, msg, location"""
        self.game = game
        self.screen  = game.screen
        self.boudaries = game.screen.get_rect()
        self.settings = game.settings
        self.font = pygame.font.Font(self.settings.font_file, 
                            self.settings.button_font_size)
        self.rect = pygame.Rect(0,0, self.settings.button_w, self.settings.button_h)
        self.rect.center = self.boudaries.center
        self._prep_msg(msg)
        
    def _prep_msg(self, msg):
        """Manges the button and centers it on screen"""
        self.msg_image = self.font.render(msg, True, self.settings.text_color, None)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        """Draws the button on screen"""
        self.screen.fill(self.settings.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def check_clicked(self, mouse_pos) -> bool:
        """Checks if the button was clicked"""
        return self.rect.collidepoint(mouse_pos)
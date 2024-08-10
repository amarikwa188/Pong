import pygame
from pygame import Surface, Rect

from settings import GameSettings

class Player:
    def __init__(self, settings: GameSettings, screen: Surface) -> None:
        self.settings: GameSettings = settings
        self.screen: Surface = screen

        self.rect: Rect = Rect(0, 0, self.settings.paddle_width, 
                               self.settings.paddle_height)
        self.screen_rect: Rect = self.screen.get_rect()

        self.rect.left = self.settings.paddle_width
        self.rect.centery = self.screen_rect.centery


    def draw_player(self) -> None:
        pygame.draw.rect(self.screen, self.settings.fg_color, self.rect)
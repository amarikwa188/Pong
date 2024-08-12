import pygame
from pygame import Surface, Rect, Mask
from pygame.sprite import Sprite, Group

from settings import GameSettings


class CPU(Sprite):
    def __init__(self, settings: GameSettings, screen: Surface,
                 paddle_group: Group):
        self.settings: GameSettings = settings

        self.screen: Surface = screen
        self.screen_rect: Rect = self.screen.get_rect()

        self.height: int = self.settings.paddle_height
        self.width: int = self.settings.paddle_width
        self.speed: int = self.settings.paddle_speed

        self.surface: Surface = Surface((self.width, self.height))
        self.rect: Rect = self.image.get_rect()
        self.mask: Mask = pygame.mask.from_surface(self.surface)

        paddle_group.add(self)

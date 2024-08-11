import pygame
from pygame import Surface, Rect, Mask
from pygame.sprite import Sprite, Group


class Ball(Sprite):
    def __init__(self, screen: Surface) -> None:
        super().__init__()
        self.screen: Surface = screen
        self.screen_rect: Rect = self.screen.get_rect()

        self.image: Surface = pygame.image.load("sprites/ball.png")\
            .convert_alpha()
        self.rect: Rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

        self.mask: Mask = pygame.mask.from_surface(self.image)

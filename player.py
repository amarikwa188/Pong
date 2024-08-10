import pygame
from pygame import Surface, Rect

from settings import GameSettings

class Player:
    def __init__(self, settings: GameSettings, screen: Surface) -> None:
        self.settings: GameSettings = settings
        self.screen: Surface = screen

        self.height: int = self.settings.paddle_height
        self.width: int = self.settings.paddle_width
        self.speed: float = self.settings.paddle_speed

        self.rect: Rect = Rect(0, 0, self.width, self.height)
        self.screen_rect: Rect = self.screen.get_rect()

        self.rect.left = self.width
        self.rect.centery = self.screen_rect.centery

        self.y: float = float(self.rect.centery)

        self.moving_up: bool = False
        self.moving_down: bool = False


    def update(self) -> None:
        if self.moving_up and self.rect.top > 0:
            self.y -= self.speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.speed

        self.rect.centery = self.y


    def draw_player(self) -> None:
        pygame.draw.rect(self.screen, self.settings.fg_color, self.rect)
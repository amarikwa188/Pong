import pygame
from pygame import Surface, Rect, Mask
from pygame.sprite import Sprite, Group

from settings import GameSettings
from ball import Ball


class CPU(Sprite):
    def __init__(self, settings: GameSettings, screen: Surface,
                 paddle_group: Group, ball: Ball):
        super().__init__()
        self.settings: GameSettings = settings

        self.ball: Ball = ball

        self.screen: Surface = screen
        self.screen_rect: Rect = self.screen.get_rect()

        self.height: int = self.settings.paddle_height
        self.width: int = self.settings.paddle_width
        self.speed: int = self.settings.paddle_speed * 0.8

        # how far from the center on the x-axis will the ai start trying to match the ball
        self.detection_range: int = 80

        self.surface: Surface = Surface((self.width, self.height))
        self.rect: Rect = self.surface.get_rect()

        self.rect.centery = self.screen_rect.centery
        self.rect.right = self.settings.screen_width - 2*self.width

        self.mask: Mask = pygame.mask.from_surface(self.surface)
        paddle_group.add(self)

        self.y: float = float(self.rect.y)


    def update(self) -> None:
        # try to math centery values with the ball when it in the right half
        ball_y: int = self.ball.rect.y
        ball_x: int = self.ball.rect.x

        if ball_x > self.settings.screen_width//2 + self.detection_range:
            if self.y > ball_y and self.rect.top > 0:
                self.y -= self.speed
            elif self.y < ball_y and self.rect.bottom < self.screen_rect.bottom:
                self.y += self.speed

        self.rect.centery = self.y


    def draw_paddle(self) -> None:
        pygame.draw.rect(self.screen, self.settings.fg_color, self.rect)
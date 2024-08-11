import pygame
from pygame import Surface, Rect, Mask
from pygame.sprite import Sprite, Group


class Ball(Sprite):
    def __init__(self, screen: Surface, ball_group: Group,
                 paddle_group: Group) -> None:
        super().__init__()
        self.screen: Surface = screen
        self.screen_rect: Rect = self.screen.get_rect()

        self.image: Surface = pygame.image.load("sprites/ball.png")\
            .convert_alpha()
        self.rect: Rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

        self.x: float = float(self.rect.x)
        self.y: float = float(self.rect.y)

        self.mask: Mask = pygame.mask.from_surface(self.image)

        self.move: bool = True

        ball_group.add(self)
        self.paddle_group: Group = paddle_group

    def update(self) -> None:
        self.check_collisions(self.paddle_group)

        if self.move:
            self.x -= 0.1
            self.rect.x = self.x

    def check_collisions(self, paddle_group: Group) -> None:
        if pygame.sprite.spritecollide(self, paddle_group, False):
            if pygame.sprite.spritecollide(self, paddle_group, False,
                                           pygame.sprite.collide_mask):
                self.move = False


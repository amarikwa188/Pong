import random as rng

import pygame
from pygame import Surface, Rect, Mask
from pygame.sprite import Sprite, Group

from settings import GameSettings


class Ball(Sprite):
    """Represents an instance of the ball class."""
    def __init__(self, settings: GameSettings, screen: Surface,
                 ball_group: Group, paddle_group: Group) -> None:
        """
        Initializes a ball object.

        :param screen: a reference to the game screen.
        :param ball_group: a sprite group containing the ball.
        Used for detecting collisions.
        :param paddle_group:  a sprite group containing the paddles.
        Used for detecting collisions.
        """
        super().__init__()

        # make a reference to the settings and screen
        self.settings: GameSettings = settings
        self.screen: Surface = screen
        self.screen_rect: Rect = self.screen.get_rect()

        # load the sprite image and position the surface
        self.image: Surface = pygame.image.load("sprites/ball.png")\
            .convert_alpha()
        self.rect: Rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

        # create float variables to handle smooth movement
        self.x: float = float(self.rect.x)
        self.y: float = float(self.rect.y)

        # handle bounce and movement
        self.speed: float = self.settings.ball_speed
        self.v_x: float = -self.speed
        self.v_y: float = 0.0

        # create a mask to handle pixel-perfect collisions
        self.mask: Mask = pygame.mask.from_surface(self.image)

        # add the ball to ball group and set the paddle group
        ball_group.add(self)
        self.paddle_group: Group = paddle_group

        self.move_side: bool = True

    def update(self) -> None:
        """
        Check for collisions and update the position of the ball.
        """
        self.check_collisions(self.paddle_group)

        self.x += self.v_x
        self.y += self.v_y

        self.rect.x = self.x
        self.rect.y = self.y

    def check_collisions(self, paddle_group: Group) -> None:
        """
        Check for collision with the paddles and walls.

        :param paddle_group: a sprite group containing the paddles.
        """
        # paddles
        if pygame.sprite.spritecollide(self, paddle_group, False):
            if pygame.sprite.spritecollide(self, paddle_group, False,
                                           pygame.sprite.collide_mask):
                # bounce
                print("collided")
                self.move_side = False
                paddle_hit = pygame.sprite.spritecollideany(self, paddle_group)

                ball_y: int = self.rect.centery
                paddle_y: int = paddle_hit.rect.centery

                rand = rng.randint(4,9)/10
                if paddle_hit.rect.x < self.settings.screen_width//2:
                    x_multiple = 1 + rand
                else:
                    x_multiple = -1 - rand

                if ball_y == paddle_y:
                    # middle
                    y_multiple = 0
                elif ball_y > paddle_y:
                    # bottom half
                    y_multiple = 1
                else:
                    # top half
                    y_multiple = -1

                self.v_x = x_multiple * self.speed
                self.v_y = y_multiple * self.speed

        # screen edges
        if self.rect.top <= self.screen_rect.top or \
            self.rect.bottom >= self.screen_rect.bottom:
            self.v_y *= -1
import pygame
from pygame import Surface, Rect, Mask
from pygame.sprite import Sprite, Group

from settings import GameSettings
from ball import Ball


class CPU(Sprite):
    """Represents an instance of the cpu paddle."""
    def __init__(self, settings: GameSettings, screen: Surface,
                 paddle_group: Group, ball: Ball):
        """
        Initializes a cpu paddle.

        :param settings:  a reference to the game settings.
        :param screen: a reference to the game screen.
        :param paddle_group: a group of sprites containing the paddles.
        Used for detecting collisions.
        :param ball: a reference to the ball object.
        """
        super().__init__()
        # make a reference to the settings and ball objects
        self.settings: GameSettings = settings
        self.ball: Ball = ball

        # set up the screen
        self.screen: Surface = screen
        self.screen_rect: Rect = self.screen.get_rect()

        # set the paddle height, width and speed based on the settings
        self.height: int = self.settings.paddle_height
        self.width: int = self.settings.paddle_width
        self.speed: int = self.settings.cpu_speed

        # the distance right-ward from the center that the ball must reach
        # before the ai starts trying to reach it
        self.detection_range: int = self.settings.detection_range

        # set up the surface where the paddle will be drawn
        self.surface: Surface = Surface((self.width, self.height))
        self.rect: Rect = self.surface.get_rect()

        # position the paddle in relation to the screen
        self.rect.centery = self.screen_rect.centery
        self.rect.right = self.settings.screen_width - 2*self.width

        # create a mask for detecting pixel perfect collisions with the ball
        self.mask: Mask = pygame.mask.from_surface(self.surface)

        # add the paddle object to the group
        paddle_group.add(self)

        # create a variable for handling smooth movement
        self.y: float = float(self.rect.y)


    def update(self) -> None:
        """
        Update the position of the paddle.
        """
        # try to math centery values with the ball when it is within
        # detection range
        ball_y: int = self.ball.rect.y
        ball_x: int = self.ball.rect.x

        if ball_x > self.settings.screen_width//2 + self.detection_range:
            if self.y > ball_y and self.rect.top > 0:
                self.y -= self.speed
            elif self.y < ball_y and self.rect.bottom < self.screen_rect.bottom:
                self.y += self.speed

        self.rect.centery = self.y


    def draw_paddle(self) -> None:
        """
        Draw the paddle to the screen.
        """
        pygame.draw.rect(self.screen, self.settings.fg_color, self.rect)
import pygame
from pygame import Surface, Rect, Mask
from pygame.sprite import Sprite, Group


class Ball(Sprite):
    """Represents an instance of the ball class."""
    def __init__(self, screen: Surface, ball_group: Group,
                 paddle_group: Group) -> None:
        """
        Initializes a ball object.

        :param screen: a reference to the game screen.
        :param ball_group: a sprite group containing the ball.
        Used for detecting collisions.
        :param paddle_group:  a sprite group containing the paddles.
        Used for detecting collisions.
        """
        super().__init__()

        # make a reference to the screen
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

        # create a mask to handle pixel-perfect collisions
        self.mask: Mask = pygame.mask.from_surface(self.image)

        self.move: bool = True

        # add the ball to ball group and set the paddle group
        ball_group.add(self)
        self.paddle_group: Group = paddle_group

    def update(self) -> None:
        """
        Check for collisions and update the position of the ball.
        """
        self.check_collisions(self.paddle_group)

        if self.move:
            self.x -= 0.1
            self.rect.x = self.x

    def check_collisions(self, paddle_group: Group) -> None:
        """
        Check for collision with the paddles and walls.

        :param paddle_group: a sprite group containing the paddles.
        """
        if pygame.sprite.spritecollide(self, paddle_group, False):
            if pygame.sprite.spritecollide(self, paddle_group, False,
                                           pygame.sprite.collide_mask):
                self.move = False


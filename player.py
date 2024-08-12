import pygame
from pygame import Surface, Rect, Mask
from pygame.sprite import Sprite, Group

from settings import GameSettings

class Player(Sprite):
    """Represents an instance of the player paddle."""
    def __init__(self, settings: GameSettings, screen: Surface,
                 paddle_group: Group) -> None:
        """
        Initializes a player paddle object.

        :param settings: the game settings.
        :param screen: a reference to the game screen.
        :param paddle_group: a sprite group containing the paddles.
        Used for detecting collisions.
        """
        super().__init__()
        # make a reference to the settings and screen
        self.settings: GameSettings = settings
        self.screen: Surface = screen

        # get the height, width and speed of the paddle from the settings
        self.height: int = self.settings.paddle_height
        self.width: int = self.settings.paddle_width
        self.speed: float = self.settings.paddle_speed

        # create a surface and rect for the paddle and position it relative
        # to the screen's rect
        self.surface: Surface = Surface((self.width, self.height))
        self.rect: Rect = self.surface.get_rect()
        self.screen_rect: Rect = self.screen.get_rect()

        self.rect.left = 2 * self.width
        self.rect.centery = self.screen_rect.centery

        # create a float variable to handle movement
        self.y: float = float(self.rect.centery)

        # create varibales to handle movement and ensure only one of the key
        # options for each direction is used for starting and stoping at a
        # time.
        self.moving_up: bool = False
        self.current_up_key = None
        self.moving_down: bool = False
        self.current_down_key = None

        # create a mask for detecting pixel-perfect collisions with the ball.
        self.mask: Mask = pygame.mask.from_surface(self.surface)

        # add the paddle object to the group
        paddle_group.add(self)


    def update(self) -> None:
        """
        Updates the position of the player.
        """
        if self.moving_up and self.rect.top > 0:
            self.y -= self.speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.speed

        self.rect.centery = self.y


    def draw_paddle(self) -> None:
        """
        Draws the player to the screen.
        """
        pygame.draw.rect(self.screen, self.settings.fg_color, self.rect)
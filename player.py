import pygame
from pygame import Surface, Rect, Mask
from pygame.sprite import Sprite, Group

from settings import GameSettings

class Player(Sprite):
    """Represents an instance of the player paddle."""
    def __init__(self, settings: GameSettings, screen: Surface, paddle_group: Group) -> None:
        """
        Initializes a player object.

        :param settings: the game settings.
        :param screen: a reference to the game screen.
        """
        super().__init__()

        self.settings: GameSettings = settings
        self.screen: Surface = screen

        self.height: int = self.settings.paddle_height
        self.width: int = self.settings.paddle_width
        self.speed: float = self.settings.paddle_speed

        self.surface: Surface = Surface((self.width, self.height))
        self.rect: Rect = self.surface.get_rect()
        self.screen_rect: Rect = self.screen.get_rect()

        self.rect.left = 2 * self.width
        self.rect.centery = self.screen_rect.centery

        self.y: float = float(self.rect.centery)

        self.moving_up: bool = False
        self.current_up_key = None
        self.moving_down: bool = False
        self.current_down_key = None

        self.mask: Mask = pygame.mask.from_surface(self.surface)

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
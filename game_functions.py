import sys
import pygame
from pygame import Surface

from settings import GameSettings


def check_events() -> None:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(settings: GameSettings, screen: Surface) -> None:
    screen.fill(settings.bg_color)
    pygame.display.flip()
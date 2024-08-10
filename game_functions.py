import sys
import pygame
from pygame import Surface

from settings import GameSettings
from player import Player


def check_events() -> None:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(settings: GameSettings, screen: Surface, player: Player) -> None:
    screen.fill(settings.bg_color)
    player.draw_player()
    pygame.display.flip()
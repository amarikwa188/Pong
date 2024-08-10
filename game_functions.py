import sys
import pygame
from pygame import Surface
from pygame.event import Event

from settings import GameSettings
from player import Player


def check_events() -> None:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            pass
        elif event.type == pygame.KEYUP:
            pass


def check_keydown_events(event: Event) -> None:
    pass

def check_keyup_events(event: Event) -> None:
    pass


def update_screen(settings: GameSettings, screen: Surface, player: Player) -> None:
    screen.fill(settings.bg_color)
    player.draw_player()
    pygame.display.flip()
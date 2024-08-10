import sys
import pygame
from pygame import Surface
from pygame.event import Event

from settings import GameSettings
from player import Player


def check_events(player: Player) -> None:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, player)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, player)


def check_keydown_events(event: Event, player: Player) -> None:
    if event.key == pygame.K_UP:
        player.moving_up = True
    elif event.key == pygame.K_DOWN:
        player.moving_down = True


def check_keyup_events(event: Event, player: Player) -> None:
    if event.key == pygame.K_UP:
        player.moving_up = False
    elif event.key == pygame.K_DOWN:
        player.moving_down = False


def update_screen(settings: GameSettings, screen: Surface, player: Player) -> None:
    screen.fill(settings.bg_color)
    player.draw_player()
    pygame.display.flip()
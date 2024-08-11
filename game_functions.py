import sys
import pygame
from pygame import Surface
from pygame.event import Event

from settings import GameSettings
from ui_manager import UIHandler
from player import Player


def check_events(player: Player, ui_handler: UIHandler) -> None:
    """
    Handles user input.

    :param player: a reference to the player object.
    """
    for event in pygame.event.get():
        ui_handler.manager.process_events(event)

        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, player, ui_handler)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, player)


def check_keydown_events(event: Event, player: Player, ui_handler: UIHandler) -> None:
    """
    Handles key presses.

    :param event: the given event instance.
    :param player: a reference to the player object.
    """
    if event.key in (pygame.K_UP, pygame.K_w) and \
        not player.current_up_key:
        player.moving_up = True
        player.current_up_key = event.key
    elif event.key in (pygame.K_DOWN, pygame.K_s) and \
        not player.current_down_key:
        player.moving_down = True
        player.current_down_key = event.key
    elif event.key == pygame.K_SPACE:
        ui_handler.player_score += 1


def check_keyup_events(event: Event, player: Player) -> None:
    """
    Handles key releases.

    :param event: the given event instance.
    :param player: a reference to the player object.
    """
    if event.key in (pygame.K_UP, pygame.K_w) and \
        event.key == player.current_up_key:
        player.moving_up = False
        player.current_up_key = None
    elif event.key in (pygame.K_DOWN, pygame.K_s) and \
        event.key == player.current_down_key:
        player.moving_down = False
        player.current_down_key = None


def update_screen(settings: GameSettings, screen: Surface,
                  ui_handler: UIHandler, player: Player) -> None:
    """
    Updates the screen.

    :param settings: the game settings.
    :param screen: the screen.
    :param player: a reference to the player object.
    """
    screen.fill(settings.bg_color)
    ui_handler.manager.draw_ui(screen)
    ui_handler.draw_ui()
    player.draw_player()
    pygame.display.flip()
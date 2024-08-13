import sys
import pygame
from pygame import Surface
from pygame.sprite import Group
from pygame.event import Event

from settings import GameSettings
from ui_manager import UIHandler
from scene_manager import SceneManager
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
            check_keydown_events(event, player)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, player)


def check_keydown_events(event: Event, player: Player) -> None:
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


def check_game_state(ui_handler: UIHandler, scene_manager: SceneManager) -> None:
    player_score: int = ui_handler.player_score
    cpu_score: int =  ui_handler.cpu_score

    if player_score >= 10 or cpu_score >= 10:
        scene_manager.game_screen_active = False
        scene_manager.end_screen_active = True


def update_screen(settings: GameSettings, screen: Surface,
                  ui_handler: UIHandler, scene_manager: SceneManager,
                  ball_group: Group, paddle_group: Group) -> None:
    """
    Updates the screen.

    :param settings: the game settings.
    :param screen: the screen.
    :param ui_handler: a reference to the ui_handler.
    :param ball_group: a sprite group containing the ball.
    :param paddle_group:  a sprite group containing the paddles.
    """
    screen.fill(settings.bg_color)

    ui_handler.manager.draw_ui(screen)
    ui_handler.draw_ui()

    if scene_manager.game_screen_active:
        for paddle in paddle_group.sprites():
            paddle.draw_paddle()
        ball_group.draw(screen)
    
    pygame.display.flip()
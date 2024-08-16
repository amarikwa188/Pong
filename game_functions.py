import sys
import pygame
from pygame import Surface
from pygame.sprite import Group
from pygame.event import Event

from settings import GameSettings
from ui_manager import UIHandler
from scene_manager import SceneManager
from audio_handler import AudioHandler

from player import Player
from cpu import CPU


def check_events(screen: Surface, player: Player, cpu: CPU,
                 scene: SceneManager, ui_handler: UIHandler,
                 audio: AudioHandler) -> None:
    """
    Handles user input.

    :param screen: a reference to the game screen.
    :param player: a reference to the player object.
    :param cpu: a reference to the cpu object.
    :param scene: a reference to the game screen.
    :param ui_handler: a reference to the ui handler.
    :param audio: a reference to the audio handler.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, screen, player, cpu, scene,
                                 ui_handler, audio)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, player)
        elif event.type == ui_handler.BLINKEVENT:
            if scene.end_screen_active:
                ui_handler.play_current = next(ui_handler.play_blinker)
            elif scene.start_screen_active:
                ui_handler.starter_current = next(ui_handler.starter_blinker)


def check_keydown_events(event: Event, screen: Surface, player: Player,
                         cpu: CPU, scene: SceneManager,
                         ui_handler: UIHandler, audio: AudioHandler) -> None:
    """
    Handles key presses.

    :param event: the given event instance.
    :param screen: a reference to the game screen.
    :param player: a reference to the player object.
    :param cpu: a reference to the cpu object.
    :param scene: a reference to the scene manager.
    :param ui_handler: a reference to the ui handler.
    :param audio: a reference to the audio handler.
    """
    if event.key in (pygame.K_UP, pygame.K_w) and \
        not player.current_up_key and not scene.game_paused:
        player.moving_up = True
        player.current_up_key = event.key
    elif event.key in (pygame.K_DOWN, pygame.K_s) and \
        not player.current_down_key and not scene.game_paused:
        player.moving_down = True
        player.current_down_key = event.key
    elif event.key == pygame.K_p and not scene.game_screen_active:
        audio.action_sound.play()
        reset_game(screen, scene, ui_handler, player, cpu)
        pygame.time.set_timer(ui_handler.BLINKEVENT, 0)
    elif event.key == pygame.K_ESCAPE:
        if scene.game_screen_active:
            audio.action_sound.play()
            scene.game_paused = not scene.game_paused
        

def reset_game(screen: Surface, scene: SceneManager, ui_handler: UIHandler,
               player: Player, cpu: CPU) -> None:
    """
    Start a new game.

    :param screen: a reference to the game screen.
    :param scene: a reference to the screen manager.
    :param ui_handler: a reference to the ui_handler.
    :param player: the player object.
    :param cpu: the cpu object. 
    """
    scene.game_screen_active = True
    scene.end_screen_active = False
    scene.start_screen_active = False 

    # reset game stats
    ui_handler.cpu_score = 0
    ui_handler.player_score = 0
    player.rect.centery = cpu.rect.centery = screen.get_rect().centery
    player.y = cpu.y = float(player.rect.centery)


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


def check_game_state(settings: GameSettings, ui_handler: UIHandler, 
                     scene: SceneManager) -> None:
    """
    End the game when one player wins.

    :param settings: a reference to the game settings.
    :param ui_handler: a reference to the ui_handler.
    :param scene: a reference to the scene manager.
    """
    player_score: int = ui_handler.player_score
    cpu_score: int =  ui_handler.cpu_score

    win: int = settings.win_score

    if (player_score >= win or cpu_score >= win) and scene.game_screen_active:
        scene.game_screen_active = False
        scene.end_screen_active = True
        pygame.time.set_timer(ui_handler.BLINKEVENT, 500)


def update_screen(settings: GameSettings, screen: Surface,
                  ui_handler: UIHandler, scene: SceneManager,
                  ball_group: Group, paddle_group: Group) -> None:
    """
    Updates the screen.

    :param settings: the game settings.
    :param screen: the screen.
    :param ui_handler: a reference to the ui_handler.
    :param scene: a reference to the scene manager.
    :param ball_group: a sprite group containing the ball.
    :param paddle_group: a sprite group containing the paddles.
    """
    screen.fill(settings.bg_color)

    ui_handler.draw_ui()

    if scene.game_screen_active:
        for paddle in paddle_group.sprites():
            paddle.draw_paddle()
        ball_group.draw(screen)
    
    pygame.display.flip()
import pygame
from pygame import Surface
from pygame.sprite import Group
from pygame.time import Clock

from settings import GameSettings
from ui_manager import UIHandler
from audio_handler import AudioHandler

import game_functions as gf
from scene_manager import SceneManager

from player import Player
from cpu import CPU
from ball import Ball


def run_game() -> None:
    """
    Run the game.
    """
    # initialize the pygame window
    pygame.init()
    pygame.display.set_caption("PONG")

    #create an instance of the settings class
    settings: GameSettings = GameSettings()

    # create and setup the screen surface, clock, and ui handler 
    screen: Surface = pygame.display.set_mode((settings.screen_width,
                                               settings.screen_height))
    clock: Clock = pygame.time.Clock()
    scene: SceneManager = SceneManager(settings)
    ui_handler: UIHandler = UIHandler(settings, screen, scene)
    audio_handler: AudioHandler = AudioHandler()
    
    # initialize the groups and ball object
    paddle_group: Group = Group()
    ball_group: Group = Group()
    ball: Ball = Ball(settings, screen, ball_group, paddle_group, ui_handler,
                      audio_handler)

    # initialize the cpu and player paddles
    player: Player = Player(settings,  screen, paddle_group)
    cpu: CPU = CPU(settings, screen, paddle_group, ball)

    # start the game loop
    while True:
        clock.tick(640)
        
        gf.check_events(screen, player, cpu, scene, ui_handler,
                        audio_handler)
        gf.check_game_state(settings, ui_handler, scene)

        if scene.game_screen_active and not scene.game_paused:
            player.update()
            cpu.update()
            ball.update()

        gf.update_screen(settings, screen, ui_handler, scene, ball_group,
                         paddle_group)


if __name__ == "__main__":
    run_game()
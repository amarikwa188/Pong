import pygame
from pygame import Surface
from pygame.sprite import Group
from pygame.time import Clock

from settings import GameSettings
from ui_manager import UIHandler

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
    
    # initialize the groups and ball object
    paddle_group: Group = Group()
    ball_group: Group = Group()
    ball: Ball = Ball(settings, screen, ball_group, paddle_group, ui_handler)

    # initialize the cpu and player paddles
    player: Player = Player(settings,  screen, paddle_group)
    cpu: CPU = CPU(settings, screen, paddle_group, ball)

    # start the game loop
    while True:
        time_delta: float = clock.tick(480)/1000
        gf.check_events(player, ui_handler)
        gf.check_game_state(ui_handler, scene)
        if scene.game_screen_active:
            player.update()
            cpu.update()
            ball.update()

        ui_handler.manager.update(time_delta)
        gf.update_screen(settings, screen, ui_handler, scene, ball_group,
                         paddle_group)


if __name__ == "__main__":
    run_game()
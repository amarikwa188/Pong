import pygame
from pygame import Surface
from pygame.sprite import Group
from pygame.time import Clock

from settings import GameSettings
from ui_manager import UIHandler
import game_functions as gf
from player import Player
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
    ui_handler: UIHandler = UIHandler(settings, screen)
    
    # initialize a player paddle
    paddle_group: Group = Group()
    player: Player = Player(settings, screen, paddle_group)

    # initialize the ball group and ball object
    ball_group: Group = Group()
    ball: Ball = Ball(screen, ball_group, paddle_group)

    # the game loop
    while True:
        time_delta: float = clock.tick(360)/1000

        gf.check_events(player, ui_handler)
        player.update()
        ball.update()
        ui_handler.manager.update(time_delta)
        gf.update_screen(settings, screen, ui_handler, player, ball_group, paddle_group)


if __name__ == "__main__":
    run_game()
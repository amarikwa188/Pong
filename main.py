import pygame
from pygame import Surface

from settings import GameSettings
import game_functions as gf
from player import Player


def run_game() -> None:
    # initialize the pygame window
    pygame.init()
    pygame.display.set_caption("PONG")

    #create an instance of the settings class
    settings: GameSettings = GameSettings()

    # create and setup the screen surface 
    screen: Surface = pygame.display.set_mode((settings.screen_width,
                                               settings.screen_height))
    
    # initialize a player paddle
    player: Player = Player(settings, screen)

    # the game loop
    while True:
        gf.check_events()
        gf.update_screen(settings, screen, player)


if __name__ == "__main__":
    run_game()
import pygame
from pygame import Surface

from settings import GameSettings

def run_game() -> None:
    # initialize the pygame window
    pygame.init()
    pygame.display.set_caption("PONG")

    #create an instance of the settings class
    settings: GameSettings = GameSettings()

    # create and setup the screen surface 
    screen: Surface = pygame.display.set_mode((settings.screen_height,\
                                               settings.screen_width))
    
    # the game loop
    while True:
        pass


if __name__ == "__main__":
    run_game()
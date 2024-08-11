import pygame
from pygame import Surface, Rect

import pygame_gui
from pygame_gui.ui_manager import UIManager
from pygame_gui.elements import UIButton, UILabel

from settings import GameSettings

class UIHandler:
    def __init__(self, settings: GameSettings, screen: Surface) -> None:
        self.screen: Surface = screen
        self.screen_rect: Rect = self.screen.get_rect()

        self.manager: UIManager = UIManager((settings.screen_width,
                                             settings.screen_height)) 


    def draw_center_line(self) -> None:
        pygame.draw.line(self.screen, (255,255,255), (275, 0), (275, 350), 3)

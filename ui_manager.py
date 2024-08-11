import math

import pygame
from pygame import Surface, Rect

import pygame_gui
from pygame_gui.ui_manager import UIManager
from pygame_gui.elements import UIButton, UILabel

from settings import GameSettings

class UIHandler:
    def __init__(self, settings: GameSettings, screen: Surface) -> None:
        self.settings: GameSettings = settings
        self.screen: Surface = screen
        self.screen_rect: Rect = self.screen.get_rect()

        self.manager: UIManager = UIManager((settings.screen_width,
                                             settings.screen_height)) 


    def draw_center_line(self) -> None:
        line_color: tuple[int,int,int] = (255,255,255)
        line_width: int = 3
        total_height: int = self.settings.screen_height
        x_pos: int = self.settings.screen_width // 2
        segment_length: int = 10
        segment_count: int = math.ceil(total_height/(2 * segment_length))

        for i in range(segment_count):
            y_start: int = (segment_length * 2) * i
            y_end: int = (segment_length * 2) * i + segment_length
            pygame.draw.line(self.screen, line_color, (x_pos, y_start),
                             (x_pos, y_end), line_width)


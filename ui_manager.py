import math

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from pygame_gui.ui_manager import UIManager

from settings import GameSettings


class UIHandler:
    """Represents an instance of the UI Handler."""
    def __init__(self, settings: GameSettings, screen: Surface) -> None:
        """
        Initializes the ui handler.

        :param settings: a reference to the game's settings.
        :param screen: a reference to the game screen.
        """
        # make a reference to the game's setting
        self.settings: GameSettings = settings

        # set up the screen
        self.screen: Surface = screen
        self.screen_rect: Rect = self.screen.get_rect()

        # set up the ui manager
        self.manager: UIManager = UIManager((settings.screen_width,
                                             settings.screen_height)) 
        
        # set the font for displaying scores
        self.score_font: Font = pygame.font.Font("fonts/ARCADE.TTF", 400)

        # set the scores
        self.player_score: int = 0
        self.cpu_score: int = 0

        # pygame.mouse.set_visible(False)


    def draw_ui(self):
        """
        Draw all the custom ui elements to the screen.
        """
        self.draw_center_line()
        self.display_player_score()
        self.display_cpu_score()


    def draw_center_line(self) -> None:
        """
        Draw the center line to the game screen.
        """
        # set the details of the line
        line_color: tuple[int,int,int] = self.settings.fg_color
        line_width: int = 2

        # calculate the amount of line segments needed and their length
        total_height: int = self.settings.screen_height
        x_pos: int = self.settings.screen_width // 2
        segment_length: int = 10
        segment_count: int = math.ceil(total_height/(2 * segment_length))

        # draw each line segment to the screen
        for i in range(segment_count):
            y_start: int = (segment_length * 2) * i
            y_end: int = (segment_length * 2) * i + segment_length
            pygame.draw.line(self.screen, line_color, (x_pos, y_start),
                             (x_pos, y_end), line_width)
    

    def display_player_score(self) -> None:
        """
        Display the player score.
        """
        # Render the text to a surface with the approporiate font and color
        image: Surface = self.score_font.render(f"{self.player_score}", 
                                                True, self.settings.fg_color)
        # make the text translucent
        image.set_alpha(45)
        
        # position the text
        image_rect: Rect = image.get_rect()
        image_rect.centery = self.settings.screen_height // 2 + 50
        image_rect.centerx = 155

        # draw the text surface to the screen
        self.screen.blit(image, image_rect)
        

    def display_cpu_score(self) -> None:
        """
        Display the cpu score.
        """
        # Render the text to a surface with the approporiate font and color
        image: Surface = self.score_font.render(f"{self.cpu_score}",
                                                True, self.settings.fg_color)
        # make the text translucent
        image.set_alpha(45)

        # position the text
        image_rect: Rect = image.get_rect()
        image_rect.centery = self.settings.screen_height // 2 + 50
        image_rect.centerx = 425

        # draw the text surface to the screen
        self.screen.blit(image, image_rect)
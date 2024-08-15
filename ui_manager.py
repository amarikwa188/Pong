import math
from itertools import cycle

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from settings import GameSettings
from scene_manager import SceneManager


class UIHandler:
    """Represents an instance of the UI Handler."""
    def __init__(self, settings: GameSettings, screen: Surface,
                 scene_manager: SceneManager) -> None:
        """
        Initializes the ui handler.

        :param settings: a reference to the game's settings.
        :param screen: a reference to the game screen.
        """
        # make a reference to the game's setting and scene manager
        self.settings: GameSettings = settings
        self.scene_manager: SceneManager = scene_manager

        # set up the screen
        self.screen: Surface = screen
        self.screen_rect: Rect = self.screen.get_rect()
        
        # set the font for displaying scores
        self.score_font: Font = pygame.font.Font("fonts/ARCADE.TTF", 400)
        self.final_font: Font = pygame.font.Font("fonts/ARCADE.TTF", 200)
        self.result_font: Font = pygame.font.Font("fonts/ARCADE.TTF", 70)
        self.play_again_font: Font = pygame.font.Font("fonts/ARCADE.TTF", 30)
        self.play_blinker: cycle = self.play_again_blinker()
        self.starter_blinker: cycle = self.start_blinker() 
        self.pause_font: Font = pygame.font.Font("fonts/ARCADE.TTF", 200)
        self.title_font: Font = pygame.font.Font("fonts/ARCADE.TTF", 200)

        # set the scores
        self.player_score: int = 0
        self.cpu_score: int = 0


    def draw_ui(self):
        """
        Draw all the custom ui elements to the screen.
        """
        if self.scene_manager.game_screen_active:
            if self.scene_manager.game_paused:
                self.draw_pause_screen()
            self.draw_game_screen()

        if self.scene_manager.end_screen_active:
            self.display_winner()
            self.screen.blit(next(self.play_blinker), self.play_again_rect)

        if self.scene_manager.start_screen_active:
            self.draw_title()
            self.screen.blit(next(self.starter_blinker), self.start_rect)
            
    
    def draw_game_screen(self) -> None:
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


    def display_winner(self) -> None:
        scores: Surface = self.final_font.render(f"{self.player_score:02d}-"
                                                 f"{self.cpu_score:02d}",True,
                                                 self.settings.fg_color)
        scores.set_alpha(200)

        scores_rect: Rect = scores.get_rect()
        scores_rect.centerx = self.screen_rect.centerx
        scores_rect.centery = 130

        self.screen.blit(scores, scores_rect)

        result_text: str = 'WIN' if self.player_score > self.cpu_score else 'LOSE'

        result: Surface = self.result_font.render(f"YOU {result_text}!", True, 
                                                  self.settings.fg_color)
        result.set_alpha(200)

        result_rect: Rect = result.get_rect()
        result_rect.centerx = self.screen_rect.centerx
        result_rect.centery = 220

        self.screen.blit(result, result_rect)

    def play_again_blinker(self) -> cycle:
        # display text saying 'Press P to play again'
        text: str = "Press P to play again..."
        image: Surface = self.play_again_font.render(text, True, 
                                                     self.settings.fg_color,
                                                     self.settings.bg_color)
        image.set_alpha(180)
        image_rect: Rect = image.get_rect()
        image_rect.centerx = self.screen_rect.centerx
        image_rect.centery = 290

        off_image: Surface = image.copy()
        off_image.set_alpha(50)

        self.play_again_rect: Rect = image_rect
        
        return cycle([image]*200 + [off_image]*200)
    

    def draw_pause_screen(self) -> None:
        self.screen.fill((100,100,100))
        text: str = "||"
        image: Surface = self.pause_font.render(text, True,
                                                self.settings.fg_color) 
        image_rect: Rect = image.get_rect()
        image_rect.centerx = self.screen_rect.centerx
        image_rect.centery = self.screen_rect.centery + 20

        self.screen.blit(image, image_rect)


    def draw_title(self) -> None:
        title: Surface = self.title_font.render("PONG", True,
                                                self.settings.fg_color,
                                                self.settings.bg_color)
        title_rect: Rect = title.get_rect()

        title_rect.centerx = self.screen_rect.centerx
        title_rect.centery = 170

        self.screen.blit(title, title_rect)

    def start_blinker(self) -> cycle:
        text: str = "Press P to play..."
        image: Surface = self.play_again_font.render(text, True,
                                                     self.settings.fg_color,
                                                     self.settings.bg_color)
        image.set_alpha(180)
        image_rect: Rect = image.get_rect()
        image_rect.centerx = self.screen_rect.centerx
        image_rect.centery = 250

        off_image: Surface = image.copy()
        off_image.set_alpha(50)

        self.start_rect: Rect = image_rect

        return cycle([image]*200 + [off_image]*200)
import pygame
from pygame import Surface, Rect
from pygame.font import Font

class Button:
    def __init__(self, screen: Surface, text: str, 
                 center: tuple[int,int]) -> None:
        self.screen: Surface = screen
        self.screen_rect: Rect = self.screen.get_rect()

        self.width, self.height = 100, 40
        self.button_color: tuple[int,int,int] = (255,255,255)
        self.text_color: tuple[int,int,int] = (0,0,0)

        self.button: Surface = Surface((self.width, self.height))
        self.rect: Rect = self.button.get_rect()
        self.rect.center = center

        self.font: Font = pygame.font.Font("fonts/ARCADE.TTF", 50)
        
        self.screen.fill(self.button_color, self.rect)
        self.render_text(text)


    def render_text(self, text: str) -> None:
        image: Surface = self.font.render(text, True, self.text_color,
                                          self.button_color)
        image_rect: Rect = image.get_rect()
        image_rect.center = self.rect.center

        self.button.blit(image, image_rect)

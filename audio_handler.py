import pygame
from pygame.mixer import Sound

class AudioHandler:
    def __init__(self) -> None:
        self.bounce_sound: Sound = Sound("audio_files/pong_sfx.wav")


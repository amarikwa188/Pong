import random as rng
import time

import pygame
from pygame import Surface, Rect, Mask
from pygame.sprite import Sprite, Group

from settings import GameSettings
from ui_manager import UIHandler
from audio_handler import AudioHandler


class Ball(Sprite):
    """Represents an instance of the ball class."""
    def __init__(self, settings: GameSettings, screen: Surface,
                 ball_group: Group, paddle_group: Group,
                 ui_handler: UIHandler, audio: AudioHandler) -> None:
        """
        Initializes a ball object.

        :param settings: a reference to the game settings.
        :param screen: a reference to the game screen.
        :param ball_group: a sprite group containing the ball.
        Used for detecting collisions.
        :param paddle_group:  a sprite group containing the paddles.
        Used for detecting collisions.
        :param ui_handler: a reference to the game ui handler.
        :param audio: a reference to the audio handler.
        """
        super().__init__()

        # make a reference to the settings, ui handler and audio handler
        self.settings: GameSettings = settings
        self.ui_handler: UIHandler = ui_handler
        self.audio: AudioHandler = audio

        # get screen data
        self.screen: Surface = screen
        self.screen_rect: Rect = self.screen.get_rect()

        # load the sprite image and position the surface
        self.image: Surface = pygame.image.load("sprites/ball.png")\
            .convert_alpha()
        self.rect: Rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

        # create float variables to handle smooth movement
        self.x: float = float(self.rect.x)
        self.y: float = float(self.rect.y)

        # handle bounce
        self.initial_speed: float = self.settings.ball_speed
        self.max_speed: float = self.initial_speed + 0.4
        self.speed: float = self.initial_speed
        self.v_x: float = self.speed
        self.v_y: float = 0.0

        # create a mask to handle pixel-perfect collisions
        self.mask: Mask = pygame.mask.from_surface(self.image)

        # add the ball to ball group and set the paddle group
        ball_group.add(self)
        self.paddle_group: Group = paddle_group

        # track when the bounce sound effect was last played
        self.last_played: float = time.time()


    def update(self) -> None:
        """
        Check for collisions and update the position of the ball.
        """
        # check for collisions
        self.check_collisions(self.paddle_group)

        # update position of the ball
        self.x += self.v_x
        self.y += self.v_y

        self.rect.x = self.x
        self.rect.y = self.y

        # check if the ball has gone of the screen
        self.out_of_bounds()


    def check_collisions(self, paddle_group: Group) -> None:
        """
        Check for collision with the paddles and walls.

        :param paddle_group: a sprite group containing the paddles.
        """
        # handle bouncing off paddles
        if pygame.sprite.spritecollide(self, paddle_group, False):
            if pygame.sprite.spritecollide(self, paddle_group, False,
                                           pygame.sprite.collide_mask):
                # play sfx without spam
                if time.time() - self.last_played > 0.05:
                    self.audio.bounce_sound.play()
                    self.last_played = time.time()

                # the paddle that was hit
                paddle_hit = pygame.sprite.spritecollideany(self, paddle_group)

               # get the center positions of the ball and the paddle on
               # the y-axis
                ball_y: int = self.rect.centery
                paddle_y: int = paddle_hit.rect.centery

                # add random floats to the multiples to increase angle variation
                randx = rng.randint(1,4)/10
                randy = rng.randint(1,4)/10

                # set the x-multiple based on which side of the screen
                # the  paddle is located, left -> player, right -> cpu
                player_hit: bool = paddle_hit.rect.x < self.settings.screen_width//2
                if player_hit:
                    x_multiple = 1 + randx
                else:
                    x_multiple = -1 - randx

                # set the angle based on where the paddle was hit
                if ball_y == paddle_y:
                    # middle -> ~ 0 degrees
                    y_multiple = 0
                    x_multiple = 1.8 if player_hit else -1.4
                elif ball_y > paddle_y:
                    # bottom half -> ~ -45 degrees
                    y_multiple = 1 + randy
                else:
                    # top half -> ~ 45 degrees
                    y_multiple = -1 - randy

                # set the x and y vectors based on the speed and angle 
                self.v_x = x_multiple * self.speed
                self.v_y = y_multiple * self.speed

                # increase speed
                if self.speed < self.max_speed:
                    self.speed += 0.05

        # handle bouncing off screen edges(top and bottom)
        if self.rect.top <= self.screen_rect.top or \
            self.rect.bottom >= self.screen_rect.bottom:
            # play sfx without spam
            if time.time() - self.last_played > 0.05:
                self.audio.bounce_sound.play()
                self.last_played = time.time()
            
            # invert y velocity
            self.v_y *= -1


    def out_of_bounds(self) -> None:
        """
        Reset the ball position when the ball goes out of bounds,
        while updating the score.
        """
        if self.rect.centerx <= self.screen_rect.x:
            # play sfx
            self.audio.point_sound.play()

            # increase score
            self.ui_handler.cpu_score += 1

            # reset movement vectors
            self.v_x = self.speed/2
            self.v_y = 0

            # reset ball position
            self.rect.centerx = self.screen_rect.centerx
            self.rect.centery = self.screen_rect.centery

            self.x = float(self.rect.x)
            self.y = float(self.rect.y)

            # reset speed
            self.speed = self.initial_speed

        elif self.rect.centerx >= self.settings.screen_width:
            # play sfx
            self.audio.point_sound.play()
             # increase score
            self.ui_handler.player_score += 1

            # reset movement vectors
            self.v_x = self.speed/2
            self.v_y = 0

            # reset ball position
            self.rect.centerx = self.screen_rect.centerx
            self.rect.centery = self.screen_rect.centery

            self.x = float(self.rect.x)
            self.y = float(self.rect.y)

            # reset speed
            self.speed = self.initial_speed

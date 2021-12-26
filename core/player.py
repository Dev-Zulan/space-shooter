import pygame

import os

from core.window import Window

class Player:
    def __init__(self, img, x, y, speed=2):
        self.sprite_img = img
        self.x = x
        self.y = y
        self.speed = speed

    def DrawSprite(self, window):
        window.blit(pygame.image.load(self.sprite_img), (self.x, self.y))
    
    def MoveSprite(self, direction):
        if direction == 1:
            self.y -= self.speed
        if direction == 2:
            self.y += self.speed
        if direction == 3:
            self.x -= self.speed
        if direction == 4:
            self.x += self.speed

Player = Player(os.path.join('assets', 'space_shooter.png'), 300-64, 450)
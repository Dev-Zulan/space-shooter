import os
from utils.colours import Colour

import pygame

from core.game import Game

class Window:
    def __init__(self, width: int, height: int, caption: str, background: str):
        self.width = width
        self.height = height
        self.caption = caption
        self.background = pygame.image.load(background)
        self.rect = self.background.get_rect()
        self.rect.left, self.rect.top = [0, 0]

        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption(self.caption)

    
    def GetWindow(self) -> None:
        return self.window
    
    def GetWindowResolution(self) -> tuple:
        return (self.width, self.height)

    def GetWindowCaption(self) -> str:
        return self.caption
    
    def DrawWindow(self):
        Window.window.fill(Colour.colour_RGB('black'))
        Window.window.blit(Window.background, Window.rect)
    
    def RefreshWindow(self):
        pygame.display.update()
    
    def SetWindowWidth(self, width):
        self.width = width
    
    def SetWindowHeight(self, height):
        self.height = height
    
    def SetWindowResolution(self, width, height):
        self.SetWindowWidth(width)
        self.SetWindowHeight(height)
    
    def SetWindowCaption(self, caption):
        self.caption = caption
    
    def SetWindowBackground(self, background):
        self.background = background

Window = Window(600, 900, Game.GetGameName(), os.path.join('assets', 'space_bg.png'))
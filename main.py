import pygame
from pygame.constants import *

from core.game import Game
from core.player import Player
from core.window import Window

def main():
    while Game.IsGameRunning():
        Game.clock.tick(Game.GetGameFPS())
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game.running = False

        KEY_UP = pygame.key.get_pressed()[K_UP] or pygame.key.get_pressed()[K_w]
        KEY_DOWN = pygame.key.get_pressed()[K_DOWN] or pygame.key.get_pressed()[K_s]
        KEY_LEFT = pygame.key.get_pressed()[K_LEFT] or pygame.key.get_pressed()[K_a]
        KEY_RIGHT = pygame.key.get_pressed()[K_RIGHT] or pygame.key.get_pressed()[K_d]
        
        if KEY_UP: Player.MoveSprite(1)
        if KEY_DOWN: Player.MoveSprite(2)
        if KEY_LEFT: Player.MoveSprite(3)
        if KEY_RIGHT: Player.MoveSprite(4)
        
        Window.DrawWindow()
        Player.DrawSprite()
        Window.RefreshWindow()
        
    pygame.QUIT

if __name__ == "__main__":
    main()
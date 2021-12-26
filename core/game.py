import pygame


class Game:
    def __init__(self, name: str, running: bool, fps: int = 120):
        self.name = name
        self.running = running
        self.fps = fps

        self.clock = pygame.time.Clock()
    
    def GetGameName(self) -> str:
        return self.name
    
    def IsGameRunning(self) -> bool:
        return self.running
    
    def GetGameFPS(self) -> int:
        return self.fps

Game = Game("Space Shooter", True)
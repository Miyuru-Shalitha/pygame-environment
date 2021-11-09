import pygame
from config import *


class Tree(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.sprite_name = "tree"
        self.image = pygame.image.load("images/game-assets/tree/tree.png").convert()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.width = width
        self.rect.height = height
        self.rect.x = x
        self.rect.y = y

    def update(self):
        pass

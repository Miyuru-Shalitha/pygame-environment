import random
import pygame
from config import *


class Leaf(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/leaf.png").convert()
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_SIZE[0])
        self.rect.y = 0

    def update(self):
        self.rect.y += 5

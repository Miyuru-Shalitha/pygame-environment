import random
import pygame
from config import *


class Leaf(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/leaf.png").convert()
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.image = pygame.transform.rotate(self.image, random.randint(0, 360))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_SIZE[0])
        self.rect.y = 0
        self.x_change = 0
        self.temp_x_val = 0
        self.x_val_reverse = False

    def update(self, wind_speed):
        self.rect.y += 5
        self.rect.x += self.x_change

        if self.x_val_reverse:
            self.temp_x_val += 0.1
            if self.temp_x_val > 5:
                self.x_val_reverse = True
        else:
            self.temp_x_val -= 0.1
            if self.temp_x_val < -5:
                self.x_val_reverse = True

        self.x_change = wind_speed + random.uniform(-1, 1) + self.temp_x_val

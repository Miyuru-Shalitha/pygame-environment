import random
import pygame
from config import *


class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.random_cloud = random.choice(["cloud-white.png", "cloud-grey.png"])
        self.random_value = random.uniform(0.5, 2.0)
        self.width = 100 * UNIT_X
        self.height = 100 * UNIT_Y

        self.image = pygame.image.load(f"images/game-assets/clouds/{self.random_cloud}").convert()
        self.image = pygame.transform.scale(self.image, (self.width * self.random_value, self.height * self.random_value))
        self.image = pygame.transform.flip(self.image, random.choice([True, False]), random.choice([True, False]))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_SIZE[0]
        self.x_change = self.random_value
        self.rect.y = self.x_change * 150 * UNIT_X

    def update(self):
        if self.rect.x <= 0:
            # This is the temporary solution for the bug that the cloud stuck in the left side.
            self.rect.x -= self.x_change * 5 * UNIT_X
        else:
            self.rect.x -= self.x_change * UNIT_X

        if self.rect.x < -self.rect.width:
            self.kill()

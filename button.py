import pygame
from config import *


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, func):
        super().__init__()
        self.func = func
        self.image = pygame.image.load("images/start-button.png").convert()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        # self.rect.centerx = x
        # self.rect.centery = y
        self.rect.x = x
        self.rect.y = y
        self.mouse_down_flag = 0

    def update(self, mouse_pos, is_clicked):
        if self.rect.collidepoint(mouse_pos) and is_clicked and (self.mouse_down_flag == 0):
            self.mouse_down_flag += 1
            self.func()
        elif not is_clicked:
            self.mouse_down_flag = 0

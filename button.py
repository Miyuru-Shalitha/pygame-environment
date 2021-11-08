import pygame
from config import *


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.image.load("images/start-button.png").convert()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.mouse_down_flag = 0

    def update(self, mouse_pos, is_clicked, func):
        if self.rect.collidepoint(mouse_pos) and is_clicked and (self.mouse_down_flag == 0):
            self.mouse_down_flag += 1
            func()
        elif not is_clicked:
            self.mouse_down_flag = 0

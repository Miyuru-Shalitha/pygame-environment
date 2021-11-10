import random
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
        self.x = 0

        self.image_copy = self.image.copy()
        self.rect_copy = self.image_copy.get_rect()

        self.image1 = pygame.image.load("images/game-assets/tree/tree-f-1.png").convert()
        self.image1 = pygame.transform.scale(self.image1, (width, height))
        self.image1.set_colorkey(WHITE)
        self.rect1 = self.image1.get_rect()
        self.x_change1 = 0
        self.is_x_change1_reversed = False

        self.image2 = pygame.image.load("images/game-assets/tree/tree-f-2.png").convert()
        self.image2 = pygame.transform.scale(self.image2, (width, height))
        self.image2.set_colorkey(WHITE)
        self.rect2 = self.image2.get_rect()
        self.x_change2 = 0
        self.is_x_change2_reversed = False

        self.image3 = pygame.image.load("images/game-assets/tree/tree-f-3.png").convert()
        self.image3 = pygame.transform.scale(self.image3, (width, height))
        self.image3.set_colorkey(WHITE)
        self.rect3 = self.image3.get_rect()
        self.x_change3 = 0
        self.is_x_change3_reversed = False

        self.image4 = pygame.image.load("images/game-assets/tree/tree-f-4.png").convert()
        self.image4 = pygame.transform.scale(self.image4, (width, height))
        self.image4.set_colorkey(WHITE)
        self.rect4 = self.image4.get_rect()
        self.x_change4 = 0
        self.is_x_change4_reversed = False

        self.image5 = pygame.image.load("images/game-assets/tree/tree-f-5.png").convert()
        self.image5 = pygame.transform.scale(self.image5, (width, height))
        self.image5.set_colorkey(WHITE)
        self.rect5 = self.image5.get_rect()
        self.x_change5 = 0
        self.is_x_change5_reversed = False

        self.image6 = pygame.image.load("images/game-assets/tree/tree-f-6.png").convert()
        self.image6 = pygame.transform.scale(self.image6, (width, height))
        self.image6.set_colorkey(WHITE)
        self.rect6 = self.image6.get_rect()
        self.x_change6 = 0
        self.is_x_change6_reversed = False

    def update(self):
        self.image.fill(SKY_COLOR)
        self.image.blit(self.image_copy, self.rect_copy)

        # Image1
        self.image.blit(self.image1, self.rect1)
        self.rect1.x += self.x_change1 * UNIT_X

        if self.is_x_change1_reversed:
            self.x_change1 -= random.uniform(0.0, 0.1)
            if self.x_change1 < -1.5:
                self.is_x_change1_reversed = False
        else:
            self.x_change1 += random.uniform(0.0, 0.1)
            if self.x_change1 > 1.5:
                self.is_x_change1_reversed = True

        # Image2
        self.image.blit(self.image2, self.rect2)
        self.rect2.x += self.x_change2 * UNIT_X

        if self.is_x_change2_reversed:
            self.x_change2 -= random.uniform(0.0, 0.1)
            if self.x_change2 < -1.5:
                self.is_x_change2_reversed = False
        else:
            self.x_change2 += random.uniform(0.0, 0.1)
            if self.x_change2 > 1.5:
                self.is_x_change2_reversed = True

            # Image3
            self.image.blit(self.image3, self.rect3)
            self.rect3.x += self.x_change3 * UNIT_X

            if self.is_x_change3_reversed:
                self.x_change3 -= random.uniform(0.0, 0.1)
                if self.x_change3 < -1.5:
                    self.is_x_change3_reversed = False
            else:
                self.x_change3 += random.uniform(0.0, 0.1)
                if self.x_change3 > 1.5:
                    self.is_x_change3_reversed = True

        # Image4
        self.image.blit(self.image4, self.rect4)
        self.rect4.x += self.x_change4 * UNIT_X

        if self.is_x_change4_reversed:
            self.x_change4 -= random.uniform(0.0, 0.1)
            if self.x_change4 < -1.5:
                self.is_x_change4_reversed = False
        else:
            self.x_change4 += random.uniform(0.0, 0.1)
            if self.x_change4 > 1.5:
                self.is_x_change4_reversed = True

        # Image5
        self.image.blit(self.image5, self.rect5)
        self.rect5.x += self.x_change5 * UNIT_X

        if self.is_x_change5_reversed:
            self.x_change5 -= random.uniform(0.0, 0.1)
            if self.x_change5 < -1.5:
                self.is_x_change5_reversed = False
        else:
            self.x_change5 += random.uniform(0.0, 0.1)
            if self.x_change5 > 1.5:
                self.is_x_change5_reversed = True

        # Image6
        self.image.blit(self.image6, self.rect6)
        self.rect6.x += self.x_change6 * UNIT_X

        if self.is_x_change6_reversed:
            self.x_change6 -= random.uniform(0.0, 0.1)
            if self.x_change6 < -1.5:
                self.is_x_change6_reversed = False
        else:
            self.x_change6 += random.uniform(0.0, 0.1)
            if self.x_change6 > 1.5:
                self.is_x_change6_reversed = True

import random
import pygame
from config import *
from game_physics import ColliderMixin


class Leaf(pygame.sprite.Sprite, ColliderMixin):
    def __init__(self, outer_blocks):
        super().__init__()
        super(pygame.sprite.Sprite, self).__init__(self, outer_blocks)
        self.image = pygame.image.load("images/leaf.png").convert()
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.image = pygame.transform.rotate(self.image, random.randint(0, 360))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(-(SCREEN_SIZE[0] // 2), (SCREEN_SIZE[0] + (SCREEN_SIZE[0] // 2)))
        self.rect.y = 0
        self.x_change = 0
        self.temp_x_val = 0
        self.x_val_reverse = False
        self.can_remove_counter = 0

    def update(self, delta_time, wind_speed, leaves):
        collisions = self.apply_collisions()
        if collisions["bottom_collide"]:
            self.apply_x_change(delta_time, wind_speed, 0.1)
            self.can_remove_counter += 1

            if self.can_remove_counter > 100:
                leaves.remove(self)
            return

        self.apply_x_change(delta_time, wind_speed, 1)

    def apply_x_change(self, delta_time, wind_speed, control_x_change):
        self.rect.y += 400 * delta_time
        self.rect.x += self.x_change * delta_time * control_x_change

        if self.x_val_reverse:
            self.temp_x_val += 5
            if self.temp_x_val > 500:
                self.x_val_reverse = True
        else:
            self.temp_x_val -= 5
            if self.temp_x_val < -500:
                self.x_val_reverse = True

        self.x_change = wind_speed + random.uniform(-100, 100) + self.temp_x_val

import pygame


class Grass(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.image.load("images/game-assets/blocks/grass-side.png").convert()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x * width
        self.rect.y = y * height

    def update(self):
        pass

import pygame


class GravityMixin:
    pass


class ColliderMixin:
    def __init__(self, obj, blocks):
        self.obj = obj
        self.blocks = blocks

    def apply_collisions(self):
        bottom_collide = False

        for block in self.blocks:
            if self.obj.rect.colliderect(block):
                if self.obj.rect.bottom > block.rect.top:
                    self.obj.rect.bottom = block.rect.top
                    bottom_collide = True

        return {"bottom_collide": bottom_collide}

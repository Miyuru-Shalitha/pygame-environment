import sys
import random
import pygame
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE, MOUSEBUTTONDOWN, MOUSEBUTTONUP
from config import *
from button import Button
from grass import Grass
from dirt import Dirt
from leaf import Leaf


class Game:
    def __init__(self):
        pygame.init()
        # pygame.font.init()
        self.clock = pygame.time.Clock()
        self.screen_size = SCREEN_SIZE
        self.screen = pygame.display.set_mode(self.screen_size)
        # self.font = pygame.font.SysFont("fonts/PermanentMarker-Reguler.ttf", 32)
        self.menu_running = False
        self.game_running = False

        self.show_menu()

    def show_menu(self):
        self.game_running = False
        self.menu_running = True
        click = False

        start_button = Button(SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2, 150, 75)

        buttons = pygame.sprite.Group()
        buttons.add(start_button)

        while self.menu_running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.menu_running = False
                    pygame.quit()
                    sys.exit()

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.menu_running = False
                        pygame.quit()
                        sys.exit()

                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

                if event.type == MOUSEBUTTONUP:
                    if event.button == 1:
                        click = False

            self.screen.fill(BLACK)

            mouse_x, mouse_y = pygame.mouse.get_pos()

            for button in buttons:
                button.update((mouse_x, mouse_y), click, self.start)
                self.screen.blit(button.image, button.rect)

            pygame.display.flip()
            self.clock.tick(FPS)

    def start(self):
        self.menu_running = False
        self.game_running = True

        spawn_leaf_event = pygame.USEREVENT + 1

        outer_blocks = pygame.sprite.Group()
        inner_blocks = pygame.sprite.Group()
        leaves = []

        with open("map.txt", "r") as map_file:
            data = map_file.read()
            data = data.split("\n")

            for i, tiles in enumerate(data):
                for j, tile in enumerate(tiles):
                    if tile == "G":
                        grass_block = Grass(j, i, TILE_SIZE[0], TILE_SIZE[1])
                        outer_blocks.add(grass_block)
                    elif tile == "D":
                        dirt_block = Dirt(j, i, TILE_SIZE[0], TILE_SIZE[1])
                        inner_blocks.add(dirt_block)

        all_sprites = pygame.sprite.Group()
        all_sprites.add(inner_blocks, outer_blocks)

        pygame.time.set_timer(spawn_leaf_event, 300)

        while self.game_running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.game_running = False
                    pygame.quit()
                    sys.exit()

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.game_running = False
                        self.show_menu()

                if event.type == spawn_leaf_event:
                    leaf = Leaf()
                    leaves.append(leaf)

            self.screen.fill(BLACK)

            for entity in all_sprites:
                entity.update()
                self.screen.blit(entity.image, entity.rect)

            print(len(leaves))

            for leaf in leaves:
                leaf.update()
                self.screen.blit(leaf.image, leaf.rect)

                if leaf.rect.y > SCREEN_SIZE[1]:
                    leaves.remove(leaf)

            pygame.display.flip()
            self.clock.tick(FPS)

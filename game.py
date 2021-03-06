import sys
import random
import json
import math
import pygame
from functools import wraps
from pygame.locals import QUIT, KEYDOWN, KEYUP, K_ESCAPE, MOUSEBUTTONDOWN, MOUSEBUTTONUP, K_s, K_g, K_d, K_t
from config import *
from button import Button
from grass import Grass
from dirt import Dirt
from leaf import Leaf
from tree import Tree
from cloud import Cloud


class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.clock = pygame.time.Clock()
        self.screen_size = SCREEN_SIZE
        self.screen = pygame.display.set_mode(self.screen_size)
        self.font = pygame.font.SysFont("fonts/PermanentMarker-Reguler.ttf", 32)
        self.menu_running = False
        self.game_running = False

        self.show_menu()

    def show_menu(self):
        self.game_running = False
        self.menu_running = True
        click = False

        start_button = Button(x=(SCREEN_SIZE[0] // 2) - (100 * UNIT_X), y=((SCREEN_SIZE[1] // 2) - 50 * UNIT_Y),
                              width=(200 * UNIT_X),
                              height=(100 * UNIT_Y), func=self.start)
        level_editor_button = Button(x=200 * UNIT_X, y=200 * UNIT_Y, width=(200 * UNIT_X), height=(100 * UNIT_Y),
                                     func=self.show_level_editor)

        buttons = pygame.sprite.Group()
        buttons.add(start_button, level_editor_button)

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
                button.update((mouse_x, mouse_y), click)
                self.screen.blit(button.image, button.rect)

            pygame.display.flip()
            self.clock.tick(FPS)

    def start(self, level_editor_func=None):
        self.menu_running = False
        self.game_running = True

        spawn_leaf_event = pygame.USEREVENT + 1
        spawn_cloud_event = pygame.USEREVENT + 2

        outer_blocks = pygame.sprite.Group()
        inner_blocks = pygame.sprite.Group()
        background_sprites = pygame.sprite.Group()
        cloud_sprites = pygame.sprite.Group()
        leaves = []

        with open("background.json", "r") as background_file:
            data = json.load(background_file)

            for obj in data:
                if obj["sprite_name"] == "tree":
                    sprite = Tree(x=obj["x_coord"] * UNIT_X, y=obj["y_coord"] * UNIT_Y, width=obj["width"] * UNIT_X,
                                  height=obj["height"] * UNIT_Y)
                    background_sprites.add(sprite)

        with open("map.txt", "r") as map_file:
            data = map_file.read()
            data = data.split("\n")

            for i, tiles in enumerate(data):
                for j, tile in enumerate(tiles):
                    if tile == "G":
                        grass_block = Grass(x=j, y=i, width=TILE_SIZE[0], height=TILE_SIZE[1])
                        outer_blocks.add(grass_block)
                    elif tile == "D":
                        dirt_block = Dirt(x=j, y=i, width=TILE_SIZE[0], height=TILE_SIZE[1])
                        inner_blocks.add(dirt_block)

        all_sprites = pygame.sprite.Group()
        all_sprites.add(background_sprites, inner_blocks, outer_blocks)

        pygame.time.set_timer(spawn_leaf_event, 300)
        pygame.time.set_timer(spawn_cloud_event, 2000)

        wind_speed = 0
        reversed_wind = False

        # t1 = pygame.time.get_ticks()

        mouse_clicks = {
            "left": False,
            "right": False
        }

        key_downs = {
            "s": False,
            "t": False
        }

        while self.game_running:
            # if mouse_clicks["left"]:
            #     mouse_clicks["left"] = False
            #
            # if mouse_clicks["right"]:
            #     mouse_clicks["right"] = False

            if key_downs["s"]:
                key_downs["s"] = False

            if key_downs["t"]:
                key_downs["t"] = False

            # t2 = pygame.time.get_ticks()
            # delta_time = (t2 - t1) / 10
            # t1 = t2
            # print("delta time 1", delta_time)
            # print(f"delta time 2 {self.clock.get_time() / 10}")

            delta_time = self.clock.get_time() / 1000

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.game_running = False
                    pygame.quit()
                    sys.exit()

                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.game_running = False
                        self.show_menu()
                    if event.key == K_s:
                        key_downs["s"] = True
                    if event.key == K_t:
                        key_downs["t"] = True

                if event.type == KEYUP:
                    if event.type == K_s:
                        key_downs["s"] = False
                    if event.type == K_t:
                        key_downs["t"] = False

                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_clicks["left"] = True
                    if event.button == 3:
                        mouse_clicks["right"] = True

                if event.type == MOUSEBUTTONUP:
                    if event.button == 1:
                        mouse_clicks["left"] = False
                    if event.button == 3:
                        mouse_clicks["right"] = False

                if event.type == spawn_leaf_event:
                    leaf = Leaf(outer_blocks)
                    leaves.append(leaf)

                if event.type == spawn_cloud_event:
                    cloud = Cloud()
                    cloud_sprites.add(cloud)

            self.screen.fill(SKY_COLOR)

            # FPS TEXT #########################################
            text_surface = self.font.render(f"FPS: {round(self.clock.get_fps())}", False, WHITE)
            self.screen.blit(text_surface, (10, 10))
            ####################################################

            for entity in all_sprites:
                entity.update()
                self.screen.blit(entity.image, entity.rect)

            for cloud_sprite in cloud_sprites:
                cloud_sprite.update(delta_time)
                self.screen.blit(cloud_sprite.image, cloud_sprite.rect)

            # print(len(leaves))
            if reversed_wind:
                wind_speed += 0.01
                if wind_speed > 10:
                    reversed_wind = False
            else:
                wind_speed -= 0.01
                if wind_speed < -10:
                    reversed_wind = True

            for leaf in leaves:
                leaf.update(delta_time, wind_speed, leaves)
                self.screen.blit(leaf.image, leaf.rect)

                if leaf.rect.y > SCREEN_SIZE[1]:
                    leaves.remove(leaf)

            # DEV only #############################
            if level_editor_func is not None:
                level_editor_func(mouse_clicks, key_downs, all_sprites, outer_blocks, inner_blocks, background_sprites)
            ########################################

            pygame.display.flip()
            self.clock.tick(FPS)

    def show_level_editor(self):
        with open("map.txt", "r") as map_file:
            prev_data = map_file.read()
            prev_data = prev_data.split("\n")
            prev_map_data = []

            for row in prev_data:
                tile = list(row)
                prev_map_data.append(tile)

        def level_editor(mouse_clicks, key_downs, all_sprites, outer_blocks, inner_blocks, background_sprites):
            pressed_keys = pygame.key.get_pressed()

            if mouse_clicks["left"]:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                tile_position = (mouse_x // TILE_SIZE[0], mouse_y // TILE_SIZE[0])

                if pressed_keys[K_g]:
                    grass = Grass(x=tile_position[0], y=tile_position[1], width=TILE_SIZE[0], height=TILE_SIZE[0])
                    outer_blocks.add(grass)
                    all_sprites.add(grass)
                    prev_map_data[tile_position[1]][tile_position[0]] = "G"
                elif pressed_keys[K_d]:
                    dirt = Dirt(x=tile_position[0], y=tile_position[1], width=TILE_SIZE[0], height=TILE_SIZE[0])
                    inner_blocks.add(dirt)
                    all_sprites.add(dirt)
                    prev_map_data[tile_position[1]][tile_position[0]] = "D"
                else:
                    for sprite in background_sprites:
                        if sprite.rect.collidepoint((mouse_x, mouse_y)):
                            sprite.rect.centerx = mouse_x
                            sprite.rect.centery = mouse_y

            if mouse_clicks["right"]:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                tile_position = (mouse_x // TILE_SIZE[0], mouse_y // TILE_SIZE[0])
                print("Tile", prev_map_data[tile_position[1]][tile_position[0]])

                for sprite in all_sprites:
                    if sprite.rect.collidepoint((mouse_x, mouse_y)):
                        sprite.kill()

                prev_map_data[tile_position[1]][tile_position[0]] = "0"

            if key_downs["s"]:
                # Save tile map data.
                new_data = []
                for row_list in prev_map_data:
                    row_string = "".join(row_list)
                    new_data.append(row_string)

                new_map_string = "\n".join(new_data)
                with open("map.txt", "w") as new_map_file:
                    new_map_file.write(new_map_string)

                # Save background sprites data.
                new_background_data = []

                for sprite in background_sprites:
                    new_background_data.append({
                        "sprite_name": sprite.sprite_name,
                        "x_coord": sprite.rect.x / UNIT_X,
                        "y_coord": sprite.rect.y / UNIT_Y,
                        "width": sprite.rect.width / UNIT_X,
                        "height": sprite.rect.height / UNIT_Y
                    })

                # Remove duplicates in new_background_data list.
                for i, sprite_data in enumerate(new_background_data):
                    for another_sprite_data in new_background_data[i + 1:]:
                        if sprite_data == another_sprite_data:
                            new_background_data.remove(another_sprite_data)

                new_background_json_data = json.dumps(new_background_data, indent=4)

                with open("background.json", "w") as new_background_file:
                    new_background_file.write(new_background_json_data)

            elif key_downs["t"]:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                width = 600 * UNIT_X
                height = 600 * UNIT_Y
                sprite = Tree(x=(mouse_x - (width / 2)), y=(mouse_y - (height / 2)), width=width, height=height)
                background_sprites.add(sprite)
                all_sprites.add(sprite)
                # print(background_sprites)

        self.start(level_editor_func=level_editor)

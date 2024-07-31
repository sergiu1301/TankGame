import pygame

from settings import *
from tile import Tile
from floor import Floor
from tank import Tank
from zombie import Zombie
from ammunition import Ammunition
from settings import WORLD_MAPS
import random


class Level:
    def __init__(self, game, level_index):
        self.game = game
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = YSortCameraGroup()
        self.obstacles_sprites = pygame.sprite.Group()
        self.bullet_sprites = pygame.sprite.Group()
        self.zombie_sprites = pygame.sprite.Group()
        self.ammunition = Ammunition()
        self.create_map(WORLD_MAPS[level_index])

    def create_map(self, world_map):
        for row_index, row in enumerate(world_map):
            for col_index, col, in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x, y), [self.visible_sprites, self.obstacles_sprites])
                if col == ' ':
                    Floor((x, y), [self.visible_sprites])
                if col == 'p':
                    Floor((x, y), [self.visible_sprites])
                    self.player = Tank((x, y), [self.visible_sprites], self.obstacles_sprites, self.bullet_sprites, self.zombie_sprites, self.game)

    def new_zombie(self):
        map_width = len(WORLD_MAPS[0][0]) * TILESIZE
        map_height = len(WORLD_MAPS[0]) * TILESIZE
        while True:
            x = random.randint(0, map_width // TILESIZE - 1) * TILESIZE
            y = random.randint(0, map_height // TILESIZE - 1) * TILESIZE
            zombie_rect = pygame.Rect(x, y, TILESIZE, TILESIZE)
            if not any(obstacle.rect.colliderect(zombie_rect) for obstacle in self.obstacles_sprites):
                Zombie((x, y), self.player, self.obstacles_sprites, [self.visible_sprites, self.zombie_sprites], self.game)
                break

    def run(self, events, dt):
        self.visible_sprites.custom_draw(self.player, self.ammunition, self.bullet_sprites, self.zombie_sprites)
        self.visible_sprites.update(events, dt)
        self.zombie_sprites.update(events, dt)


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player, ammunition, bullet_sprites, zombie_sprites):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)

        for bullet in bullet_sprites:
            offset_pos = bullet.rect.topleft - self.offset
            self.display_surface.blit(bullet.image, offset_pos)

        for zombie in zombie_sprites:
            offset_pos = zombie.rect.topleft - self.offset
            self.display_surface.blit(zombie.image, offset_pos)

        ammunition.draw_bullets(self.display_surface, self.offset)
        player_offset_pos = player.rect.topleft - self.offset
        self.display_surface.blit(player.image, player_offset_pos)

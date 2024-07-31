import pygame
import random

from settings import TILESIZE, WORLD_MAPS


class Ammunition:
    def __init__(self):
        self.image = pygame.image.load("Characters/bl.png").convert()
        self.image.set_colorkey((255, 255, 255))
        self.bullets = []

    def draw_bullets(self, surface, offset):
        for bullet in self.bullets:
            rect = self.image.get_rect(topleft=(bullet[0] - offset.x, bullet[1] - offset.y))
            surface.blit(self.image, rect)

    def check_collision(self, tank_rect):
        for bullet in self.bullets:
            rect = self.image.get_rect(topleft=bullet)
            if tank_rect.colliderect(rect):
                self.bullets.remove(bullet)
                return True
        return False

    def new_bullet(self, obstacle_sprites):
        map_width = len(WORLD_MAPS[0][0]) * TILESIZE
        map_height = len(WORLD_MAPS[0]) * TILESIZE
        while True:
            x = random.randint(0, map_width // TILESIZE - 1) * TILESIZE
            y = random.randint(0, map_height // TILESIZE - 1) * TILESIZE
            bullet_rect = pygame.Rect(x, y, TILESIZE, TILESIZE)
            if not any(obstacle.rect.colliderect(bullet_rect) for obstacle in obstacle_sprites):
                self.bullets.append([x, y])
                break

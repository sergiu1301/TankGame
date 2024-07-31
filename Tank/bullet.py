import pygame
from explosion import Explosion


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, direction, obstacle_sprites, groups, zombie_sprites, game):
        super().__init__(groups)
        self.image = pygame.image.load('Characters/bullet1.png')
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect(center=pos)
        self.collision_rect = self.rect.copy()
        self.direction = pygame.Vector2(direction.y, -direction.x)
        self.pos = pygame.Vector2(self.rect.center)
        self.obstacle_sprites = obstacle_sprites
        self.zombie_sprites = zombie_sprites
        self.speed = 10
        self.game = game

    def update(self, events, dt):
        self.pos += self.direction * dt
        self.rect.center = round(self.pos.x), round(self.pos.y)
        self.collision_rect.center = self.rect.center

        for obstacle in self.obstacle_sprites:
            if self.collision_rect.colliderect(obstacle.rect):
                self.kill()
                return

        for zombie in self.zombie_sprites:
            if self.collision_rect.colliderect(zombie.rect):
                Explosion(zombie.rect.center, self.groups())
                zombie.kill()
                self.kill()
                self.game.score += 1
                return
    '''
    def update(self, events, dt):
        self.pos += self.direction * self.speed * dt
        self.rect.center = round(self.pos.x), round(self.pos.y)

        # Verificare coliziune cu obstacolele
        for obstacle in self.obstacle_sprites:
            if self.rect.colliderect(obstacle.rect):
                collision_vector = pygame.Vector2(self.rect.center) - pygame.Vector2(obstacle.rect.center)
                if abs(collision_vector.x) > abs(collision_vector.y):
                    # Coliziune pe axa orizontală
                    self.direction.x *= -1
                else:
                    # Coliziune pe axa verticală
                    self.direction.y *= -1
                self.pos += self.direction * self.speed * dt  # Ajustare poziție după ricoseu
    '''
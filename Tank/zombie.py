import pygame


class Zombie(pygame.sprite.Sprite):
    def __init__(self, pos, target, obstacle_sprites, groups, game):
        super().__init__(groups)
        self.image = pygame.image.load('Characters/zombie.png').convert_alpha()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect(center=pos)
        self.collision_rect = self.rect.copy()
        self.pos = pygame.Vector2(self.rect.center)
        self.target = target
        self.obstacle_sprites = obstacle_sprites
        self.speed = 0.1
        self.game = game

    def update(self, events, dt):
        direction = self.target.pos - self.pos
        if direction.length() > 0:
            direction = direction.normalize()
            self.avoid_obstacles(direction)
            self.pos += direction * self.speed * dt
            self.rect.center = round(self.pos.x), round(self.pos.y)
            self.collision_rect.center = self.rect.center

        if self.collision_rect.colliderect(self.target.rect):
            self.game.decrease_lives()
            self.kill()

    def avoid_obstacles(self, direction):
        for obstacle in self.obstacle_sprites:
            if self.rect.colliderect(obstacle.rect.inflate(4, 4)):
                diff = self.pos - pygame.Vector2(obstacle.rect.center)
                if abs(diff.x) > abs(diff.y):
                    direction.x = diff.x / abs(diff.x)
                else:
                    direction.y = diff.y / abs(diff.y)

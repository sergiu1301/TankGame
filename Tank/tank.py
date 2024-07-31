import pygame.sprite

from bullet import Bullet


class Tank(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites, bullet_sprites, zombie_sprites, game):
        super().__init__(groups)
        self.frames = [
            pygame.image.load('Characters/tank1_up.png'),
            pygame.image.load('Characters/tank1_up_move1.png'),
            pygame.image.load('Characters/tank1_up_move2.png'),
            pygame.image.load('Characters/tank1_up_move3.png'),
            pygame.image.load('Characters/tank1_up_move4.png'),
            pygame.image.load('Characters/tank1_up_move5.png'),
            pygame.image.load('Characters/tank1_up_move6.png'),
            pygame.image.load('Characters/tank1_up_move7.png')
        ]
        for frame in self.frames:
            frame.set_colorkey("white")

        self.original_frames = [frame.copy() for frame in self.frames]
        self.current_frame = 0
        self.animation_time = 70
        self.current_time = 0

        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(center=pos)
        self.collision_rect = self.rect.copy()
        self.direction = pygame.Vector2(1, 0)
        self.pos = pygame.Vector2(self.rect.center)
        self.last_pos = pygame.Vector2(self.rect.center)
        self.angle = 0
        self.ammo_count = 100

        self.obstacle_sprites = obstacle_sprites
        self.bullet_sprites = bullet_sprites
        self.zombie_sprites = zombie_sprites
        self.game = game

    def update(self, events, dt):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.ammo_count > 0:
                        self.bullet_sprites.add(
                            Bullet(self.rect.center, self.direction.normalize(), self.obstacle_sprites, self.groups(), self.zombie_sprites, self.game))
                        self.ammo_count -= 1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.angle += 3
        if keys[pygame.K_d]:
            self.angle -= 3

        if self.pos != self.last_pos:
            self.current_time += dt
            if self.current_time >= self.animation_time:
                self.current_frame = (self.current_frame + 1) % len(self.frames)
                self.image = self.frames[self.current_frame]
                self.current_time = 0
            self.image = pygame.transform.rotate(self.original_frames[self.current_frame], self.angle)
        else:
            self.image = pygame.transform.rotate(self.original_frames[0], self.angle)

        self.direction = pygame.Vector2(1, 0).rotate(-self.angle)

        self.rect = self.image.get_rect(center=self.rect.center)
        self.collision_rect.center = self.rect.center

        self.last_pos.update(self.pos)
        self.up_down()
        self.collision()

    def move(self, velocity):
        direction = pygame.Vector2(0, velocity).rotate(-self.angle)
        self.pos += direction
        self.rect.center = round(self.pos[0]), round(self.pos[1])

    def up_down(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.move(-5)
        if keys[pygame.K_s]:
            self.move(5)

    def check_collision(self, random_bullet):
        if random_bullet.check_collision(self.collision_rect):
            self.ammo_count += 5

    def collision(self):
        for sprite in self.obstacle_sprites:
            if sprite.rect.colliderect(self.collision_rect):
                collision_vector = pygame.Vector2(sprite.rect.center) - pygame.Vector2(self.collision_rect.center)
                collision_vector_length = collision_vector.length()

                if collision_vector_length == 0:
                    return

                overlap_x = self.collision_rect.width / 2 + sprite.rect.width / 2 - abs(collision_vector.x)
                overlap_y = self.collision_rect.height / 2 + sprite.rect.height / 2 - abs(collision_vector.y)

                if overlap_x < overlap_y:
                    if collision_vector.x > 0:
                        self.pos.x -= overlap_x / 2
                    else:
                        self.pos.x += overlap_x / 2
                else:
                    if collision_vector.y > 0:
                        self.pos.y -= overlap_y / 2
                    else:
                        self.pos.y += overlap_y / 2

                self.rect.center = round(self.pos.x), round(self.pos.y)
                self.collision_rect.center = self.rect.center
        self.rect.center = round(self.pos.x), round(self.pos.y)
        self.collision_rect.center = self.rect.center

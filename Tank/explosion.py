import pygame


class Explosion(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.frames = [pygame.image.load(f'Characters/explosion{frame}.png') for frame in range(3)]
        for frame in self.frames:
            frame.set_colorkey("white")
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(center=pos)
        self.animation_speed = 70
        self.last_update = pygame.time.get_ticks()

    def update(self, events, dt):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.animation_speed:
            self.last_update = now
            self.current_frame += 1
            if self.current_frame < len(self.frames):
                self.image = self.frames[self.current_frame]
                self.rect = self.image.get_rect(center=self.rect.center)
            else:
                self.kill()

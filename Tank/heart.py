import pygame


class Heart(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("Characters/heart2.png")
        self.rect = self.image.get_rect(topleft=pos)

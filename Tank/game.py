import pygame
import json

from settings import WIDTH, HEIGHT, FPS
from level import Level


class Game:
    def __init__(self):
        super().__init__()
        self.run_game = True
        self.width = 1280
        self.height = 720
        self.loc = [0, 0]
        self.background_color = (0, 0, 0)
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.bullet_container = 10000
        self.my_font = pygame.font.SysFont('Comic Sans MS', 30)
        self.score = 0
        self.lives = 6
        self.full_heart_image = pygame.image.load('Characters/full_heart.png').convert_alpha()
        self.half_heart_image = pygame.image.load('Characters/half_heart.png').convert_alpha()
        self.empty_heart_image = pygame.image.load('Characters/empty_heart.png').convert_alpha()
        self.scores_file = 'scores.json'

    def show_text(self, msg, x, y, variable=None):
        if variable != None:
            text = self.my_font.render('Amo:' + str(variable), False, (255, 255, 255))
        else:
            text = self.my_font.render(msg, True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.topleft = [x, y]
        self.screen.blit(text, text_rect)

    def show_score(self, x, y):
        text = self.my_font.render('Score:' + str(self.score), False, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.topleft = [x, y]
        self.screen.blit(text, text_rect)

    def decrease_lives(self):
        self.lives -= 1
        if self.lives <= 0:
            self.run_game = False

    def display_game_over(self):
        font = pygame.font.Font(None, 74)
        text_surface = font.render("GAME OVER", True, (255, 0, 0))
        rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.screen.blit(text_surface, rect.topleft)

    def draw_lives(self):
        for i in range(3):
            if self.lives >= (i + 1) * 2:
                self.screen.blit(self.full_heart_image, (10 + i * 55, 10))
            elif self.lives == (i * 2 + 1):
                self.screen.blit(self.half_heart_image, (10 + i * 55, 10))
            else:
                self.screen.blit(self.empty_heart_image, (10 + i * 55, 10))

    def save_score(self, name, score):
        scores = self.load_scores()
        scores.append({"name": name, "score": score})
        scores = sorted(scores, key=lambda x: x['score'], reverse=True)

        with open(self.scores_file, 'w') as f:
            json.dump(scores, f, indent=4)

    def load_scores(self):
        try:
            with open(self.scores_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def ask_save_score(self):
        font = pygame.font.Font(None, 36)
        self.screen.fill(self.background_color)
        self.show_text("Do you want to save your score? (Y/N)", self.screen.get_width() // 2 - 250,
                       self.screen.get_height() // 2)
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        return True
                    elif event.key == pygame.K_n:
                        return False

    def get_player_name(self):
        font = pygame.font.Font(None, 36)
        name = ""
        self.screen.fill(self.background_color)
        self.show_text("Enter your name: ", self.screen.get_width() // 2 - 200, self.screen.get_height() // 2)
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return ""
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return name
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    else:
                        name += event.unicode

            self.screen.fill(self.background_color)
            self.show_text("Enter your name: ", self.screen.get_width() // 2 - 200, self.screen.get_height() // 2)
            self.show_text(name, self.screen.get_width() // 2 - 200, self.screen.get_height() // 2 + 50)
            pygame.display.update()

    def run_level(self, level_index):
        self.lives = 6
        self.run_game = True
        self.score = 0
        level = Level(self, level_index)

        clock = pygame.time.Clock()
        dt = 0

        ammo_interval = 30000
        pygame.time.set_timer(pygame.USEREVENT + 1, ammo_interval)

        zombie_interval = 10000
        pygame.time.set_timer(pygame.USEREVENT + 2, zombie_interval)

        while self.run_game:
            events = pygame.event.get()
            for e in events:
                if e.type == pygame.QUIT:
                    return
                elif e.type == pygame.USEREVENT + 1:
                    level.ammunition.new_bullet(level.obstacles_sprites)
                elif e.type == pygame.USEREVENT + 2:
                    level.new_zombie()

            level.player.check_collision(level.ammunition)
            self.screen.fill(self.background_color)
            level.run(events, dt)

            self.show_text(' ', 200, 5, level.player.ammo_count)
            self.show_score(1100, 5)
            self.draw_lives()

            pygame.display.update()
            dt = clock.tick(FPS)

        self.display_game_over()
        pygame.display.update()
        pygame.time.wait(3000)

        if self.ask_save_score():
            name = self.get_player_name()
            if name:
                self.save_score(name, self.score)

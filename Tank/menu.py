import pygame
import sys


class Menu:
    def __init__(self, screen, levels, game):
        self.screen = screen
        self.levels = levels
        self.selected_level = 0
        self.game = game
        self.background = pygame.image.load('Characters/Background.png').convert()

        self.font = pygame.font.Font(None, 74)
        self.title_text = self.font.render("Tank Game", True, (255, 255, 255))

        self.level_buttons = []
        for i, level in enumerate(levels):
            button_text = self.font.render(f"Level {i + 1}", True, (255, 255, 255))
            button_rect = button_text.get_rect(center=(screen.get_width() // 2, 150 + i * 100))
            self.level_buttons.append((button_text, button_rect))

        self.scores_button = self.font.render("Ranks", True, (255, 255, 255))
        self.scores_button_rect = self.scores_button.get_rect(center=(screen.get_width() // 2, 150 + len(levels) * 100))

    def run(self):
        while True:
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.title_text, self.title_text.get_rect(center=(self.screen.get_width() // 2, 50)))

            mouse_pos = pygame.mouse.get_pos()
            for i, (button_text, button_rect) in enumerate(self.level_buttons):
                if button_rect.collidepoint(mouse_pos):
                    button_text = self.font.render(f"Level {i + 1}", True, (255, 0, 0))
                else:
                    button_text = self.font.render(f"Level {i + 1}", True, (255, 255, 255))
                self.screen.blit(button_text, button_rect)

            if self.scores_button_rect.collidepoint(mouse_pos):
                self.scores_button = self.font.render("Ranks", True, (255, 0, 0))
            else:
                self.scores_button = self.font.render("Ranks", True, (255, 255, 255))
            self.screen.blit(self.scores_button, self.scores_button_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for i, (_, button_rect) in enumerate(self.level_buttons):
                        if button_rect.collidepoint(event.pos):
                            return i
                        if self.scores_button_rect.collidepoint(event.pos):
                            self.show_scores()

            pygame.display.flip()

    def show_scores(self):
        scores = self.game.load_scores()
        font = pygame.font.Font(None, 36)
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.title_text, self.title_text.get_rect(center=(self.screen.get_width() // 2, 50)))

        y_offset = 150
        for score in scores:
            score_text = font.render(f"{score['name']}: {score['score']}", True, (255, 255, 255))
            score_rect = score_text.get_rect(center=(self.screen.get_width() // 2, y_offset))
            self.screen.blit(score_text, score_rect)
            y_offset += 50

        pygame.display.flip()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    waiting = False

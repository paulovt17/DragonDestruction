import sys

import pygame


class GameOver:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load(
            "./asset/GameOver.png"
        ).convert_alpha()

        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):

        pygame.mixer_music.load("./asset/GameOver.mp3")
        pygame.mixer_music.play(-1)

        while True:
            self.window.blit(self.surf, self.rect)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return "menu"

            pygame.display.flip()
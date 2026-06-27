import sys

import pygame

from code.Const import MENU_OPTION, WIN_HEIGHT, WIN_WIDTH
from code.GameOver import GameOver
from code.Level import Level
from code.Menu import Menu
from code.Score import Score


class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    def run(self):

        while True:
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[4]:
                pygame.quit()
                sys.exit()

            if menu_return == MENU_OPTION[3]:
                score.show()
                continue

            if menu_return in (
                MENU_OPTION[0],
                MENU_OPTION[1],
                MENU_OPTION[2],
            ):
                player_score = [0, 0]

                player_form = [
                    "Player1Form0",
                    "Player2Form0",
                ]

                win = True

                for level_name in ("Level1", "Level2", "Level3"):
                    level = Level(
                        self.window,
                        level_name,
                        menu_return,
                        player_score,
                        player_form,
                    )

                    if not level.run(player_score, player_form):
                        win = False

                        game_over = GameOver(self.window)
                        option = game_over.run()

                        if option == "menu":
                            break

                if not win:
                    continue

                score.save(menu_return, player_score)
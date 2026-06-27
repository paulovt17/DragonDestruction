import random

from code.Background import Background
from code.Const import WIN_HEIGHT, WIN_WIDTH
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def _create_background(level: str) -> list:

        backgrounds = []

        for i in range(4):
            backgrounds.extend(
                [
                    Background(f"{level}Bg{i}", (0, 0)),
                    Background(f"{level}Bg{i}", (WIN_WIDTH, 0)),
                ]
            )

        return backgrounds

    @staticmethod
    def get_entity(entity_name: str):

        match entity_name:
            case "Level1Bg":
                return EntityFactory._create_background("Level1")

            case "Level2Bg":
                return EntityFactory._create_background("Level2")

            case "Level3Bg":
                return EntityFactory._create_background("Level3")

            case "Player1Form0":
                return Player("Player1Form0", (10, WIN_HEIGHT / 2 - 30))

            case "Player1Form1":
                return Player("Player1Form1", (10, WIN_HEIGHT / 2 - 30))

            case "Player1Form2":
                return Player("Player1Form2", (10, WIN_HEIGHT / 2 - 30))

            case "Player2Form0":
                return Player("Player2Form0", (10, WIN_HEIGHT / 2 + 30))

            case "Player2Form1":
                return Player("Player2Form1", (10, WIN_HEIGHT / 2 + 30))

            case "Player2Form2":
                return Player("Player2Form2", (10, WIN_HEIGHT / 2 + 30))

            case "Enemy1":
                return Enemy(
                    "Enemy1",
                    (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)),
                )

            case "Enemy2":
                return Enemy(
                    "Enemy2",
                    (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)),
                )

            case "Enemy3":
                return Enemy(
                    "Enemy3",
                    (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)),
                )

            case "Enemy4":
                return Enemy(
                    "Enemy4",
                    (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)),
                )

            case "Enemy5":
                return Enemy(
                    "Enemy5",
                    (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)),
                )

            case "Enemy6":
                return Enemy(
                    "Enemy6",
                    (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)),
                )

            case _:
                return None
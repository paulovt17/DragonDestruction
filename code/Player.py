import pygame.key

from code.Const import COOLDOWN_SHOT1,COOLDOWN_SHOT2,COOLDOWN_SHOT3,ENTITY_HEALTH, \
ENTITY_SPEED,PLAYER_KEY_DOWN,PLAYER_KEY_LEFT,PLAYER_KEY_RIGHT,PLAYER_KEY_SHOOT1, \
 PLAYER_KEY_SHOOT2,PLAYER_KEY_SHOOT3,PLAYER_KEY_UP,SCORE_TRANSFORMATION1, \
 SCORE_TRANSFORMATION2,WIN_HEIGHT,WIN_WIDTH
from code.Entity import Entity
from code.PlayerShot import PlayerShot


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

        self.cooldown1 = 0
        self.cooldown2 = 0
        self.cooldown3 = 0

        self.health = ENTITY_HEALTH[self.name]

    def move(self):
        pressed = pygame.key.get_pressed()
        speed = ENTITY_SPEED[self.name]

        if pressed[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= speed

        if pressed[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += speed

        if pressed[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= speed

        if pressed[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += speed

    def shoot(self):

        if self.cooldown1 > 0:
            self.cooldown1 -= 1
        if self.cooldown2 > 0:
            self.cooldown2 -= 1
        if self.cooldown3 > 0:
            self.cooldown3 -= 1

        pressed = pygame.key.get_pressed()

        if pressed[PLAYER_KEY_SHOOT1[self.name]] and self.cooldown1 == 0:
            self.cooldown1 = COOLDOWN_SHOT1[self.name]

            return PlayerShot(
                name=f"{self.name[:-1]}0Shot",
                position=(self.rect.centerx, self.rect.centery),
            )

        if self.name in ("Player1Form1","Player1Form2","Player2Form1","Player2Form2",
        ) and pressed[PLAYER_KEY_SHOOT2[self.name]] and self.cooldown2 == 0:

            self.cooldown2 = COOLDOWN_SHOT2[self.name]

            return PlayerShot(
                name=f"{self.name[:-1]}1Shot",
                position=(self.rect.centerx, self.rect.centery),
            )

        if self.name in ("Player1Form2", "Player2Form2") and pressed[
            PLAYER_KEY_SHOOT3[self.name]
        ] and self.cooldown3 == 0:

            self.cooldown3 = COOLDOWN_SHOT3[self.name]

            return PlayerShot(
                name=f"{self.name[:-1]}2Shot",
                position=(self.rect.centerx, self.rect.centery),
            )

        return None

    def transform(self):
        if self.name == "Player1Form0" and self.score >= SCORE_TRANSFORMATION1:
            self._change_form("Player1Form1")

        elif self.name == "Player1Form1" and self.score >= SCORE_TRANSFORMATION2:
            self._change_form("Player1Form2")

        elif self.name == "Player2Form0" and self.score >= SCORE_TRANSFORMATION1:
            self._change_form("Player2Form1")

        elif self.name == "Player2Form1" and self.score >= SCORE_TRANSFORMATION2:
            self._change_form("Player2Form2")

    def _change_form(self, new_name: str):
        self.name = new_name
        self.surf = pygame.image.load(f"./asset/{new_name}.png").convert_alpha()
        self.health = ENTITY_HEALTH[self.name]
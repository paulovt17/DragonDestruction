from code.Const import ENTITY_SHOT_DELAY, ENTITY_SPEED
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[name]

    def move(self) -> None:
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self) -> EnemyShot | None:
        self.shot_delay -= 1

        if self.shot_delay > 0:
            return None

        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

        return EnemyShot(
            name=f"{self.name}Shot",
            position=(self.rect.centerx, self.rect.centery),
        )
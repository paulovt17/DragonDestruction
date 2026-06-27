from code.Const import ENTITY_SPEED
from code.Entity import Entity


class EnemyShot(Entity):

    def move(self) -> None:
        self.rect.centerx -= ENTITY_SPEED[self.name]
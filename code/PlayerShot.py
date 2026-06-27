from code.Const import ENTITY_SPEED
from code.Entity import Entity


class PlayerShot(Entity):

    def move(self) -> None:
        self.rect.centerx += ENTITY_SPEED[self.name]
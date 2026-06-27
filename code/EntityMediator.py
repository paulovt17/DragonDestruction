from code.Const import WIN_WIDTH
from code.Enemy import Enemy
from code.EnemyShot import EnemyShot
from code.Entity import Entity
from code.Player import Player
from code.PlayerShot import PlayerShot


class EntityMediator:

    @staticmethod
    def _handle_window_collision(entity: Entity) -> None:

        if isinstance(entity, Enemy) and entity.rect.right <= 0:
            entity.health = 0

        elif isinstance(entity, PlayerShot) and entity.rect.left >= WIN_WIDTH:
            entity.health = 0

        elif isinstance(entity, EnemyShot) and entity.rect.right <= 0:
            entity.health = 0

    @staticmethod
    def _is_valid_interaction(ent1: Entity, ent2: Entity) -> bool:
        return (
            (isinstance(ent1, Enemy) and isinstance(ent2, PlayerShot)) or
            (isinstance(ent1, PlayerShot) and isinstance(ent2, Enemy)) or
            (isinstance(ent1, Player) and isinstance(ent2, EnemyShot)) or
            (isinstance(ent1, EnemyShot) and isinstance(ent2, Player))
        )

    @staticmethod
    def _handle_entity_collision(ent1: Entity, ent2: Entity) -> None:

        if not EntityMediator._is_valid_interaction(ent1, ent2):
            return

        if (
            ent1.rect.right >= ent2.rect.left and
            ent1.rect.left <= ent2.rect.right and
            ent1.rect.bottom >= ent2.rect.top and
            ent1.rect.top <= ent2.rect.bottom
        ):
            ent1.health -= ent2.damage
            ent2.health -= ent1.damage

            ent1.last_dmg = ent2.name
            ent2.last_dmg = ent1.name

    @staticmethod
    def _assign_score(enemy: Enemy, entities: list[Entity]) -> None:

        if not enemy.last_dmg:
            return

        target_player_prefix = None

        if enemy.last_dmg.startswith("Player1"):
            target_player_prefix = "Player1"
        elif enemy.last_dmg.startswith("Player2"):
            target_player_prefix = "Player2"

        if not target_player_prefix:
            return

        for entity in entities:
            if (
                isinstance(entity, Player)
                and entity.name.startswith(target_player_prefix)
            ):
                entity.score += enemy.score
                break

    @staticmethod
    def verify_collision(entity_list: list[Entity]) -> None:
        for i, entity1 in enumerate(entity_list):
            EntityMediator._handle_window_collision(entity1)

            for entity2 in entity_list[i + 1:]:
                EntityMediator._handle_entity_collision(entity1, entity2)

    @staticmethod
    def verify_health(entity_list: list[Entity]) -> None:
        for entity in entity_list[:]:
            if entity.health <= 0:

                if isinstance(entity, Enemy):
                    EntityMediator._assign_score(entity, entity_list)

                entity_list.remove(entity)

import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import MENU_OPTION, EVENT_ENEMY, C_CYAN, EVENT_TIMEOUT, \
    TIMEOUT_STEP, TIMEOUT_LEVEL, C_ORANGE, MIN_SPAWN_TIME, LEVEL_SETTINGS, C_GREEN
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:
    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int], player_form: list[str]):

        self.player_form = None
        self.timeout = TIMEOUT_LEVEL
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))
        player = EntityFactory.get_entity(player_form[0])
        player.score = player_score[0]
        self.entity_list.append(player)

        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            player = EntityFactory.get_entity(player_form[1])
            player.score = player_score[1]
            self.entity_list.append(player)
        self.enemy_spawn = LEVEL_SETTINGS[self.name]['spawn_time']
        pygame.time.set_timer(EVENT_ENEMY, self.enemy_spawn)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

    def run(self, player_score: list[int], player_form: list[str]):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.set_volume(0.3)
        pygame.mixer_music.play(-1)
        self.player_form = player_form
        clock = pygame.time.Clock()

        while True:

            clock.tick(60)

            self.window.fill((0, 0, 0))

            new_shots = []

            for ent in self.entity_list:

                self.window.blit(source=ent.surf, dest=ent.rect)

                ent.move()

                if isinstance(ent, Player):
                    ent.transform()

                if isinstance(ent, (Player, Enemy)):

                    shoot = ent.shoot()

                    if shoot is not None:
                        new_shots.append(shoot)

                if isinstance(ent, Player):

                    if ent.name.startswith('Player1'):

                        self.level_text(14,f'Player1 - Health: {ent.health} | Score: {ent.score}',C_ORANGE,(10, 5))

                    elif ent.name.startswith('Player2'):

                        self.level_text(14,f'Player2 - Health: {ent.health} | Score: {ent.score}',C_CYAN,(10, 25)
                        )

            self.entity_list.extend(new_shots)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    if self.name == 'Level1':
                        choice = random.choice(('Enemy1', 'Enemy2'))

                    elif self.name == 'Level2':
                        choice = random.choice(('Enemy2', 'Enemy3', 'Enemy4'))

                    elif self.name == 'Level3':
                        choice = random.choice(('Enemy3', 'Enemy4', 'Enemy5', 'Enemy6'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP

                    config = LEVEL_SETTINGS[self.name]

                    if self.timeout % config['decrease_time'] == 0:
                        self.enemy_spawn = max(MIN_SPAWN_TIME,self.enemy_spawn - config['decrease_value'])
                        pygame.time.set_timer(EVENT_ENEMY,self.enemy_spawn)
                            
                    if self.timeout == 0:
                        for ent in self.entity_list:

                            if isinstance(ent, Player):

                                if ent.name.startswith('Player1'):
                                    player_score[0] = ent.score

                                elif ent.name.startswith('Player2'):
                                    player_score[1] = ent.score
                        return True

                found_player = False
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True

                if not found_player:
                    return False


            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', C_GREEN, (400, 5))
            pygame.display.flip()

            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.Font("./asset/Bubblegum.ttf", text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

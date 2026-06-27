import pygame

# C
C_CYAN = (0, 128, 128)
C_GREEN = (0, 128, 0)
C_ORANGE = (255, 165, 0)
C_WHITE = (255, 255, 255)
C_YELLOW = (255, 255, 128)

COOLDOWN_SHOT1 = {
    'Player1Form0': 40,
    'Player1Form1': 20,
    'Player1Form2': 10,
    'Player2Form0': 40,
    'Player2Form1': 20,
    'Player2Form2': 10
}

COOLDOWN_SHOT2 = {
    'Player1Form1': 40,
    'Player1Form2': 20,
    'Player2Form1': 40,
    'Player2Form2': 20
}

COOLDOWN_SHOT3 = {
    'Player1Form2': 40,
    'Player2Form2': 40
}

# E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level2Bg0': 0,
    'Level2Bg1': 1,
    'Level2Bg2': 2,
    'Level2Bg3': 3,
    'Level3Bg0': 0,
    'Level3Bg1': 1,
    'Level3Bg2': 2,
    'Level3Bg3': 3,
    'Player1Form0': 3,
    'Player1Form1': 6,
    'Player1Form2': 9,
    'Player1Form0Shot': 1,
    'Player1Form1Shot': 5,
    'Player1Form2Shot': 3,
    'Player2Form0': 3,
    'Player2Form1': 6,
    'Player2Form2': 9,
    'Player2Form0Shot': 1,
    'Player2Form1Shot': 5,
    'Player2Form2Shot': 3,
    'Enemy1': 1,
    'Enemy1Shot': 3,
    'Enemy2': 1,
    'Enemy2Shot': 2,
    'Enemy3': 1.25,
    'Enemy3Shot': 5,
    'Enemy4': 1.25,
    'Enemy4Shot': 3,
    'Enemy5': 1.5,
    'Enemy5Shot': 7,
    'Enemy6': 1.5,
    'Enemy6Shot': 3,
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,
    'Level3Bg0': 999,
    'Level3Bg1': 999,
    'Level3Bg2': 999,
    'Level3Bg3': 999,
    'Player1Form0': 100,
    'Player1Form1': 200,
    'Player1Form2': 300,
    'Player1Form0Shot': 1,
    'Player1Form1Shot': 1,
    'Player1Form2Shot': 1,
    'Player2Form0': 100,
    'Player2Form1': 200,
    'Player2Form2': 300,
    'Player2Form0Shot': 1,
    'Player2Form1Shot': 1,
    'Player2Form2Shot': 1,
    'Enemy1': 45,
    'Enemy1Shot': 1,
    'Enemy2': 60,
    'Enemy2Shot': 1,
    'Enemy3': 100,
    'Enemy3Shot': 1,
    'Enemy4': 120,
    'Enemy4Shot': 1,
    'Enemy5': 160,
    'Enemy5Shot': 1,
    'Enemy6': 180,
    'Enemy6Shot': 1,
}

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level3Bg0': 0,
    'Level3Bg1': 0,
    'Level3Bg2': 0,
    'Level3Bg3': 0,
    'Player1Form0': 1,
    'Player1Form1': 1,
    'Player1Form2': 1,
    'Player1Form0Shot': 20,
    'Player1Form1Shot': 40,
    'Player1Form2Shot': 60,
    'Player2Form0': 1,
    'Player2Form1': 1,
    'Player2Form2': 1,
    'Player2Form0Shot': 20,
    'Player2Form1Shot': 40,
    'Player2Form2Shot': 60,
    'Enemy1': 1,
    'Enemy1Shot': 5,
    'Enemy2': 1,
    'Enemy2Shot': 10,
    'Enemy3': 1,
    'Enemy3Shot': 20,
    'Enemy4': 1,
    'Enemy4Shot': 25,
    'Enemy5': 1,
    'Enemy5Shot': 35,
    'Enemy6': 1,
    'Enemy6Shot': 40,
}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level3Bg0': 0,
    'Level3Bg1': 0,
    'Level3Bg2': 0,
    'Level3Bg3': 0,
    'Player1Form0': 0,
    'Player1Form1': 0,
    'Player1Form2': 0,
    'Player1Form0Shot': 0,
    'Player1Form1Shot': 0,
    'Player1Form2Shot': 0,
    'Player2Form0': 0,
    'Player2Form1': 0,
    'Player2Form2': 0,
    'Player2Form0Shot': 0,
    'Player2Form1Shot': 0,
    'Player2Form2Shot': 0,
    'Enemy1': 100,
    'Enemy1Shot': 0,
    'Enemy2': 125,
    'Enemy2Shot': 0,
    'Enemy3': 200,
    'Enemy3Shot': 0,
    'Enemy4': 250,
    'Enemy4Shot': 0,
    'Enemy5': 400,
    'Enemy5Shot': 0,
    'Enemy6': 500,
    'Enemy6Shot': 0,
}

ENTITY_SHOT_DELAY = {
    'Enemy1': 200,
    'Enemy2': 250,
    'Enemy3': 150,
    'Enemy4': 200,
    'Enemy5': 100,
    'Enemy6': 150,
}

# L
LEVEL_SETTINGS = {
    'Level1': {
        'spawn_time': 4000,
        'decrease_time': 10000,
        'decrease_value': 400
    },

    'Level2': {
        'spawn_time': 3000,
        'decrease_time': 8000,
        'decrease_value': 350
    },

    'Level3': {
        'spawn_time': 2000,
        'decrease_time': 5000,
        'decrease_value': 300
    }
}

# M
MENU_OPTION = ('NEW GAME 1Player',
               'NEW GAME 2Players - TEAM',
               'NEW GAME 2Players - VERSUS',
               'SCORE',
               'EXIT')
MIN_SPAWN_TIME = 800

# P
PLAYER_KEY_UP = {'Player1Form0': pygame.K_w,
                 'Player1Form1': pygame.K_w,
                 'Player1Form2': pygame.K_w,

                 'Player2Form0': pygame.K_UP,
                 'Player2Form1': pygame.K_UP,
                 'Player2Form2': pygame.K_UP
                 }
PLAYER_KEY_DOWN = {'Player1Form0': pygame.K_s,
                   'Player1Form1': pygame.K_s,
                   'Player1Form2': pygame.K_s,

                   'Player2Form0': pygame.K_DOWN,
                   'Player2Form1': pygame.K_DOWN,
                   'Player2Form2': pygame.K_DOWN
                   }
PLAYER_KEY_LEFT = {'Player1Form0': pygame.K_a,
                   'Player1Form1': pygame.K_a,
                   'Player1Form2': pygame.K_a,

                   'Player2Form0': pygame.K_LEFT,
                   'Player2Form1': pygame.K_LEFT,
                   'Player2Form2': pygame.K_LEFT
                   }
PLAYER_KEY_RIGHT = {'Player1Form0': pygame.K_d,
                    'Player1Form1': pygame.K_d,
                    'Player1Form2': pygame.K_d,

                    'Player2Form0': pygame.K_RIGHT,
                    'Player2Form1': pygame.K_RIGHT,
                    'Player2Form2': pygame.K_RIGHT
                    }
PLAYER_KEY_SHOOT1 = {'Player1Form0': pygame.K_f,
                     'Player1Form1': pygame.K_f,
                     'Player1Form2': pygame.K_f,

                     'Player2Form0': pygame.K_p,
                     'Player2Form1': pygame.K_p,
                     'Player2Form2': pygame.K_p
                     }
PLAYER_KEY_SHOOT2 = {'Player1Form0': pygame.K_g,
                     'Player1Form1': pygame.K_g,
                     'Player1Form2': pygame.K_g,
                     'Player2Form0': pygame.K_o,
                     'Player2Form1': pygame.K_o,
                     'Player2Form2': pygame.K_o
                     }
PLAYER_KEY_SHOOT3 = {'Player1Form0': pygame.K_h,
                     'Player1Form1': pygame.K_h,
                     'Player1Form2': pygame.K_h,
                     'Player2Form0': pygame.K_i,
                     'Player2Form1': pygame.K_i,
                     'Player2Form2': pygame.K_i
                     }

# S
SCORE_TRANSFORMATION1 = 5000
SCORE_TRANSFORMATION2 = 20000

# T
TIMEOUT_STEP = 100
TIMEOUT_LEVEL = 100000

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324

# S
SCORE_POS = {'Title': (WIN_WIDTH / 2, 50),
             'EnterName': (WIN_WIDTH / 2, 80),
             'Label': (WIN_WIDTH / 2, 90),
             'Name': (WIN_WIDTH / 2, 110),
             0: (WIN_WIDTH / 2, 110),
             1: (WIN_WIDTH / 2, 130),
             2: (WIN_WIDTH / 2, 150),
             3: (WIN_WIDTH / 2, 170),
             4: (WIN_WIDTH / 2, 190),
             5: (WIN_WIDTH / 2, 210),
             6: (WIN_WIDTH / 2, 230),
             7: (WIN_WIDTH / 2, 250),
             8: (WIN_WIDTH / 2, 270),
             9: (WIN_WIDTH / 2, 290),
             }

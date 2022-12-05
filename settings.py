import pygame as pg
vec = pg.math.Vector2

#defining colors

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255,255,0)
ORANGE = (255, 98, 0)

#game settings
WIDTH = 1024
HEIGHT = 768
FPS = 60
TITLE = "A 2D WORLD"


TILESIZE = 16
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE



# # Player settings
# PLAYER_HEALTH = 100
# PLAYER_SPEED = 280
# PLAYER_ROT_SPEED = 200
# PLAYER_IMG = 'manBlue_gun.png'
# PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)



# # Mob settings
# MOB_IMG = 'zombie1_hold.png'
# MOB_SPEED = 150
# MOB_HIT_RECT = pg.Rect(0, 0, 30, 30)
# MOB_HEALTH = 100
# MOB_DAMAGE = 10
# MOB_KNOCKBACK = 20

import pygame as pg
from utube_1st_tutorial_1st import posx
from utube_1st_tutorial_1st import posy
from utube_1st_tutorial_1st import cwidth
from utube_1st_tutorial_1st import cheight

global swidth
global sheight

swidth = 640
sheight = 480

global screen
screen = pg.display.set_mode((swidth,sheight))
global time
time = pg.time.Clock()
pg.display.set_caption("Title")

global bubble_surface
bubble_surface = pg.Surface((20, 20))

for i in range(0,255):
    for j in range(0,20):
        for n in range(0,5):
            pg.draw.circle(bubble_surface, (100, 100, 100, i), (j, j), n)
            screen.blit(bubble_surface, (posx, posy))

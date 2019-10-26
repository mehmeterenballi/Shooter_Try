""""
import pygame as pg
import utube_1st_tutorial


class Projectile(object):
    def __init__(self, posx, posy, radius, color, facing):
        self.x = posx
        self.y = posy
        self.radius = radius
        self.color = color
        self.facing = facing
        self.speed = 10

    def draw(self, win):
        pg.draw.circle(win, (200, 0, 0, 0), (self.x, self.y), self.radius)


bullets = []


def del_bullets():
    for bullet in bullets:
        if utube_1st_tutorial.swidth > bullet.x > 0:
            bullet.x += bullet.speed * facing
        else:
            bullets.pop(bullets.index(bullet))


def draw_bullets():
    for bullet in bullets:
        bullet.draw(utube_1st_tutorial.screen)


def create_bullets():
    if len(bullets) < 5:
        bullets.append(Projectile(round(utube_1st_tutorial.player.x + utube_1st_tutorial.player.width // 2), round(utube_1st_tutorial.player.y + utube_1st_tutorial.player.height // 2), 4, (0, 0, 0), facing))

    """
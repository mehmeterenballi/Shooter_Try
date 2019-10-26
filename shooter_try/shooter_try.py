import pygame as pg
# import random

pg.init()
running = True


time = pg.time.Clock()
pg.display.set_caption("Shooter Game Try")

swidth = 640
sheight = 480

screen = pg.display.set_mode((swidth, sheight))

path = 'C:/Users/Mehmet/Desktop/Çalışma Dosyaları/Bm programları/Yazılımsal/kişisel-python/Game_Tries/pygame_tries/FirstHand/shooter_try/'

walkRight = [pg.image.load('R%s.png' % frame) for frame in range(1, 10)]

walkLeft = [pg.image.load('L%s.png' % frame) for frame in range(1, 10)]

bg = pg.image.load(path + 'BG.jpg')
char = pg.image.load(path + 'Standing.png')

bSound = pg.mixer.Sound('bullet.wav')
hSound = pg.mixer.Sound('hit.wav')

score = 0

font = pg.font.SysFont("comicsans", 30, True, True)


class Player(object):
    def __init__(self, posx, posy, cwidth, cheight):
        self.x = posx
        self.y = posy
        self.width = cwidth
        self.height = cheight
        self.speed = 5
        self.isJump = False
        self.left = False
        self.right = True
        self.standing = True
        self.walkCount = 0
        self.jumpCount = 10
        self.hitbox = (self.x + 17, self.y + 11, 28, 52)

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not self.standing:
            if self.left:
                win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))

        self.hitbox = (self.x + 17, self.y + 11, 28, 52)
        # pg.draw.rect(win, (255, 0, 0), self.hitbox, 2)


player = Player(200, 415, 64, 64)


class Projectile(object):
    def __init__(self, posx, posy, radius, color, facing):
        self.x = posx
        self.y = posy
        self.radius = radius
        self.color = color
        self.facing = facing
        self.speed = 10

    def draw(self, win):
        pg.draw.circle(win, (0, 0, 0), (self.x, self.y), self.radius)


bullets = []


class Enemy(object):
    walkRight = [pg.image.load('R%sE.png' % frame) for frame in range(1, 12)]
    walkLeft = [pg.image.load('L%sE.png' % frame) for frame in range(1, 12)]

    def __init__(self, posx, posy, ewidth, eheight, end):
        self.x = posx
        self.y = posy
        self.width = ewidth
        self.height = eheight
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.speed = 5
        self.health = 9
        self.visible = True
        self.hitbox = (self.x + 16, self.y, 31, 57)

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0

            if self.speed > 0:
                win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            self.hitbox = (self.x + 16, self.y, 34, 57)

            pg.draw.rect(win, (200, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pg.draw.rect(win, (0, 150, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (9 - self.health)), 10))
            # pg.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def move(self):
        if self.speed > 0:
            if self.x + self.speed < self.path[1]:
                self.x += self.speed
            else:
                self.speed = self.speed * -1
                self.walkCount = 0
        elif self.speed < 0:
            if self.x - self.speed > self.path[0]:
                self.x += self.speed
            else:
                self.speed = self.speed * -1
                self.walkCount = 0

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        print("hit")


def redrawwin():
    global walkCount
    screen.blit(bg, (0, 0))
    player.draw(screen)
    goblin.draw(screen)
    text = font.render('Score: ' + str(score), 1, (0, 0, 0))
    screen.blit(text, (510, 10))

    for bullet in bullets:
        bullet.draw(screen)

    pg.display.update()


goblin = Enemy(100, 420, 64, 64, 450)
shootLoop = 0

while running:
    pg.time.delay(10)
    time.tick(27)

    if shootLoop >= 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0

    # bubble_surface = pg.Surface((50, 50))
    # pg.draw.circle(bubble_surface, (100, 100, 100), (10, 10), 10, 10)
    # screen.blit(bubble_surface, (0, 0))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False

    keys = pg.key.get_pressed()

    # bSound.play()
    if keys[pg.K_SPACE] and shootLoop == 0:
        if player.left:
            facing = -1
        elif player.right:
            facing = 1
        else:
            print("Ne right ım ne left im ben Atatürkçüyüm")

        if len(bullets) < 5:
            bullets.append(Projectile(round(player.x + player.width // 2), round(player.y + player.height // 2), 4,
(0, 0, 0), facing))
            bSound.play()

    for bullet in bullets:

        if goblin.visible:
            if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
                if bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2] and bullet.x + bullet.radius > goblin.hitbox[0]:
                    hSound.play()
                    goblin.hit()
                    score += 1
                    bullets.pop(bullets.index(bullet))

        if swidth > bullet.x > 0:
            bullet.x += bullet.speed * facing
        else:
            bullets.pop(bullets.index(bullet))

    if keys[pg.K_LEFT] and player.x > player.speed:
        player.x -= player.speed
        player.left = True
        player.right = False
        player.standing = False
    elif keys[pg.K_RIGHT] and player.x < (swidth - player.width - player.speed):
        player.x += player.speed
        player.right = True
        player.left = False
        player.standing = False
    else:
        player.standing = True
        player.walkCount = 0

    if not player.isJump:
        if keys[pg.K_UP]:
            player.isJump = True
            player.left = False
            player.right = False
            player.walkCount = 0
    else:
        if player.jumpCount >= -10:
            neg = 1
            if player.jumpCount < 0:
                neg = -1
            player.y -= (player.jumpCount ** 2) * 0.5 * neg
            player.jumpCount -= 1
        else:
            player.isJump = False
            player.jumpCount = 10

    redrawwin()

pg.quit()

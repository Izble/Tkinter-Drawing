import pygame as pg
import random as rd


class CatAnimation(pg.sprite.Sprite):
    def __init__(self):
        super(CatAnimation, self).__init__()

        self.catDead = []
        for i in range(1, 11):
            self.catDead.append(pg.image.load(('cat/dead/Dead (' + str(i) + ').png')))

        self.catFall = []
        for i in range(1, 9):
            self.catFall.append(pg.image.load(('cat/fall/Fall (' + str(i) + ').png')))

        self.catHurt = []
        for i in range(1, 11):
            self.catHurt.append(pg.image.load(('cat/hurt/Hurt (' + str(i) + ').png')))

        self.catIdle = []
        for i in range(1, 11):
            self.catIdle.append(pg.image.load(('cat/idle/Idle (' + str(i) + ').png')))

        self.catJump = []
        for i in range(1, 9):
            self.catJump.append(pg.image.load(('cat/jump/Jump (' + str(i) + ').png')))

        self.catRun = []
        for i in range(1, 9):
            self.catRun.append(pg.image.load(('cat/run/Run (' + str(i) + ').png')))

        self.catSlide = []
        for i in range(1, 11):
            self.catSlide.append(pg.image.load(('cat/slide/Slide (' + str(i) + ').png')))

        self.catWalk = []
        for i in range(1, 11):
            self.catWalk.append(pg.image.load(('cat/walk/Walk (' + str(i) + ').png')))

        self.index = 0

        self.lis = [self.catDead, self.catFall, self.catHurt, self.catIdle, self.catRun, self.catSlide, self.catWalk]
        x = rd.choice(self.lis)

        self.image = x[self.index]
        self.rect = pg.Rect(5, 5, 150, 190)

    def update(self):

        i = rd.choice(self.lis)
        self.index += 1
        if self.index >= len(i):
            self.index = 0

        self.image = i[self.index]


pg.init()
screen = pg.display.set_mode((900, 900))
sprite = CatAnimation()
group = pg.sprite.Group(sprite)

clock = pg.time.Clock()

running = True

while running:

    screen.fill((245, 102, 66))
    group.update()
    group.draw(screen)
    pg.display.update()
    clock.tick(10)

    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            pg.quit()
            running = False

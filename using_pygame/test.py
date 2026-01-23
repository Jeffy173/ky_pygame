# coding=utf-8

import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"]="1"

import pygame
import Good,Text,Music,RunGame
from typing import Union,List,Tuple

Music.init()

RunGame.Runner.PRINT=False

runner=RunGame.Runner(
    screen_size=[800,600],
    game_caption="test",
    clock_tick_framerate=60,
    auto_quit=True,
    auto_update=False,
    auto_clock_tick=True
)

screen:Union[pygame.surface.Surface,None]=None
bgmusic=Music.Music("megalovania.mp3",volume=1)
pop=Music.Sound("pop.wav",volume=1)

@runner.set_on_start
def on_start():
    global screen
    screen=runner.screen
    Good.init(screen)
    Text.init(screen)
    screen.fill("black")
    pygame.display.update()
    bgmusic.play(-1)   

class Heart(Good.Polygon):
    VX=5
    VY=5
    G=0.5
    JUMP_V=0.4

    LEFT=0
    RIGHT=800
    TOP=0
    BOTTOM=600
    CENTER_X=400
    CENTER_Y=300

    def __init__(self,points:List[Tuple[int,int]],color:any,width:int=1,filled:bool=False):
        if len(points)<3: raise ValueError("Polygon requires at least 3 points")
        self.points=points
        self.color=color
        self.width=width
        self.filled=filled
        self.rect=None
        self.min_x=min(i for i,_ in points)
        self.max_x=max(i for i,_ in points)
        self.min_y=min(i for _,i in points)
        self.max_y=max(i for _,i in points)
        self.jumping=False
        self.now_v=0
        self.slow_move_center_step=0

    def move(self,x:int,y:int):
        self.points=[(x0+x,y0+y) for x0,y0 in self.points]
        self.min_x+=x
        self.max_x+=x
        self.min_y+=y
        self.max_y+=y

    def get_center(self):
        return ((self.min_x+self.max_x)/2,(self.min_y+self.max_y)/2)

    def change_color(self):
        if heart.color=="red":
            heart.color="blue"
            self.now_v=0
            return
        if heart.color=="blue":
            heart.color="green"
            self.slow_move_center_step=10
            return
        if heart.color=="green":
            heart.color="red"
            return   

    def move_center(self):
        nowx,nowy=self.get_center()
        heart.move(Heart.CENTER_X-nowx,Heart.CENTER_Y-nowy)

    def move_save(self):
        if self.min_x<Heart.LEFT: self.move(Heart.LEFT-self.min_x,0)
        elif self.max_x>Heart.RIGHT: self.move(Heart.RIGHT-self.max_x,0)
        if self.min_y<Heart.TOP: self.move(0,Heart.TOP-self.min_y)
        elif self.max_y>Heart.BOTTOM: self.move(0,Heart.BOTTOM-self.max_y)

    def on_floor(self):
        return self.max_y>=self.BOTTOM

heart=Heart(
    points=[
        (387,288),
        (393,284),
        (398,287),
        (400,290),
        (403,287),
        (408,284),
        (413,288),
        (415,294),
        (414,300),
        (410,306),
        (405,312),
        (400,316),
        (395,312),
        (390,306),
        (387,300),
        (385,294),
    ],
    color="red",
    width=0,
    filled=True
)

def heart_slow_move_center():
    if heart.slow_move_center_step==0: return 
    nowx,nowy=heart.get_center()
    dx,dy=Heart.CENTER_X-nowx,Heart.CENTER_Y-nowy
    heart.move(dx/heart.slow_move_center_step,dy/heart.slow_move_center_step)
    heart.slow_move_center_step-=1

@runner.set_run_loop
def run_loop():
    screen.fill("black")

    for event in runner.events:
        if event.type==pygame.KEYDOWN and event.key==pygame.K_c:
            heart.change_color()
        if event.type==pygame.KEYUP and event.key==pygame.K_w:
            heart.jumping=False

    if runner.keys[pygame.K_LEFT] and runner.keys[pygame.K_RIGHT]: pass
    elif runner.keys[pygame.K_LEFT] and heart.color!="green":
        heart.move(-Heart.VX,0)
    elif runner.keys[pygame.K_RIGHT] and heart.color!="green":
        heart.move(Heart.VX,0)

    if runner.keys[pygame.K_w] and runner.keys[pygame.K_s]: pass
    elif runner.keys[pygame.K_w] and heart.color=="red":
        heart.move(0,-Heart.VY)
    elif runner.keys[pygame.K_s] and heart.color=="red":
        heart.move(0,Heart.VY)

    if heart.color=="blue":
        if heart.on_floor():
            heart.now_v=0
            if runner.keys[pygame.K_w]:
                heart.jumping=True
                heart.now_v=-Heart.VY
        else:
            heart.now_v+=Heart.G
            if heart.jumping: heart.now_v-=Heart.JUMP_V
        heart.move(0,heart.now_v)

    heart.move_save()
    heart_slow_move_center()
    heart.draw()
    pygame.display.update()

@runner.set_on_exit
def on_exit():
    bgmusic.stop()

runner.run()


# coding=utf-8

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import pygame
import old_Good
import old_Run_game
import math
from typing import List

old_Run_game.init(screen_size=[800,600],game_caption="robot_test_2")
old_Good.init(old_Run_game.screen)

class Robot:
    def __init__(self,x:int,y:int,radius:int,color:any,width:int):
        self.x=x
        self.y=y
        self.radius=radius
        self.color=color
        self.width=width
        self.head=old_Good.Circle(x,y-radius*0.75,radius/4,color,width,False)
        self.hand=old_Good.Line(x-radius/4,y-radius/4,x+radius/4,y-radius/4,color,width)
        self.body=old_Good.Line(x,y-radius/2,x,y+radius/4,color,width)
        self.leg1=old_Good.Line(x,y+radius/4,x+radius*math.cos(2/3*math.pi),y+radius*math.sin(2/3*math.pi),color,width)
        self.leg2=old_Good.Line(x,y+radius/4,x-radius*math.cos(2/3*math.pi),y+radius*math.sin(2/3*math.pi),color,width)
        self.goods:List[old_Good.Good]=[self.head,self.hand,self.leg1,self.leg2,self.body]
        self.rects=[]

    def set_color(self,color:any)->None:
        self.color=color
        for good in self.goods:
            good.color=color

    def set_width(self,width:any)->None:
        self.width=width
        for good in self.goods:
            good.width=width

    def move(self,x:int,y:int)->None:
        for good in self.goods:
            good.move(x,y)

    def spin(self,radian:float)->None:
        for good in self.goods:
            good.center_spin(self.x,self.y,radian)

    def draw(self)->None:
        self.rects=old_Good.draw_goods(self.goods)

big_circle=old_Good.Circle(400,300,200,"black",1,False)
robot=Robot(400,300,200,"blue",10)

@old_Run_game.run
def run():
    prev_rects=[]
    rects=[]
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            old_Run_game.running=False

    old_Run_game.screen.fill("white")
    robot.spin(0.01)
    big_circle.draw()
    robot.draw()
    rects=robot.rects+[big_circle.rect]
    pygame.display.update(rects+prev_rects)
    prev_rects=rects
    old_Run_game.clock.tick(60)

old_Run_game.screen.fill("white")
pygame.display.update()
run()
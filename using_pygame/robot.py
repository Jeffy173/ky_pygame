# coding=utf-8

# hide the outputed when import pygame
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"]="1"

import pygame
import sys
import time
import math
import Good
from typing import List

pygame.init()
screen=pygame.display.set_mode([800, 600])
pygame.display.set_caption("Robot Spin")
Good.init(screen)

class Robot:
    def __init__(self,x:int,y:int,radius:int,color:any,width:int):
        self.x=x
        self.y=y
        self.radius=radius
        self.color=color
        self.width=width
        self.head=Good.Circle(x,y-radius*0.75,radius/4,color,width,False)
        self.hand=Good.Line(x-radius/4,y-radius/4,x+radius/4,y-radius/4,color,width)
        self.body=Good.Line(x,y-radius/2,x,y+radius/4,color,width)
        self.leg1=Good.Line(x,y+radius/4,x+radius*math.cos(2/3*math.pi),y+radius*math.sin(2/3*math.pi),color,width)
        self.leg2=Good.Line(x,y+radius/4,x-radius*math.cos(2/3*math.pi),y+radius*math.sin(2/3*math.pi),color,width)
        self.goods:List[Good.Good]=[self.head,self.hand,self.leg1,self.leg2,self.body]
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
        self.rects=Good.draw_goods(self.goods)

screen.fill("white")
big_circle=Good.Circle(400,300,200,"black",1,False)
robot=Robot(400,300,200,"blue",10)
pygame.display.update()

clock=pygame.time.Clock()
running=True
print("game start")
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    screen.fill("white")
    robot.spin(0.01)
    big_circle.draw()
    robot.draw()
    pygame.display.update([big_circle.rect]+robot.rects)
    clock.tick(60)

print("game end")
pygame.quit()
sys.exit()
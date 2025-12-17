import pygame
import pgzrun
from typing import List

screen:any

def init(s:any):
    global screen
    screen=s

class Good:
    def draw(self):
        pass

    def move(self,x:int,y:int):
        pass

class Circle(Good):
    def __init__(self,x:int,y:int,r:int,c:any,f:bool=False):
        self.x=x
        self.y=y
        self.radius=r
        self.color=c
        self.filled=f
    
    def draw(self):
        if self.filled:screen.draw.filled_circle((self.x,self.y),self.radius,self.color)
        else: screen.draw.circle((self.x,self.y),self.radius,self.color)

    def move(self,x:int,y:int):
        self.x+=x
        self.y+=y

class Line(Good):
    def __init__(self,x1:int,y1:int,x2:int,y2:int,c:any,w:int=1):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        self.color=c
        self.width=w
    
    def draw(self):
        pygame.draw.line(screen.draw._surf,self.color,(self.x1,self.y1),(self.x2,self.y2),self.width)

    def move(self,x:int,y:int):
        self.x1+=x
        self.y1+=y
        self.x2+=x
        self.y2+=y

def draw_goods(lst:List[Good]):
    for good in lst:
        good.draw()

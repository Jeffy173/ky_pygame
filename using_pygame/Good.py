"""The module is to draw shapes with pygame easily. (without pgzero)"""
# by Jeffy

import pygame
import math
from typing import List

def init(screen:any)->None:
    Good.screen=screen

class Good:
    screen:any=None

    def draw(self)->None:
        pass

    def move(self,x:int,y:int)->None:
        pass

    def spin(self,radian:float)->None:
        pass

    def center_spin(self,x:int,y:int,radian:float)->None:
        pass

class Point(Good):
    def __init__(self,x:int,y:int,r:int,color:any):
        self.x=x
        self.y=y
        self.radius=r
        self.color=color
        self.rect=None
    
    def draw(self)->None:
        self.rect=pygame.draw.circle(
            surface=Good.screen,
            color=self.color,
            center=(self.x,self.y),
            radius=self.radius,
            width=0
        )

    def move(self,x:int,y:int)->None:
        self.x+=x
        self.y+=y

class Circle(Good):
    def __init__(self,x:int,y:int,r:int,color:any,width:int=1,filled:bool=False):
        self.x=x
        self.y=y
        self.radius=r
        self.color=color
        self.width=width
        self.filled=filled
        self.rect=None
    
    def draw(self)->None:
        if self.width==0 and not self.filled: return 
        self.rect=pygame.draw.circle(
            surface=Good.screen,
            color=self.color,
            center=(self.x,self.y),
            radius=self.radius,
            width=0 if self.filled else self.width
        )

    def move(self,x:int,y:int)->None:
        self.x+=x
        self.y+=y

class Line(Good):
    def __init__(self,x1:int,y1:int,x2:int,y2:int,color:any,width:int=1):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        self.color=color
        self.width=width
        self.rect=None
    
    def draw(self)->None:
        self.rect=pygame.draw.line(
            surface=Good.screen,
            color=self.color,
            start_pos=(self.x1,self.y1),
            end_pos=(self.x2,self.y2),
            width=self.width
        )

    def move(self,x:int,y:int)->None:
        self.x1+=x
        self.y1+=y
        self.x2+=x
        self.y2+=y

    def spin(self,radian:float)->None:
        x=(self.x1+self.x2)/2
        y=(self.y1+self.y2)/2
        dx=self.x1-self.x2
        dy=self.y1-self.y2
        rad0=math.atan2(dy,dx)
        r=math.sqrt(dx**2+dy**2)/2
        self.x1=x+r*math.cos(rad0+radian)
        self.y1=y+r*math.sin(rad0+radian)
        self.x2=x-r*math.cos(rad0+radian)
        self.y2=y-r*math.sin(rad0+radian)

    def center_spin(self,x:int,y:int,radian:float)->None:
        dx1=self.x1-x
        dy1=self.y1-y
        dx2=self.x2-x
        dy2=self.y2-y
        rad1=math.atan2(dy1,dx1)
        rad2=math.atan2(dy2,dx2)
        r1=math.sqrt(dx1**2+dy1**2)
        r2=math.sqrt(dx2**2+dy2**2)
        self.x1=x+r1*math.cos(rad1+radian)
        self.y1=y+r1*math.sin(rad1+radian)
        self.x2=x+r2*math.cos(rad2+radian)
        self.y2=y+r2*math.sin(rad2+radian)

class Square(Good):
    def __init__(self,x:int,y:int,s:int,c:any,rad:float=0,w:int=1,f:bool=False):
        self.x=x
        self.y=y
        self.side=s
        self.color=c
        self.radian=rad
        self.width=w
        self.filled=f

    def draw(self):
        points=[(self.x+self.side/2*math.cos(i*(math.pi/2)+self.radian-math.pi/4),self.y+self.side/2*math.sin(i*(math.pi/2)+self.radian-math.pi/4)) for i in range(4)]
        if self.filled: pygame.draw.polygon(screen.draw._surf,self.color,points,0)
        else: pygame.draw.polygon(screen.draw._surf,self.color,points,self.width)

    def move(self,x:int,y:int):
        self.x+=x
        self.y+=y

    def spin(self,radian:float):
        self.radian+=radian

class Rectangle(Good):
    def __init__(self,x:int,y:int,sx:int,sy:int,c:any,rad:float=0,w:int=1,f:bool=False):
        self.x=x
        self.y=y
        self.sidex=sx
        self.sidey=sy
        self.color=c
        self.radian=rad
        self.width=w
        self.filled=f

    def draw(self):
        r=math.sqrt(self.sidex**2+self.sidey**2)/2
        rad0=math.atan(self.sidey/self.sidex)
        points=[(self.x+r*math.cos(i*(math.pi/2)+rad0*(-1)**i+self.radian-math.pi/4),self.y+r*math.sin(i*(math.pi/2)+rad0*(-1)**i+self.radian-math.pi/4)) for i in range(4)]
        if self.filled: pygame.draw.polygon(screen.draw._surf,self.color,points,0)
        else: pygame.draw.polygon(screen.draw._surf,self.color,points,self.width)

    def move(self,x:int,y:int):
        self.x+=x
        self.y+=y

    def spin(self,radian:float):
        self.radian+=radian

class RegularPolygon(Good):
    def __init__(self,x:int,y:int,r:int,n:int,c:any,rad:float=0,w:int=1,f:bool=False):
        self.x=x
        self.y=y
        self.radius=r
        self.n=n
        self.color=c
        self.radian=rad
        self.width=w
        self.filled=f

    def draw(self):
        points=[(self.x+self.radius*math.cos(2*i*math.pi/self.n+self.radian),self.y+self.radius*math.sin(2*i*math.pi/self.n+self.radian)) for i in range(self.n)]
        if self.filled: pygame.draw.polygon(screen.draw._surf,self.color,points,0)
        else: pygame.draw.polygon(screen.draw._surf,self.color,points,self.width)

    def move(self,x:int,y:int):
        self.x+=x
        self.y+=y

    def spin(self,radian:float):
        self.radian+=radian
        
def draw_goods(goods:List[Good])->List[pygame.Rect]:
    rects=[]
    for good in goods:
        if good.rect is not None: rects.append(good.rect)
        good.draw()
        if good.rect is not None: rects.append(good.rect)
    return rects

def draw_goods_and_update(goods:List[Good])->None:
    rects=[]
    for good in goods:
        if good.rect is not None: rects.append(good.rect)
        good.draw()
        if good.rect is not None: rects.append(good.rect)
    pygame.display.update(rects)
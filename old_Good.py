"""The module is to draw shapes with pygame easily. (without pgzero, kwargs)"""
# by Jeffy

import Color
import pygame
import math
from typing import List,Tuple

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
    def __init__(self,x:int,y:int,radius:int,color:any):
        self.x=x
        self.y=y
        self.radius=radius
        self.color=Color.to_rgb(color)
        self.rect=None
    
    def draw(self)->None:
        if self.radius==0: return 
        self.rect=pygame.draw.circle(
            Good.screen,
            self.color,
            (self.x,self.y),
            self.radius,
            0
        )

    def move(self,x:int,y:int)->None:
        self.x+=x
        self.y+=y

    def center_spin(self,x:int,y:int,radian:float)->None:
        dx=self.x-x
        dy=self.y-y
        rad=math.atan2(dy,dx)
        r=math.hypot(dx,dy)
        self.x=x+r*math.cos(rad+radian)
        self.y=y+r*math.sin(rad+radian)

class Circle(Good):
    def __init__(self,x:int,y:int,radius:int,color:any,width:int=1,filled:bool=False):
        self.x=x
        self.y=y
        self.radius=radius
        self.color=Color.to_rgb(color)
        self.width=width
        self.filled=filled
        self.rect=None
    
    def draw(self)->None:
        if self.width==0 and not self.filled: return 
        self.rect=pygame.draw.circle(
            Good.screen,
            self.color,
            (self.x,self.y),
            self.radius,
            (0 if self.filled else self.width)
        )

    def move(self,x:int,y:int)->None:
        self.x+=x
        self.y+=y

    def center_spin(self,x:int,y:int,radian:float)->None:
        dx=self.x-x
        dy=self.y-y
        rad=math.atan2(dy,dx)
        r=math.hypot(dx,dy)
        self.x=x+r*math.cos(rad+radian)
        self.y=y+r*math.sin(rad+radian)

class Line(Good):
    def __init__(self,x1:int,y1:int,x2:int,y2:int,color:any,width:int=1):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        self.color=Color.to_rgb(color)
        self.width=width
        self.rect=None
    
    def draw(self)->None:
        if self.width==0: return 
        self.rect=pygame.draw.line(
            Good.screen,
            self.color,
            (self.x1,self.y1),
            (self.x2,self.y2),
            self.width
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
        rad=math.atan2(dy,dx)
        r=math.hypot(dx,dy)/2
        self.x1=x+r*math.cos(rad+radian)
        self.y1=y+r*math.sin(rad+radian)
        self.x2=x-r*math.cos(rad+radian)
        self.y2=y-r*math.sin(rad+radian)

    def center_spin(self,x:int,y:int,radian:float)->None:
        dx1=self.x1-x
        dy1=self.y1-y
        dx2=self.x2-x
        dy2=self.y2-y
        rad1=math.atan2(dy1,dx1)
        rad2=math.atan2(dy2,dx2)
        r1=math.hypot(dx1,dy1)
        r2=math.hypot(dx2,dy2)
        self.x1=x+r1*math.cos(rad1+radian)
        self.y1=y+r1*math.sin(rad1+radian)
        self.x2=x+r2*math.cos(rad2+radian)
        self.y2=y+r2*math.sin(rad2+radian)

class Square(Good):
    def __init__(self,x:int,y:int,side:int,color:any,radian:float=0,width:int=1,filled:bool=False):
        self.x=x
        self.y=y
        self.side=side
        self.color=Color.to_rgb(color)
        self.radian=radian
        self.width=width
        self.filled=filled
        self.rect=None

    def draw(self)->None:
        if self.width==0 and not self.filled: return 
        if self.side==0: return 
        points=[]
        r=self.side/2
        rad=self.radian-math.pi/4
        for _ in range(4):
            rad+=math.pi/2
            points.append((self.x+r*math.cos(rad),self.y+r*math.sin(rad)))
        self.rect=pygame.draw.polygon(
            Good.screen,
            self.color,
            points,
            (0 if self.filled else self.width)
        )

    def move(self,x:int,y:int)->None:
        self.x+=x
        self.y+=y

    def spin(self,radian:float)->None:
        self.radian+=radian

    def center_spin(self,x:int,y:int,radian:float)->None:
        dx=self.x-x
        dy=self.y-y
        rad=math.atan2(dy,dx)
        r=math.hypot(dx,dy)
        self.x=x+r*math.cos(rad+radian)
        self.y=y+r*math.sin(rad+radian)
        self.radian+=radian

class Rectangle(Good):
    def __init__(self,x:int,y:int,sidex:int,sidey:int,color:any,radian:float=0,width:int=1,filled:bool=False):
        self.x=x
        self.y=y
        self.sidex=sidex
        self.sidey=sidey
        self.color=Color.to_rgb(color)
        self.radian=radian
        self.width=width
        self.filled=filled
        self.rect=None

    def draw(self)->None:
        if self.width==0 and not self.filled: return 
        if self.sidex==0 or self.sidey==0: return 
        r=math.hypot(self.sidex,self.sidey)/2
        rad=math.atan2(self.sidey,self.sidex)
        points=[
            (self.x+r*math.cos(self.radian+rad),self.y+r*math.sin(self.radian+rad)),
            (self.x+r*math.cos(self.radian-rad),self.y+r*math.sin(self.radian-rad)),
            (self.x-r*math.cos(self.radian+rad),self.y-r*math.sin(self.radian+rad)),
            (self.x-r*math.cos(self.radian-rad),self.y-r*math.sin(self.radian-rad))
        ]
        self.rect=pygame.draw.polygon(
            Good.screen,
            self.color,
            points,
            (0 if self.filled else self.width)
        )

    def move(self,x:int,y:int)->None:
        self.x+=x
        self.y+=y

    def spin(self,radian:float)->None:
        self.radian+=radian

    def center_spin(self,x:int,y:int,radian:float)->None:
        dx=self.x-x
        dy=self.y-y
        rad=math.atan2(dy,dx)
        r=math.hypot(dx,dy)
        self.x=x+r*math.cos(rad+radian)
        self.y=y+r*math.sin(rad+radian)
        self.radian+=radian

class RegularPolygon(Good):
    def __init__(self,x:int,y:int,radius:int,n:int,color:any,radian:float=0,width:int=1,filled:bool=False):
        if n<3: raise ValueError("RegularPolygon requires at least 3 sides")
        self.x=x
        self.y=y
        self.radius=radius
        self.n=n
        self.color=Color.to_rgb(color)
        self.radian=radian
        self.width=width
        self.filled=filled
        self.rect=None

    def draw(self)->None:
        if self.width==0 and not self.filled: return 
        if self.radius==0: return 
        points=[(self.x+self.radius*math.cos(2*i*math.pi/self.n+self.radian),self.y+self.radius*math.sin(2*i*math.pi/self.n+self.radian)) for i in range(self.n)]
        self.rect=pygame.draw.polygon(
            Good.screen,
            self.color,
            points,
            (0 if self.filled else self.width)
        )

    def move(self,x:int,y:int)->None:
        self.x+=x
        self.y+=y

    def spin(self,radian:float)->None:
        self.radian+=radian

    def center_spin(self,x:int,y:int,radian:float)->None:
        dx=self.x-x
        dy=self.y-y
        rad=math.atan2(dy,dx)
        r=math.hypot(dx,dy)
        self.x=x+r*math.cos(rad+radian)
        self.y=y+r*math.sin(rad+radian)
        self.radian+=radian

class Polygon(Good):
    def __init__(self,points:List[Tuple[int,int]],color:any,width:int=1,filled:bool=False):
        if len(points)<3: raise ValueError("Polygon requires at least 3 points")
        self.points=points
        self.color=Color.to_rgb(color)
        self.width=width
        self.filled=filled
        self.rect=None

    def draw(self)->None:
        if self.width==0 and not self.filled: return 
        self.rect=pygame.draw.polygon(
            Good.screen,
            self.color,
            self.points,
            (0 if self.filled else self.width)
        )

    def move(self,x:int,y:int)->None:
        self.points=[(x0+x,y0+y) for x0,y0 in self.points]

    def center_spin(self,x:int,y:int,radian:float)->None:
        new_points=[]
        for x0,y0 in self.points:
            dx=x0-x
            dy=y0-y
            rad=math.atan2(dy,dx)
            r=math.hypot(dx,dy)
            new_points.append((x+r*math.cos(rad+radian),y+r*math.sin(rad+radian)))
        self.points=new_points

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



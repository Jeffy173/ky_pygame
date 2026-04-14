# coding=utf-8
"""
The module is to draw shapes with pygame easily. (without pgzero)

Author: Jeffy
"""

import pygame
import math
from . import Color
from typing import List,Tuple,Union

def init(surface:Union[pygame.surface.Surface,None])->None:
    Shape.surface=surface

class Shape:
    surface:pygame.surface.Surface=None

    def __init__(self):
        self.rect:Union[pygame.Rect,None]=None

    def draw(self,surface:Union[pygame.surface.Surface,None]=None)->None:
        pass

    def move(self,x:int,y:int)->None:
        pass

    def spin(self,radian:float)->None:
        pass

    def center_spin(self,x:int,y:int,radian:float)->None:
        pass

    def in_shape(self,x:int,y:int):
        pass

    def __str__(self):
        items=self.__dict__.items()
        cls_str=str(self.__class__).split("'")[1]
        s=f"{cls_str}(\n"
        for k,v in items:
            if k in ["rect","surface"]: continue
            s+=f"    {k}={v},\n"
        s+=")"
        return s

    def __repr__(self):
        items=self.__dict__.items()
        cls_str=str(self.__class__).split("'")[1]
        s=f"{cls_str}(\n"
        for k,v in items:
            if k in ["rect","surface"]: continue
            s+=f"    {k}={v},\n"
        s+=")"
        return s

class Point(Shape):
    def __init__(self,x:int,y:int,radius:int,color:any):
        self.x=x
        self.y=y
        self.radius=radius
        self.color=color
        self.rect=None

    def in_shape(self,x:int,y:int):
        return self.radius>=math.hypot(self.x-x,self.y-y)
    
    def draw(self,surface:Union[pygame.surface.Surface,None]=None)->None:
        if self.radius==0: return 
        self.rect=pygame.draw.circle(
            Shape.surface if surface is None else surface,
            Color.to_rgb(self.color),
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

class Circle(Shape):
    def __init__(self,x:int,y:int,radius:int,color:any,width:int=1,filled:bool=False):
        self.x=x
        self.y=y
        self.radius=radius
        self.color=color
        self.width=width
        self.filled=filled
        self.rect=None
    
    def in_shape(self,x:int,y:int):
        return self.radius>=math.hypot(self.x-x,self.y-y)

    def draw(self,surface:Union[pygame.surface.Surface,None]=None)->None:
        if self.width==0 and not self.filled: return 
        self.rect=pygame.draw.circle(
            Shape.surface if surface is None else surface,
            Color.to_rgb(self.color),
            (self.x,self.y),
            self.radius,
            0 if self.filled else self.width
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

class Line(Shape):
    def __init__(self,x1:int,y1:int,x2:int,y2:int,color:any,width:int=1):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        self.color=color
        self.width=width
        self.rect=None

    def in_shape(self,x:int,y:int):
        mid_x=(self.x1+self.x2)/2
        mid_y=(self.y1+self.y2)/2
        A1=self.y2-self.y1
        B1=self.x1-self.x2
        C1=-A1*self.x1-B1*self.y1
        A2=B1
        B2=-A1
        C2=A2*mid_x-B2*mid_y
        d1_max=self.width/2
        d2_max=math.hypot(A1,B1)/2
        d1=abs(A1*x+B1*y+C1)/math.hypot(A1,B1)
        d2=abs(A2*x+B2*y+C2)/math.hypot(A2,B2)
        return d2<=d2_max and d1<=d1_max

    def draw(self,surface:Union[pygame.surface.Surface,None]=None)->None:
        if self.width==0: return 
        self.rect=pygame.draw.line(
            Shape.surface if surface is None else surface,
            Color.to_rgb(self.color),
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

class Square(Shape):
    def __init__(self,x:int,y:int,side:int,color:any,radian:float=0,width:int=1,filled:bool=False):
        self.x=x
        self.y=y
        self.side=side
        self.color=color
        self.radian=radian
        self.width=width
        self.filled=filled
        self.rect=None

    def in_shape(self,x:int,y:int):
        rad=self.radian-math.pi/4
        d_max=self.side/2
    
        # v=(r*math.cos(rad),r*math.sin(rad))

        mid_x=(self.x1+self.x2)/2
        mid_y=(self.y1+self.y2)/2
        A1=self.y2-self.y1
        B1=self.x1-self.x2
        C1=-A1*self.x1-B1*self.y1
        A2=B1
        B2=-A1
        C2=A2*mid_x-B2*mid_y
        d1_max=self.width/2
        d2_max=math.hypot(A1,B1)/2
        d1=abs(A1*x+B1*y+C1)/math.hypot(A1,B1)
        d2=abs(A2*x+B2*y+C2)/math.hypot(A2,B2)
        return d2<=d2_max and d1<=d1_max

    def draw(self,surface:Union[pygame.surface.Surface,None]=None)->None:
        if self.width==0 and not self.filled: return 
        if self.side==0: return 
        points=[]
        r=self.side/2
        rad=self.radian-math.pi/4
        for _ in range(4):
            rad+=math.pi/2
            points.append((self.x+r*math.cos(rad),self.y+r*math.sin(rad)))
        self.rect=pygame.draw.polygon(
            Shape.surface if surface is None else surface,
            Color.to_rgb(self.color),
            points,
            0 if self.filled else self.width
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

class Rectangle(Shape):
    def __init__(self,x:int,y:int,sidex:int,sidey:int,color:any,radian:float=0,width:int=1,filled:bool=False):
        self.x=x
        self.y=y
        self.sidex=sidex
        self.sidey=sidey
        self.color=color
        self.radian=radian
        self.width=width
        self.filled=filled
        self.rect=None

    def draw(self,surface:Union[pygame.surface.Surface,None]=None)->None:
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
            Shape.surface if surface is None else surface,
            Color.to_rgb(self.color),
            points,
            0 if self.filled else self.width
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

class RegularPolygon(Shape):
    def __init__(self,x:int,y:int,radius:int,n:int,color:any,radian:float=0,width:int=1,filled:bool=False):
        if n<3: raise ValueError("RegularPolygon requires at least 3 sides")
        self.x=x
        self.y=y
        self.radius=radius
        self.n=n
        self.color=color
        self.radian=radian
        self.width=width
        self.filled=filled
        self.rect=None

    def draw(self,surface:Union[pygame.surface.Surface,None]=None)->None:
        if self.width==0 and not self.filled: return 
        if self.radius==0: return 
        points=[(self.x+self.radius*math.cos(2*i*math.pi/self.n+self.radian),self.y+self.radius*math.sin(2*i*math.pi/self.n+self.radian)) for i in range(self.n)]
        self.rect=pygame.draw.polygon(
            Shape.surface if surface is None else surface,
            Color.to_rgb(self.color),
            points,
            0 if self.filled else self.width
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

class Polygon(Shape):
    def __init__(self,points:List[Tuple[int,int]],color:any,width:int=1,filled:bool=False):
        if len(points)<3: raise ValueError("Polygon requires at least 3 points")
        self.points=points
        self.color=color
        self.width=width
        self.filled=filled
        self.rect=None

    def draw(self,surface:Union[pygame.surface.Surface,None]=None)->None:
        if self.width==0 and not self.filled: return 
        self.rect=pygame.draw.polygon(
            Shape.surface if surface is None else surface,
            Color.to_rgb(self.color),
            self.points,
            0 if self.filled else self.width
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

def draw_shapes(shapes:List[Shape],surface:Union[pygame.surface.Surface,None]=None)->List[pygame.Rect]:
    rects=[]
    for shape in shapes:
        if shape.rect is not None: rects.append(shape.rect)
        shape.draw(surface)
        if shape.rect is not None: rects.append(shape.rect)
    return rects

def draw_shapes_and_update(shapes:List[Shape],surface:Union[pygame.surface.Surface,None]=None)->None:
    rects=[]
    for shape in shapes:
        if shape.rect is not None: rects.append(shape.rect)
        shape.draw(surface)
        if shape.rect is not None: rects.append(shape.rect)
    pygame.display.update(rects)
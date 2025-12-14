import pgzrun
from typing import List

class Good:
    def draw():
        pass

class Circle(Good):
    def __init__(self,x:int,y:int,r:int,c,f:bool=False):
        self.x=x
        self.y=y
        self.radius=r
        self.color=c
        self.filled=f
    
    def draw(self):
        if self.filled:screen.draw.filled_circle((self.x,self.y),self.radius,self.color)
        else: screen.draw.circle((self.x,self.y),self.radius,self.color)

class Line(Good):
    def __init__(self,x1:int,y1:int,x2:int,y2:int,c):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        self.color=c
    
    def draw(self):
        screen.draw.line((self.x1,self.y1),(self.x2,self.y2),self.color)

def draw_goods(lst:List[Good]):
    for good in lst:
        good.draw()




WIDTH = 800
HEIGHT = 600
TITLE = "title"

c1=Circle(400,300,30,"red",True)
c2=Circle(200,200,15,"blue",True)
l1=Line(400,300,200,200,"black")

lst=[c1,c2,l1]

def draw():
    screen.fill("white")
    draw_goods(lst)

c1_vy=10
dt=0.5

def update():
    global c1_vy
    c1.y+=c1_vy*dt
    l1.y1=c1.y
    if (c1.y+c1.radius>600 and c1_vy>0) or (c1.y-c1.radius<0 and c1_vy<0): c1_vy*=-1
    
pgzrun.go()


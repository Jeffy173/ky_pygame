import pgzrun
import math
import Good
from Good import Point,Circle,Line,Square,Rectangle,RegularPolygon,draw_goods

WIDTH = 800
HEIGHT = 600
TITLE = "title"

c1=Circle(400,300,30,"red",True)
c2=Circle(200,200,15,"blue",True)
l1=Line(400,300,200,200,"black",5)
s1=Square(c1.x,c1.y,c1.radius*2*math.sqrt(2),"green",0,1,True)
r1=Rectangle(100,200,20,40,"pink",0,1,True)
l2=Line(200,400,200,200,"red",5)
six=RegularPolygon(250,250,50,6,"purple",0,5,False)

lst=[c2,l1,s1,c1,r1,l2,six]

def draw():
    Good.init(screen)
    screen.fill("white")
    draw_goods(lst)

c1_vy=10
dt=0.5

def update():
    global c1_vy
    c1.move(0,c1_vy*dt)
    s1.move(0,c1_vy*dt)
    s1.radian+=dt*0.1
    r1.radian+=dt*0.1
    l2.spin(dt*0.1)
    six.spin(dt*0.1)
    l1.y1=c1.y
    if (c1.y+c1.radius>600 and c1_vy>0) or (c1.y-c1.radius<0 and c1_vy<0): c1_vy*=-1
    
pgzrun.go()


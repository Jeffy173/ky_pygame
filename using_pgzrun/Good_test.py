import pgzrun
from Good import Good,Circle,Line,draw_goods
from Good import init as Good_init

WIDTH = 800
HEIGHT = 600
TITLE = "title"

c1=Circle(400,300,30,"red",True)
c2=Circle(200,200,15,"blue",True)
l1=Line(400,300,200,200,"black")

lst=[c1,c2,l1]

def draw():
    Good_init(screen)
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


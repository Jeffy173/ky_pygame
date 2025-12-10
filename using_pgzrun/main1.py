import pgzrun

WIDTH = 800
HEIGHT = 600
TITLE = "circle"

x1=300
y1=0
x2=0
y2=0
r=30
vx1=10
vx2=10
vy1=5
vy2=-15
dt=1
colors=["red","blue"]
count=4

def draw_circle(x,y,r,c,f=False):
    if f: screen.draw.filled_circle((x,y),r,c)
    else: screen.draw.circle((x,y),r,c)

def draw_circles(lst):
    for t in lst:
        draw_circle(*t)

def create_circles(x,y,c):
    lst=list()
    for i in range(count):
        lst.append((x,y+r*(i*2+1),r,c,True))
    return lst

def draw():
    screen.fill("white")
    lst=[]
    lst.extend(create_circles(x1,y1,colors[0]))
    lst.extend(create_circles(x2,y2,colors[1]))
    draw_circles(lst)

def update():
    global x1,y1,vx1,vy1,x2,y2,vx2,vy2
    x1+=vx1*dt
    y1+=vy1*dt
    x2+=vx2*dt
    y2+=vy2*dt

    if (x1-r<0 and vx1<0) or (x1+r>800 and vx1>0):
        vx1*=-1
        colors.reverse()

    if (y1-r<0 and vy1<0) or (y1+r*count*2>600 and vy1>0):
        vy1*=-1

    if (x2-r<0 and vx2<0) or (x2+r>800 and vx2>0):
        vx2*=-1
        colors.reverse()
    
    if (y2-r<0 and vy2<0) or (y2+r*count*2>600 and vy2>0):
        vy2*=-1

print("game start")
pgzrun.go()
print("game end")

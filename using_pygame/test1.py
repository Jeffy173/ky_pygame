import pygame
import sys
import time
import Good

pygame.init()
screen=pygame.display.set_mode([800, 600])
pygame.display.set_caption("test1")
Good.init(screen)

# screen.fill("white")
# pygame.display.update()

p=Good.Point(100,100,5,"black")
c1=Good.Circle(100,100,20,"red",5,False)
c2=Good.Circle(200,200,30,"blue",1,True)
l1=Good.Line(100,100,200,200,"pink",1)
l2=Good.Line(300,300,400,400,"green",5)
goods=[p,c1,c2,l1,l2]
Good.draw_goods_and_update(goods)

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()
            sys.exit()
    screen.fill("white")

    l1.spin(0.01)
    l2.center_spin(200,200,0.01)

    rects=Good.draw_goods(goods)
    time.sleep(0.01)
    pygame.display.update(rects)
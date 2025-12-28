# coding=utf-8
import pygame
import sys
import time
import math

# 初始化Pygame
pygame.init()

# 创建游戏窗口
screen=pygame.display.set_mode([800, 600])  # 设定窗口大小[citation:8]
pygame.display.set_caption("My Pygame")  # 设置窗口标题

t=0

# screen.fill("white")

# 游戏主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    screen.fill("white")
    pygame.draw.circle(
        surface=screen,
        center=(400,300),
        color="black",
        radius=200,
        width=1
    )
    pygame.draw.circle(
        surface=screen,
        center=(400-150*math.sin(t),300-150*math.cos(t)),
        color="blue",
        radius=50,
        width=10
    )
    # hand
    hand_r=math.sqrt((100*(math.sqrt(3)-1))**2+25**2)
    hand_t=math.atan((25/(100*(math.sqrt(3)-1))))
    pygame.draw.line(
        surface=screen,
        color="blue",
        width=10,
        start_pos=(400+hand_r*math.cos(hand_t+t),300-hand_r*math.sin(hand_t+t)),
        end_pos=(400-hand_r*math.cos(-hand_t+t),300+hand_r*math.sin(-hand_t+t))
    )
    #leg1
    leg1_r1=200
    leg1_r2=50
    leg1_t1=-math.pi/3
    leg1_t2=-math.pi/2
    pygame.draw.line(
        surface=screen,
        color="blue",
        width=10,
        start_pos=(400+leg1_r1*math.cos(t+leg1_t1),300-leg1_r1*math.sin(t+leg1_t1)),
        end_pos=(400+leg1_r2*math.cos(t+leg1_t2),300-leg1_r2*math.sin(t+leg1_t2))
    )
    #leg2
    leg2_r1=200
    leg2_r2=50
    leg2_t1=-2*math.pi/3
    leg2_t2=-math.pi/2
    pygame.draw.line(
        surface=screen,
        color="blue",
        width=10,
        start_pos=(400+leg2_r1*math.cos(t+leg2_t1),300-leg2_r1*math.sin(t+leg2_t1)),
        end_pos=(400+leg2_r2*math.cos(t+leg2_t2),300-leg2_r2*math.sin(t+leg2_t2))
    )
    # body
    body_r1=100
    body_r2=50
    body_t1=math.pi/2
    body_t2=-math.pi/2
    pygame.draw.line(
        surface=screen,
        color="blue",
        width=10,
        start_pos=(400+body_r1*math.cos(t+body_t1),300-body_r1*math.sin(t+body_t1)),
        end_pos=(400+body_r2*math.cos(t+body_t2),300-body_r2*math.sin(t+body_t2))
    )
    t+=0.01
    time.sleep(0.01)
    pygame.display.update()
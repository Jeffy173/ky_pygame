import pgzrun
import random
import pygame
from typing import Tuple


def draw_circle(color: Tuple[int, int, int], center: Tuple[int, int], radius: int, width: int = 1):
    return pygame.draw.circle(
        screen.surface,
        color,               # color
        center,              # center
        radius,              # radius
        width                # width
    )


def draw():
    screen.fill("white")
    for i in range(50):
        draw_circle(
            color=(random.randint(0,255),random.randint(0,255),random.randint(0,255)),
            center=(400, 300),
            radius=i*5+5,
            width=5
        )


# def update():
#     pass

def on_mouse_down():
    draw()

pgzrun.go()

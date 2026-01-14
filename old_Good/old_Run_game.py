# coding=utf-8
"""The module is to run game with pygame easily. (without pgzero)"""
# by Jeffy

import sys
import pygame
from typing import List,Callable

pygame.init()
clock=pygame.time.Clock()
screen:any
running=False

def init(screen_size:List[int]=[800,600],game_caption:str="game"):
    global screen,clock
    screen=pygame.display.set_mode(screen_size)
    pygame.display.set_caption(game_caption)

def run(func:Callable):
    def wrapper(*args,**kwargs):
        global running
        running=True
        print("game start")
        while running:
            func(*args,**kwargs)
        print("game end")
        pygame.quit()
        sys.exit()
    return wrapper

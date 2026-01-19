# coding=utf-8
"""The module is to run game with pygame easily. (without pgzero)

Example:
    >>> 
    >>> import pygame
    >>> import RunGame
    >>> 
    >>> RunGame.init(screen_size=[800,600],game_caption="Text_test")
    >>> pygame.init()
    >>> screen=Rungame.screen
    >>> 
    >>> ...

Author: Jeffy
"""

import pygame
from typing import List,Callable

pygame.init()

class Runner:
    clock:pygame.time.Clock=pygame.time.Clock()
    PRINT:bool=False

    @classmethod
    def clock_tick(cls,framerate:float=0)->int:
        return cls.clock.tick(framerate)

    def __init__(self,screen_size:List[int]=[800,600],game_caption:str="game",clock_tick_framerate:float=60):
        self.screen=None
        self.screen_size=screen_size
        self.game_caption=game_caption
        self.running=False
        self.clock_tick_framerate=clock_tick_framerate
        self.update_list:List[pygame.Rect]=[]
        self.on_start=None
        self.run_loop=None
        self.on_exit=None

    def set_on_start(self,func:Callable):
        self.on_start=func
        return func

    def set_run_loop(self,func:Callable):
        def wrapper(*args,**kwargs):
            break_run=False
            while self.running:
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        self.end_running()
                        break_run=True
                        
                if break_run: break
                func(*args,**kwargs)

                pygame.display.update(self.update_list)
                self.update_list=[]
                Runner.clock_tick(self.clock_tick_framerate)
        self.run_loop=wrapper
        return wrapper
    
    def set_on_exit(self,func:Callable):
        self.on_exit=func
        return func

    def run(self,*args,**kwargs):
        self.screen=pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption(self.game_caption)
        self.running=True
        if Runner.PRINT: print("game start")
        if self.on_start is not None: self.on_start()
        if self.run_loop is not None: self.run_loop(*args,**kwargs)

    def end_running(self):
        self.running=False
        if Runner.PRINT: print("game end")
        if self.on_exit is not None: self.on_exit()
        pygame.display.quit()

    def __enter__(self):
        self.run()
        return self

    def __exit__(self,exc_type,exc_val,exc_tb):
        self.end_running()
        return False


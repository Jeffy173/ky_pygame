# coding=utf-8
"""
The module is to draw button with pygame easily. (without pgzero)

Author: Jeffy
"""

from typing import Union
import pygame
from . import Shape

def init(surface:Union[pygame.surface.Surface,None])->None:
    Button.surface=surface

class Button:
    surface:pygame.surface.Surface=None

    def __init__(self,shape:Shape.Shape,focus_shape:Union[Shape.Shape,None]=None,down_shape:Union[Shape.Shape,None]=None):
        self.shape=shape
        self.focus_shape=focus_shape
        self.down_shape=down_shape

    def on_focus(self):
        mouse_pos=pygame.mouse.get_pos()
        result=self.shape.in_shape(*mouse_pos)
        if result is not None:return result
        new_surface=pygame.Surface(Button.surface.get_size())
        self.shape.draw(new_surface)
        return self.shape.rect.collidepoint(mouse_pos)

    def on_click(self):
        pass

    def draw(self,surface:Union[pygame.surface.Surface,None]=None)->None:
        pass

    def move(self,x:int,y:int)->None:
        pass

    def spin(self,radian:float)->None:
        pass

    def center_spin(self,x:int,y:int,radian:float)->None:
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




















# coding=utf-8
"""
The module is to draw Image with pygame easily. (without pgzero)

Example:
    >>> 
    >>> import pygame
    >>> import Image
    >>> ...
    >>> 
Author: Jeffy
"""

import pygame
from typing import Union

def init(surface:pygame.surface.Surface)->None:
    Image.surface=surface

class Image:
    surface:Union[pygame.surface.Surface,None]=None

    def __init__(self,x:int,y:int,image_path:str,width:Union[int,None]=None,height:Union[int,None]=None):
        self.image_surface=pygame.image.load(image_path)
        self.x=x
        self.y=y
        if width is None and height is None:
            self.width,self.height=self.image_surface.get_size()
        else:
            if width is None:
                self.height=height
                w,h=self.image_surface.get_size()
                self.width=self.height*w//h
            elif height is None:
                self.width=width
                w,h=self.image_surface.get_size()
                self.height=self.width*h//w
            else:
                self.width=width
                self.height=height
            self.set_size(self.width,self.height)
        self.rect=None

    def set_image(self,image_path:str,width:Union[int,None]=None,height:Union[int,None]=None):
        self.image_surface=pygame.image.load(image_path)
        if width is None and height is None:
            self.width,self.height=self.image_surface.get_size()
        else:
            if width is None:
                self.height=height
                w,h=self.image_surface.get_size()
                self.width=self.height*w//h
            elif height is None:
                self.width=width
                w,h=self.image_surface.get_size()
                self.height=self.width*h//w
            else:
                self.width=width
                self.height=height
            self.set_size(self.width,self.height)
        self.rect=None

    def move(self,x:int,y:int)->None:
        self.x+=x
        self.y+=y

    def sub_surface(self,x1:int,y1:int,x2:int,y2:int)->pygame.surface.Surface:
        x1,x2=sorted((x1,x2))
        y1,y2=sorted((y1,y2))
        return self.image_surface.subsurface(pygame.Rect(x1,y1,x2-x1,y2-y1))

    def copy(self)->"Image":
        new_image=Image.__new__(Image)
        new_image.image_surface=self.image_surface.copy()
        new_image.x=self.x
        new_image.y=self.y
        new_image.width=self.width
        new_image.height=self.height
        new_image.rect=self.rect.copy()
        return new_image
        
    def set_size(self,width:int,height:int)->None:
        self.width=width
        self.height=height
        self.image_surface=pygame.transform.scale(self.image_surface,(width,height))
    
    def draw(self,surface:Union[pygame.surface.Surface,None]=None)->None:
        if surface is None and Image.surface is None: raise ValueError("surface is still None, please offer a surface or call Image.init(surface) first")
        self.rect=(Image.surface if surface is None else surface).blit(
            source=self.image_surface,
            dest=(self.x-self.width/2,self.y-self.height/2),
            area=None,
            special_flags=0
        )

    def __str__(self):
        items=self.__dict__.items()
        cls_str=str(self.__class__).split("'")[1]
        s=f"{cls_str}(\n"
        for k,v in items:
            s+=f"    {k}={v},\n"
        s+=")"
        return s

    def __repr__(self):
        items=self.__dict__.items()
        cls_str=str(self.__class__).split("'")[1]
        s=f"{cls_str}(\n"
        for k,v in items:
            s+=f"    {k}={v},\n"
        s+=")"
        return s

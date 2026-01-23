"""The module is to draw Text with pygame easily. (without pgzero)

Example:
    >>> 
    >>> import pygame
    >>> import Text
    >>>  
    >>> pygame.init()
    >>> screen=pygame.display.set_mode([800,600])
    >>> Text.init(screen)
    >>> 
    >>> text=Text.Text(
    >>>     x=400,
    >>>     y=300,
    >>>     text="Hello",
    >>>     size=36,
    >>>     color="red"
    >>> )
    >>> 
    >>> # Draw to default surface
    >>> text.draw()
    >>> 
    >>> # Update text
    >>> text.set_text("World")
    >>> text.set_color("blue")
    >>> text.draw()

Author: Jeffy
"""

import pygame
from typing import Any,Tuple

def init(surface:pygame.surface.Surface)->None:
    """
    set default surface
    
    :param surface: the default surface while call draw without offer surface
    :type surface: pygame.surface.Surface
    """
    Text.surface=surface

class Text:
    surface:pygame.surface.Surface|None=None

    def __init__(self,x:int,y:int,text:str,size:int,font_name:str|None=None,bold:bool=False,italic:bool=False,underline:bool=False,antialias:bool=False,color:Any="black",background_color:Any=None):
        self.font=pygame.font.Font(font_name,size)
        self.font.bold=bold
        self.font.italic=italic
        self.font.underline=underline

        self.x=x
        self.y=y
        self.text=text
        self.size=size
        self.font_name=font_name
        self.antialias=antialias
        self.color=color
        self.background_color=None if background_color is None else background_color
        self.set_text_surface()
        self.rect=None

    def set_size(self,size:int)->None:
        self.size=size
        font=pygame.font.Font(self.font_name,size)
        font.bold=self.font.bold
        font.italic=self.font.italic
        font.underline=self.font.underline
        self.font=font
        self.set_text_surface()

    def set_text(self,text:str)->None:
        self.text=text
        self.set_text_surface()

    def set_color(self,color:Any)->None:
        self.color=color
        self.set_text_surface()
    
    def set_antialias(self,antialias:bool)->None:
        self.antialias=antialias
        self.set_text_surface()

    def set_background_color(self,background_color:Any)->None:
        self.background_color=None if background_color is None else background_color
        self.set_text_surface()

    def set_text_surface(self)->None:
        """
        create a surface to genorate a Rect object
        """
        self.text_surface=self.font.render(
            self.text,
            self.antialias,
            self.color,
            self.background_color
        )

    def get_size(self)->Tuple[int,int]:
        """
        get the size of the Rect object

        :return: (width,height)
        :rtype: Tuple[int, int]
        """
        return self.text_surface.get_size()
    
    def draw(self,surface:pygame.surface.Surface|None=None)->None:
        """
        draw the text and update the rect 
        
        :param surface: surface, it will be default surface if not offer
        :type surface: pygame.surface.Surface | None
        """
        width,height=self.get_size()
        if surface is None and Text.surface is None: raise ValueError("surface is still None, please offer a surface or call Text.init(surface) first")
        self.rect=(Text.surface if surface is None else surface).blit(
            source=self.text_surface,
            dest=(self.x-width/2,self.y-height/2),
            area=None,
            special_flags=0
        )

    def __str__(self):
        items=self.__dict__.items()
        cls_str=str(self.__class__).split("'")[1]
        s=f"{cls_str}(\n"
        for k,v in items:
            if k in ["rect","font","text_surface"]: continue
            if k=="text":
                s+=f"    text={repr(v)},\n"
                continue
            s+=f"    {k}={v},\n"
        s+=")"
        return s

    def __repr__(self):
        items=self.__dict__.items()
        cls_str=str(self.__class__).split("'")[1]
        s=f"{cls_str}(\n"
        for k,v in items:
            if k in ["rect","font","text_surface"]: continue
            if k=="text":
                s+=f"    text={repr(v)},\n"
                continue
            s+=f"    {k}={v},\n"
        s+=")"
        return s

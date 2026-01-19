# coding=utf-8
"""
RunGame - A Pygame Game Development Framework Module

This module provides a flexible game runner that allows control over automation features
like event handling, display updates, and frame rate management, while maintaining
compatibility with the native Pygame API.

Main Features:
1. Three-level automation control: Independent control over event handling, display updates, and frame rate management
2. Event passing mechanism: Automatically passes each frame's events to the main loop function
3. Safe context management: Supports `with` statements with automatic resource cleanup
4. Extensible callback system: Provides callback functions for start, execution, and exit phases
5. Backward compatibility: Maintains compatibility with native Pygame API

Usage Example:
    >>> 
    >>> import pygame
    >>> import RunGame
    >>> 
    >>> # Create game runner
    >>> runner = RunGame.Runner(
    >>>     screen_size=[800, 600],
    >>>     game_caption="My Game",
    >>>     clock_tick_framerate=60,
    >>>     auto_quit=True,
    >>>     auto_update=True,
    >>>     auto_clock_tick=True
    >>> )
    >>> 
    >>> # Enable debug output
    >>> RunGame.Runner.PRINT = True
    >>> 
    >>> @runner.set_on_start
    >>> def on_start():
    >>>     print("Game starting!")
    >>>     # Initialize resources here
    >>> 
    >>> @runner.set_run_loop
    >>> def run():
    >>>     # Main game loop
    >>>     for event in runner.events:
    >>>         if event.type == pygame.KEYDOWN:
    >>>             print(f"Key pressed: {pygame.key.name(event.key)}")
    >>> 
    >>>     runner.screen.fill((0, 0, 0))
    >>>     pygame.draw.circle(runner.screen, (255, 0, 0), (400, 300), 50)
    >>> 
    >>> @runner.set_on_exit
    >>> def on_exit():
    >>>     print("Game ending!")
    >>>     # Clean up resources here
    >>> 
    >>> # Run the game
    >>> runner.run()

Author: Jeffy
License: MIT
"""

import pygame
from typing import List,Callable

pygame.init()

class Runner:
    """
    Game runner class
    
    Provides flexible game loop management with customizable automation features.
    
    Attributes:
        clock (pygame.time.Clock): Game clock object
        PRINT (bool): Whether to output debug information (class attribute)
        screen (pygame.Surface): Main game display surface
        events (List[pygame.Event]): Current frame's event list
        running (bool): Whether the game is currently running
        update_list (List[pygame.Rect]): List of areas to update
    """
    
    clock:pygame.time.Clock=pygame.time.Clock()
    PRINT:bool=False

    @classmethod
    def clock_tick(cls,framerate:float=0)->int:
        """
        Control game frame rate
        
        Args:
            framerate (float): Target frame rate, 0 means unlimited
        
        Returns:
            int: Milliseconds since last frame
        """
        return cls.clock.tick(framerate)

    def __init__(self,screen_size:List[int]=[800,600],game_caption:str="game",clock_tick_framerate:float=60,auto_quit:bool=True,auto_update:bool=True,auto_clock_tick:bool=True):
        """
        Initialize game runner
        
        Args:
            screen_size (List[int]): Window size [width, height], default [800, 600]
            game_caption (str): Window title, default "game"
            clock_tick_framerate (float): Target frame rate (FPS), default 60
            auto_quit (bool): Whether to automatically handle quit events, default True
            auto_update (bool): Whether to automatically update display, default True
            auto_clock_tick (bool): Whether to automatically control frame rate, default True
        """
        self.screen=None
        self.screen_size=screen_size
        self.game_caption=game_caption
        self.running=False
        self.clock_tick_framerate=clock_tick_framerate
        self.update_list:List[pygame.Rect]=[]
        self.on_start=None
        self.run_loop=None
        self.on_exit=None
        self.auto_quit=auto_quit
        self.auto_update=auto_update
        self.auto_clock_tick=auto_clock_tick

    def set_on_start(self,func:Callable):
        """
        Set callback function for game start
        
        Args:
            func (Callable): Start callback function
        
        Returns:
            Callable: Original function (supports decorator syntax)
        """
        self.on_start=func
        return func

    def set_run_loop(self,func:Callable):
        """
        Set main game loop function
        
        Args:
            func (Callable): Main loop function
        
        Returns:
            Callable: Wrapped function (supports decorator syntax)
        
        Note:
            The main loop function will be called each frame. Access current frame's
            events through runner.events
        """
        def wrapper(*args,**kwargs):
            while self.running:
                self.events=pygame.event.get()

                if self.auto_quit: 
                    break_run=False
                    for event in self.events:
                        if event.type==pygame.QUIT:
                            self.end_running()
                            break_run=True
                    if break_run: break

                func(*args,**kwargs)

                if self.auto_update:
                    pygame.display.update(self.update_list)
                    self.update_list=[]

                if self.auto_clock_tick: Runner.clock_tick(self.clock_tick_framerate)

        self.run_loop=wrapper
        return wrapper
    
    def set_on_exit(self,func:Callable):
        """
        Set callback function for game exit
        
        Args:
            func (Callable): Exit callback function
        
        Returns:
            Callable: Original function (supports decorator syntax)
        """
        self.on_exit=func
        return func

    def run(self,*args,**kwargs):
        self.screen=pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption(self.game_caption)
        self.running=True
        self.events=[]
        if Runner.PRINT: print("game start")
        if self.on_start is not None: self.on_start()
        if self.run_loop is not None: self.run_loop(*args,**kwargs)

    def end_running(self):
        """
        Safely end game execution
        
        Note:
            This method calls the exit callback function and cleans up resources
        """
        self.running=False
        if Runner.PRINT: print("game end")
        if self.on_exit is not None: self.on_exit()
        pygame.display.quit()
        self.screen=None

    def __enter__(self):
        """
        Context manager entry
        
        Returns:
            Runner: Self instance
        """
        self.run()
        return self

    def __exit__(self,exc_type,exc_val,exc_tb):
        """
        Context manager exit
        
        Args:
            exc_type: Exception type
            exc_val: Exception value
            exc_tb: Exception traceback
        
        Returns:
            bool: Whether to suppress exceptions (False means don't suppress)
        """
        if self.screen is not None: self.end_running()
        return False

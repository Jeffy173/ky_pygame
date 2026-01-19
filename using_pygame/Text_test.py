import pygame
import Text
import RunGame
import time

runner1=RunGame.Runner(screen_size=[800,600],game_caption="game1")
screen1:pygame.surface.Surface=None

RunGame.Runner.PRINT=True

text1=Text.Text(
    x=400,
    y=300,
    text="Hello World",
    color="red",
    antialias=True,
    size=100
)

@runner1.set_on_start
def on_start1():
    global screen1
    screen1=runner1.screen
    Text.init(screen1)
    screen1.fill("white")
    pygame.display.update()

@runner1.set_run_loop
def run1():
    screen1.fill("white")
    text1.draw()
    runner1.update_list.append(text1.rect)

runner1.run()
time.sleep(1)
runner1.run()
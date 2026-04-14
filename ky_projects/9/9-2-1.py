import os
import sys
sys.path.insert(0,os.path.dirname(__file__))
script_dir=os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# block.s=20

# # snkaeHead = Actor('snake1')  # 导入蛇头方块图片
# snkaeHead.x = WIDTH/2   # 蛇头方块图片的x坐标
# snkaeHead.y = HEIGHT/2  # 蛇头方块图片的y坐标

# Snake = []  # 存储蛇的列表
# Snake.append(snkaeHead)  # 把蛇头加入到列表中

# for i in range(4):  # 再为蛇添加4段蛇身
#     snakebody = Actor('snake1')  # 导入蛇身方块图片
#     snakebody.x = Snake[i].x - TILE_SIZE  # 蛇身方块图片的x坐标
#     snakebody.y = Snake[i].y  # 蛇身方块图片的y坐标
#     Snake.append(snakebody)   # 把蛇身加入到列表中

# def draw():  # 绘制模块，每帧重复执行
#     screen.clear()  # 每帧清除屏幕，便于重新绘制
#     for snkaebody in Snake:  # 绘制蛇
#         snkaebody.draw()

# def update():  # 更新模块，每帧重复操作
#     newSnakeHead = Actor('snake1') # 创建新蛇头的图片
#     # 设定新蛇头的坐标，小蛇向右移动，在旧蛇头的右边
#     newSnakeHead.x = Snake[0].x + TILE_SIZE
#     newSnakeHead.y = Snake[0].y
#     Snake.insert(0, newSnakeHead) # 把新蛇头加到列表的最前面
#     del Snake[len(Snake)-1] # 删除掉旧蛇尾


# coding=utf-8
import pygame
from typing import List,Tuple,Optional
from PygameSimple import Color,Good,Music,RunGame,Text,Image

Music.init()
RunGame.Runner.PRINT=False

screen:Optional[pygame.surface.Surface]=None
bgmusic=Music.Music("megalovania.mp3",volume=1)
endmusic=Music.Music("determination.mp3",volume=1)
pop=Music.Sound("pop.wav",volume=1)
heartbreak=Music.Sound("heartbreak.wav",volume=1)
heartbreak_length=heartbreak.sound.get_length()
heartbreak_runtimes=int(heartbreak_length*60)

score=100
snake_head=Image.Image(
    x=400,
    y=300,
    image_path="images/snake1.jpg",
    width=20,
    height=20
)
cookie=Image.Image(
    x=100,
    y=300,
    image_path="images/cookie.jpg",
    width=20,
    height=20
)
direction=(1,0)
move_tick=20
now_move_tick=0

def snake_out(snake):
    return not(snake.x>=0+10 and snake.x<=800-10 and  snake.y>=0+10 and snake.y<=600-10)

def eat_cookie(snake_head,cookie):
    return snake_head.x==cookie.x and snake_head.y==cookie.y

runner=RunGame.Runner(
    screen_size=[800,600],
    game_caption="snack",
    clock_tick_framerate=60,
    auto_update=False,
)
end_runner=RunGame.Runner(
    screen_size=[800,600],
    game_caption="snack_game_over",
    clock_tick_framerate=60,
    auto_update=False,
)

# main loop(game)
@runner.set_on_start
def on_start():
    global screen,score
    screen=runner.screen
    Good.init(screen)
    Text.init(screen)
    Image.init(screen)
    screen.fill("black")
    pygame.display.update()
    bgmusic.play(-1)

    score=0

@runner.set_run_loop
def run_loop():
    global score,direction,now_move_tick,move_tick
    for event in runner.events:
        if event.type==pygame.KEYDOWN:
            # print(f"Key pressed:{pygame.key.name(event.key)}")
            if event.key==pygame.K_DOWN:
                direction=(0,1)
            elif event.key==pygame.K_UP:
                direction=(0,-1)
            elif event.key==pygame.K_LEFT:
                direction=(-1,0)
            elif event.key==pygame.K_RIGHT:
                direction=(1,0)
    screen.fill("black")
    # move
    now_move_tick+=1
    if now_move_tick==move_tick:
        now_move_tick=0
        snake_head.move(*(20*i for i in direction))
        if snake_out(snake_head):
            snake_head.move(*(-20*i for i in direction))
            runner.end_running()
        if eat_cookie(snake_head,cookie):
            score+=1
            pop.play()
    # draw
    cookie.draw()
    snake_head.draw()
    pygame.display.update()
    
@runner.set_on_exit
def on_exit():
    global screen
    bgmusic.stop()
    heartbreak.play()

    snake_head.set_image("images/snake2.jpg",width=20,height=20)
    screen.fill("black")
    snake_head.draw()
    pygame.display.update()
    change_color_times=int(heartbreak_runtimes*0.4)
    pygame.time.wait(int(change_color_times*1000/60))

    rest=heartbreak_runtimes-change_color_times
    t=rest*0.7
    vy=-5
    s=800 # s=vy*t+0.5*a*t**2
    a=(s-vy*t)*2/(t**2)
    for _ in range(rest):
        vy+=a*1
        snake_head.move(0,vy)
        screen.fill("black")
        snake_head.draw()
        pygame.display.update()
        RunGame.Runner.clock_tick(60)
        
    screen=None
    end_runner.run()

# game over
@end_runner.set_on_start
def end_on_start():
    end_runner.screen.fill("black")
    Text.Text(
        x=400,
        y=300,
        text="Game Over",
        size=150,
        color="red"
    ).draw(end_runner.screen)
    Text.Text(
        x=400,
        y=400,
        text=f"Score:{score}",
        size=80,
        color="white"
    ).draw(end_runner.screen)
    pygame.display.update()
    endmusic.play(-1)

@end_runner.set_run_loop
def end_run_loop():
    pass
    # for event in end_runner.events:
        # if event.type==pygame.MOUSEBUTTONUP and on_button(button)
            # runner.run()
    
@end_runner.set_on_exit
def on_exit():
    endmusic.stop()

runner.run()

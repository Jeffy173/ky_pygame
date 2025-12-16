import pygame
import pgzrun

# --- 音乐初始化与加载 (通常放在代码靠前的位置) ---
# 注意：确保你的音乐文件（如bg_music.mp3）与Python脚本在同一目录下，或者使用正确的文件路径。
pygame.mixer.init()  # 初始化混音器[citation:2]
pygame.mixer.music.load('megalovania.mp3')  # 加载背景音乐文件[citation:1][citation:4]
pygame.mixer.music.play(-1)  # 开始播放，-1代表循环播放[citation:1][citation:2]
pygame.mixer.music.set_volume(1)  # 可选项：设置音量（0.0到1.0之间）[citation:3][citation:4]


# 2. 加载音效文件，例如一个“pop”声
# 确保有一个名为 'pop.wav' 的音效文件在项目目录中
pop_sound = pygame.mixer.Sound('pop.wav')
pop_sound.set_volume(1)  # 可单独调节音效音量

from typing import List

class Good:
    def draw():
        pass

class Circle(Good):
    def __init__(self,x:int,y:int,r:int,c,f:bool=False):
        self.x=x
        self.y=y
        self.radius=r
        self.color=c
        self.filled=f
    
    def draw(self):
        if self.filled:screen.draw.filled_circle((self.x,self.y),self.radius,self.color)
        else: screen.draw.circle((self.x,self.y),self.radius,self.color)

class Line(Good):
    def __init__(self,x1:int,y1:int,x2:int,y2:int,c:any,w:int=1):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
        self.color=c
        self.width=w
    
    # @staticmethod
    # def make_color(arg):
    #     if isinstance(arg, tuple):
    #         return arg
    #     elif isinstance(arg, str):
    #         # 将颜色字符串转换为RGB元组
    #         return tuple(pygame.Color(arg))[:3]  # 只取RGB，忽略alpha
    #     else:
    #         return arg

    def draw(self):
        # screen.draw.line((self.x1,self.y1),(self.x2,self.y2),self.color,self.width)
        pygame.draw.line(screen.draw._surf,self.color,(self.x1,self.y1),(self.x2,self.y2),self.width)

def draw_goods(lst:List[Good]):
    for good in lst:
        good.draw()




WIDTH = 800
HEIGHT = 600
TITLE = "title"

c1=Circle(400,300,30,"red",True)
c2=Circle(200,200,15,"blue",True)
l1=Line(400,300,200,200,"black")

lst=[c1,c2,l1]

def draw():
    screen.fill("white")
    draw_goods(lst)

c1_vy=10
dt=0.5

def update():
    global c1_vy
    c1.y+=c1_vy*dt
    l1.y1=c1.y
    if (c1.y+c1.radius>600 and c1_vy>0) or (c1.y-c1.radius<0 and c1_vy<0): c1_vy*=-1;pop_sound.play()

pgzrun.go()
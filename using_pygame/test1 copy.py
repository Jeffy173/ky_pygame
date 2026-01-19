# coding:utf-8
import pygame
import time

pygame.init()
# 第一个窗口
screen = pygame.display.set_mode((800, 600))
screen.fill((255, 0, 0))
pygame.display.flip()
print("第一个窗口打开")
time.sleep(2)  # 等待2秒

# 关闭显示模块
pygame.display.quit()
print("显示模块已关闭，窗口消失")
time.sleep(2)

# 重新初始化显示模块，创建第二个窗口
screen = pygame.display.set_mode((400, 300))
screen.fill((0, 0, 255))
pygame.display.flip()
print("第二个窗口打开")
time.sleep(2)

pygame.quit()
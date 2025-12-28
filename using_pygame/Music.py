# coding=utf-8
"""The module is to play music and sound with pygame easily. (without pgzero)"""
import pygame

pygame.mixer.init()

# 操作      函数	                            说明
# 暂停播放	pygame.mixer.music.pause()	        pause
# 继续播放	pygame.mixer.music.unpause()	    continue
# 停止播放	pygame.mixer.music.stop()	        stop, have to load again next time
# 音量淡出	pygame.mixer.music.fadeout(time)	stop in {time} ms (漸變)
# 检查状态	pygame.mixer.music.get_busy()	    playing?

# pygame.mixer.music.load('megalovania.mp3')
# pygame.mixer.music.play(-1)  # -1 means play looping
# pygame.mixer.music.set_volume(1)  # between 0 and 1

class Music:
    def __init__(self,url:str|None=None,volume:float=1):
        """background music, url format : music.mp3"""
        if url is not None: pygame.mixer.music.load(url)
        self.volume=volume
        pygame.mixer.music.set_volume(volume)
    
    def load(self,url:str):
        self.url=url
        pygame.mixer.music.load(url)
    
    def play(self,loops:int=0,start:float=0,fade_ms:int=0):
        pygame.mixer.music.play(loops,start,fade_ms)

    def pause(self):
        pygame.mixer.music.pause()

    def unpause(self):
        pygame.mixer.music.unpause()

    def stop(self):
        pygame.mixer.music.stop()

    def fadeout(self,time):
        pygame.mixer.music.fadeout(time)

    def get_busy(self):
        pygame.mixer.music.get_busy()

class Sound:
    def __init__(self,url:str,volume:float=1):
        """short sound, url format : file.wav"""
        self.sound=pygame.mixer.Sound(url)
        self.volume=volume
        self.sound.set_volume(volume)
    
    def play(self):
        self.sound.play()

# bgmusic=Music("megalovania.mp3",volume=1)
# pop=Sound("pop.wav",volume=1)

# pop.play()
# bgmusic.play(-1)
# bgmusic.pause()
# bgmusic.unpause()
# bgmusic.stop()



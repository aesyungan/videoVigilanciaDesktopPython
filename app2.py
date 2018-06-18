#!/usr/bin/python
import os
import pygame, sys

from pygame.locals import *
import pygame.camera
import time
width = 640
height = 480

#initialise pygame   
pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0",(width,height))
cam.start()

#setup window
windowSurfaceObj = pygame.display.set_mode((width,height),1,16)
pygame.display.set_caption('Camera')
#display the picture
#contador
num=0
while True:
    num=num+1
    image = cam.get_image()
    catSurfaceObj = image
    windowSurfaceObj.blit(catSurfaceObj,(0,0))
    pygame.display.update()
    print("N:")
    print(num)
    time.sleep(.30)
print("temino el programa")
cam.stop()
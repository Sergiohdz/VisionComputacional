#!/usr/bin/python

import pygame
from pygame.locals import *
import os, sys
import Image

im = Image.open("imagen.jpg")
for x in range(0,900): #Ancho
  for y in range(0,600): #Largo
		pix = im.load()
		
pygame.init()
ventana=pygame.display.set_mode((900,600))
imagen=pygame.image.load("imagen.jpg")
ventana.blit(imagen,(0,0))
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

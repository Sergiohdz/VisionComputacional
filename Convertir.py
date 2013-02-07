#!/usr/bin/python

import pygame
from pygame.locals import *
import Image


pygame.init()
ventana=pygame.display.set_mode((1024,768))
imagen=pygame.image.load("imagen.jpg")
ventana.blit(imagen,(0,0))
pygame.display.update()

		
im = Image.open("imagen.jpg")
pix = im.load()
for x in range(0,1024): #Ancho
	for y in range(0,768): #Largo
		(r,g,b) = pix[x,y] 
		promedio=(r+g+b)/3
		pix[x,y] =(promedio,promedio,promedio)
im.save('escala.jpg')

esc=pygame.image.load("escala.jpg")
ventana.blit(esc,(0,0))
pygame.display.update()
 
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

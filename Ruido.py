#!/usr/bin/python

import pygame
from pygame.locals import *
import os, sys
import Image
import random

pygame.init()
ventana=pygame.display.set_mode((1024,768))
imagen=pygame.image.load("imagen.jpg")
ventana.blit(imagen,(0,0))
pygame.display.update()

#Ruido sal y pimienta
polarizacion = 0 # Que tan Negros/Blancos seran los puntos / Entre mayor sea el numero seran mas negros
intensidad = 1 # % de pixeles
total=((1024*768)/100)*intensidad
im = Image.open("imagen.jpg")
pix = im.load()

for i in range(0,total): 
  x = random.randint(0, 1024-1)
	y = random.randint(0, 768-1) 
	syp=random.randint(0, 255-polarizacion)
	pix[x,y] =(syp,syp,syp) 
		
im.save('salypimienta.jpg')
imagen=pygame.image.load("salypimienta.jpg")
ventana.blit(imagen,(0,0))
pygame.display.update()
  
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()


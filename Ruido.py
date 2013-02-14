#!/usr/bin/python

import pygame
from pygame.locals import *
import os, sys
import Image
import random

pygame.init()
ventana=pygame.display.set_mode((1024,768))
imagen=pygame.image.load("carro.jpg")
ventana.blit(imagen,(0,0))
pygame.display.update()

#Ruido sal y pimienta
polarizacion = 30 # Que tan Negros/Blancos seran los puntos / Entre mayor sea el numero seran mas negros
intensidad = 10 # % de pixeles
total=((1024*768)/100)*intensidad
im = Image.open("carro.jpg")
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
 
#Eliminacion de ruido sal y pimienta
im = Image.open("salypimienta.jpg")
pix = im.load()

for x in range(2,1024-2): #Ancho
	for y in range(2,768-2): #Largo
		r=0
		(r,g,b) = pix[x,y]
		
		if (pix[x,y]==(syp,syp,syp)):
			r+=pix[x+1,y][0]
			r+=pix[x-1,y][0]
			r+=pix[x,y+1][0]
			r+=pix[x,y-1][0]
			var=r/4		
			pix[x,y]=(var,var,var)
		
im.save('eliminacion.jpg')
imagen=pygame.image.load("eliminacion.jpg")
ventana.blit(imagen,(0,0))
pygame.display.update()
 
im = Image.open("eliminacion.jpg")
pix = im.load()
for x in range(0,1024): #Ancho
	for y in range(0,768): #Largo
		(r,g,b) = pix[x,y] 
		promedio=(r+g+b)/3
		pix[x,y] =(promedio,promedio,promedio)
im.save('escala.jpg')

imagen=pygame.image.load("escala.jpg")
ventana.blit(imagen,(0,0))
pygame.display.update() 
 
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()




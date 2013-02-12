#!/usr/bin/python

import pygame
from pygame.locals import *
import os, sys
import Image
import math

pygame.init()
ventana=pygame.display.set_mode((1024,768))
imagen=pygame.image.load("imagen.jpg")
ventana.blit(imagen,(0,0))
pygame.display.update()

#Escala de grises
im = Image.open("imagen.jpg")
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
 
#Mascara
im = Image.open("escala.jpg")
pix = im.load()
dirX = ([-1, 0, 1], [-2, 0, 2], [-1, 0, 1]) 
dirY = ([1, 2, 1], [0, 0, 0], [-1, -2, -1])
for x in range(0,1024-3): #Ancho
	for y in range(0,768-3): #Largo
		sumDirX=0
		sumDirY=0
	
		for i in range(0,3):
			for j in range(0,3):	
				sumDirX +=(pix[x+i,y+j][0]*dirX[i][j])
				sumDirY +=(pix[x+i,y+j][0]*dirY[i][j])
		
		potX = pow(sumDirX, 2) 
		potY = pow(sumDirY, 2) 
		res = int(math.sqrt(potX+potY)) 
		if res > 255: 
			res = 255
		if res < 0:
			res = 0
		pix[x,y] = (res, res, res) 
		
im.save('convolucion.jpg')
imagen=pygame.image.load("convolucion.jpg")
ventana.blit(imagen,(0,0))
pygame.display.update()

#Binarizacion
im = Image.open("convolucion.jpg")
pix = im.load()
for x in range(0,1024-1): #Ancho
	for y in range(0,768-1): #Largo
		(r,g,b) = pix[x,y] 
		promedio=(r+g+b)/3
		if promedio<=127:
			pix[x,y] =(0,0,0)
		else: 
			pix[x,y] =(255,255,255)
		
im.save('binarizada.jpg')
imagen=pygame.image.load("binarizada.jpg")
ventana.blit(imagen,(0,0))
pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()



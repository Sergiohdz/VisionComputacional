#!/usr/bin/python
 
import pygame
from pygame.locals import *
import os, sys
import Image
import math
import random
 
ancho=600
largo=400
 
pygame.init()
ventana=pygame.display.set_mode((ancho,largo))
imagen=pygame.image.load("ab.jpg")
ventana.blit(imagen,(0,0))
pygame.display.update()
 
#Escala de grises
im = Image.open("ab.jpg")
pix = im.load()
for x in range(0,ancho): #Ancho
  for y in range(0,largo): #Largo
  	(r,g,b) = pix[x,y] 
		promedio=(r+g+b)/3
		pix[x,y] =(promedio,promedio,promedio)
im.save('escala.jpg')
 
imagen=pygame.image.load("escala.jpg")
ventana.blit(imagen,(0,0))
pygame.display.update()
 
im = Image.open("escala.jpg")
pix = im.load()
dirX = ([-1, 0, 1], [-2, 0, 2], [-1, 0, 1]) 
dirY = ([1, 2, 1], [0, 0, 0], [-1, -2, -1])
for x in range(0,ancho-3): #Ancho
	for y in range(0,largo-3): #Largo
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
for x in range(0,ancho-1): #Ancho
	for y in range(0,largo-1): #Largo
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
 
 
#BFS
im = Image.open("binarizada.jpg")
pix = im.load()
for x in range(0,ancho-1): #Ancho
	for y in range(0,largo-1): #Largo
		if pix[x,y]==(0,0,0):
			rd=random.randint(0,255)
			gd=random.randint(0,255)
			bd=random.randint(0,255)
			r,g,b=(rd,gd,bd)
			arr=[]
			arr.append(actual) 
			inicio=pix[actual] 
			while len(arr)>0:
				(x,y)=arr.pop(0)
				actual=pix[x,y]
				if actual==inicio or actual ==color:
					if (pix[x-1,y]):
							if (pix[x-1,y]==inicio):
								pix[x-1,y]=color
								arr.append((x-1,y))
					except:
						pass
		
					try:
						if (pix[x+1,y]):                                               
							if (pix[x+1,y]==inicio):
								pix[x+1,y]=color
								arr.append((x+1,y))
					except:
						pass
					try:
						if (pix[x,y-1]):                                          
							if (pix[x,y-1]==inicio):
								pix[x,y-1]=color
								arr.append((x,y-1))
												
					except:
						pass
			
					try:
						if (pix[x,y+1]):                                   
							if (pix[x,y+1]==inicio):
								pix[x,y+1]=color
								arr.append((x,y+1))
					except:
						pass
						
im.save('deteccion.jpg')
imagen=pygame.image.load("deteccion.jpg")
ventana.blit(imagen,(0,0))
pygame.display.update()
actual=0,0
 
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

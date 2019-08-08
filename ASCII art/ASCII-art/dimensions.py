# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 14:30:55 2019

@author: RAHUL
"""
from PIL import Image
import numpy as p
import math

img=Image.open("F:/ASCII art/ascii-pineapple.jpg")
width, height=img.size
width=str(width)
height=str(height) 
print("Image size:"+width+" "+height)
pixel_matrix=p.asarray(img)
print("Pixels are: ")
bright_pix_mat=[[0]*700]*467
i=0
j=0
for i in range(len(pixel_matrix)):
    for j in range(len(pixel_matrix[i])):
        bright_pix_mat[i][j]=math.floor((int(pixel_matrix[i][j][0])+int(pixel_matrix[i][j][1])+int(pixel_matrix[i][j][2]))/3)
        

bright_char=list("`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$")
d={}
k=0

for i in range(len(bright_char)):
    for j in range(3):
        d[k]=bright_char[i]
        k+=1

while (k <= 255) :
    d[k]=bright_char[64]
    k+=1
    
for i in range(len(pixel_matrix)):
    for j in range(len(pixel_matrix[i])):
        for k in range(3):
            print(d[bright_pix_mat[i][j]], end='', file=open("output.txt", "a"))
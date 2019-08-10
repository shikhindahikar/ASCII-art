# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 14:30:55 2019

@author: SHIKHIN
"""
from PIL import Image
import numpy as p
import math

print("Enter file path")    #input path for image
s=str(input())
img=Image.open(s)
width, height=img.size
width=int(width)
height=int(height) 
print("Image size: "+str(width)+"x"+str(height))
pixel_matrix=p.asarray(img)         #made a pixel matrix of image, which is array of width x height with each element a tuple of size 3
bright_pix_mat=[[0 for _ in range(width)] for _ in range(height)]
i=0
j=0
for i in range(len(pixel_matrix)):
    for j in range(len(pixel_matrix[i])):
        bright_pix_mat[i][j]=math.floor((int(pixel_matrix[i][j][0])+int(pixel_matrix[i][j][1])+int(pixel_matrix[i][j][2]))/3)       #made matrix for brightness (integer)values of each pixel
        

bright_char=list("`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$")         #symbols in increasing brightness values
d={}
k=0

for i in range(len(bright_char)):
    for j in range(3):
        d[k]=bright_char[i]             #mapped each symbol with its brightness value
        k+=1

while (k <= 255) :
    d[k]=bright_char[64]
    k+=1
    
for i in range(len(pixel_matrix)):
    for j in range(len(pixel_matrix[i])):
        print(d[bright_pix_mat[i][j]], end='', file=open("output.txt", "a"))            #printed all symbols in output.txt file 
        
    
    print('', file=open("output.txt", "a"))    
print("done")

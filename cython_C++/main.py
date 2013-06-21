'''
Created on 2 oct. 2012

@author: maxime
'''
import sys
sys.path.insert(-1,"E:\CppWorkspace\clipper_m\cython_C++")
from pyclipper import Pyclipper
from pyclipper import *
import random

class PyIntPoint():
    def __init__(self, x,y):
        self.x = x
        self.y = y
 
'''       
clip = Pyclipper()
#clip.test()

square = [[0,0], [1000, 0], [1000, 1000], [0, 1000]]
clip.add_polygon(square)


hole = []
for i in range(3):
    p = [500+int(1000*random.random()), 500+int(1000*random.random())]
    hole.append(p)
    
clip.sub_polygon(hole)

print clip.GetBounds()

sol = clip.execute()
print sol 


f = open("plot_src.dat", "w")
for i, loop in enumerate([square, hole]):
    f.write("")
    for p in loop:
        f.write("%f, %f\n"%(p[0]/1000.0, p[1]/1000.0) )
    p = loop[0]
    f.write("%f, %f\n"%(p[0]/1000.0, p[1]/1000.0) )
    f.write("\n\n")
f.close()   

f = open("plot.dat", "w")
for i, loop in enumerate(sol):
    f.write("")
    for p in loop:
        f.write("%f, %f\n"%(p[0]/1000.0, p[1]/1000.0) )
    f.write("\n\n")
    p = loop[0]
    f.write("%f, %f\n"%(p[0]/1000.0, p[1]/1000.0) )
    f.write("\n\n")
f.close()
'''    
#offsetting

clip = Pyclipper()
shapes = []

shape = []
for i in range(3):
    p = [500+int(1000*random.random()), 500+int(1000*random.random())]
    shape.append(p)
shapes.append(shape)
    
for i in range(3):
    p = [500+int(1000*random.random()), 500+int(1000*random.random())]
    shape.append(p)    
shapes.append(shape)
    
shapes = simplify_polygons(shapes)
sol = offset(shapes, delta=100, jointype=1)


f = open("plot_src.dat", "w")
for i, loop in enumerate([shape]):
    f.write("")
    for p in loop:
        f.write("%f, %f\n"%(p[0]/1000.0, p[1]/1000.0) )
    p = loop[0]
    f.write("%f, %f\n"%(p[0]/1000.0, p[1]/1000.0) )
    f.write("\n\n")
f.close()   

f = open("plot.dat", "w")
for i, loop in enumerate(sol):
    f.write("")
    for p in loop:
        f.write("%f, %f\n"%(p[0]/1000.0, p[1]/1000.0) )
    f.write("\n\n")
    p = loop[0]
    f.write("%f, %f\n"%(p[0]/1000.0, p[1]/1000.0) )
    f.write("\n\n")
f.close()








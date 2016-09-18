'''
Created on Sep 18, 2016

@author: omega
'''

from swampy.TurtleWorld import *
from math import *

def square(t, length):
    for i in range(4):
        fd(t, length)
        lt(t)

def polygon(t, n, length):
    for i in range(n):
        fd(t, length)
        lt(t, 360.0 / n)

def circle(t, r):
    length = 2*pi*r/360
    polygon(t, 360, length)

world = TurtleWorld()
bob = Turtle()
bob.pen_color='black';
print bob
bob.delay=0.01

circle(bob, 100)

wait_for_user()
from swampy.TurtleWorld import *
import math

def square(t, length):
    for i in range(4):
        fd(t, length)
        rt(t)
        
def polyline(t, n, length, angle):
    for i in range(n):
        fd(t, length)
        lt(t, angle)
        
def polygon(t, n, length):
    angle = 360 / n
    polyline(t, n, length, angle)

def circle(t, r):
    cirumference = 2 * math.pi * r
    n = int(cirumference / 3) + 1
    length = cirumference / n
    polygon(t, n, length)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    polyline(t, n, step_length, step_angle)
    


world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01
arc(bob, 50, 180)


wait_for_user()
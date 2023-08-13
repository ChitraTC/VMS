import math
class Point:
    """"
    Represents point in 2-D
    """
def read_point(p):
    p.x=float(input("x coordinate:"))
    p.y=float(input("y coordinate:"))

def print_point(p):
    print("(%g,%g)"%(p.x, p.y))

def distance(p1,p2):
    d=math.sqrt((p1.x-p2.x)**2+(p1.y-p2.y)**2)
    return d

p1=Point()	#create first object
print("Enter First point:")
read_point(p1)	#read x and y for p1

p2=Point()	#create second object
print("Enter Second point:")
read_point(p2)	#read x and y for p2

dist=distance(p1,p2)	#compute distance print("First point is:")
print_point(p1)	#print p1
print("Second point is:")
print_point(p2)			#print p2
print("Distance is: %g" %(dist))	#print d

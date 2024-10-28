## Script Name: ray_ellipsoid_intersection.py

## Usage: python3 ray_ellipsoid_intersection.py d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z

## Parameters:
# d_l_x: x-component of origin-referenced ray direction
# d_l_y: y-component of origin-referenced ray direction
# d_l_z: z-component of origin-referenced ray direction
# c_l_x: x-component offset of ray origin
# c_l_y: y-component offset of ray origin
# c_l_z: z-component offset of ray origin

## Output: Outputs the intersection X, Y, and Z coordinates

## Written by Carl Hayden

## Importing Libraries
import math
import sys # argv

## Defining Functions
def mag(v): # Vector Magnitude
    sum_of_squares = 0.0
    for i in range(0, len(v)):
        sum_of_squares += v[i]**2
    return math.sqrt(sum_of_squares)

def smul(s, v): # Scalar Multipication
    sprod = []
    for i in range(0, len(v)):
        sprod.append(s*v[i])
    return sprod
    # return [s*e for e in v] # Does the same thing in Python

def add(v1, v2): # Vector Addition
    if len(v1) != len(v2):
        return None
    else:
        v3 = []
        for i in range(0, len(v1)):
            v3.append(v1[i] + v2[i])
        return v3

def sub(v1, v2): # Vector Subtraction
    if len(v1) != len(v2):
        return None
    else:
        v3 = []
        for i in range(0, len(v1)):
            v3.append(v1[i] - v2[i])
        return v3

def dot(v1, v2): # Dot Product
    if len(v1) != len(v2):
        return float('nan')
    else:
        dp = 0.0
        for i in range(0, len(v1)):
            dp += v1[i] * v2[i]
        return dp

## Defining Constants
R_Earth = 6378.1363 # Radius of Earth in km
e_Earth = 0.081819221456 # Eccentricity of Earth

## Initialize Script Arguments
d_l_x = float('nan')
d_l_y = float('nan')
d_l_z = float('nan')
c_l_x = float('nan')
c_l_y = float('nan')
c_l_z = float('nan')

## Parse Script Arguments
if len(sys.argv)==7:
    d_l_x = float(sys.argv[1])
    d_l_y = float(sys.argv[2])
    d_l_z = float(sys.argv[3])
    c_l_x = float(sys.argv[4])
    c_l_y = float(sys.argv[5])
    c_l_z = float(sys.argv[6])
else:
    print(\
        'Usage: '\
        'python3 ray_ellipsoid_intersection.py d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z'\
    )
    exit()

## Main Script
d_l = [d_l_x, d_l_y, d_l_z]
c_l = [c_l_x, c_l_y, c_l_z]

a = d_l_x**2 + d_l_y**2 + (d_l_z**2/(1 - e_Earth**2))
b = 2*(d_l_x*c_l_x + d_l_y*c_l_y + (d_l_z*c_l_z)/(1 - e_Earth**2))
c = c_l_z**2 + c_l_y**2 + (c_l_z**2)/(1 - e_Earth**2) - R_Earth**2

disc = b**2 - 4.0*a*c

if disc >= 0.0:
    d = (-b - math.sqrt(disc))/(2*a)
    if d < 0.0:
        d = (-b + math.sqrt(disc))/(2*a)
    if d >= 0.0:
        l_d = add(smul(d, d_l), c_l)
        print(l_d[0])
        print(l_d[1])
        print(l_d[2])
else:
    print('There are no intersections for the provided ray-ellipsoid pair...')
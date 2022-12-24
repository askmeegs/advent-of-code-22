"""
Lava is landing in a pond 
You want to determine a droplet's cooling rate by doing a 3D scan. 

The scan is low-res due to its high speed. 
1x1x1 cubes each represented with x y z position 
"""

import plotly.graph_objects as go
import pandas as pd
import numpy as np
import plotly.express as px

def main():
    with open('small.txt', 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    cubes = []
    for line in lines:
        ix, iy, iz = line.split(',')
        cubes.append((int(ix), int(iy), int(iz)))
    x = [cube[0] for cube in cubes]
    y = [cube[1] for cube in cubes]
    z = [cube[2] for cube in cubes]
    
    # now I have to turn those x, y, z coordinates into cubes 
    # 
    vertices = [] 
    for cube in cubes:
        v = []
        x, y, z = cube[0], cube[1], cube[2]
        # 8 vertices of a cube are 8 sets of triplet coordinates
        v.append((x, y, z))
        v.append((x+1, y, z))
        v.append((x, y+1, z))
        v.append((x+1, y+1, z))
        v.append((x, y, z+1))
        v.append((x+1, y, z+1))
        v.append((x, y+1, z+1))
        v.append((x+1, y+1, z+1))
        vertices.append(v)
        
    # now I have to turn those vertices into faces
    #
    faces = []
    for vertex in vertices:
        f = []
        # 6 faces of a cube are 6 sets of 4 vertices
        f.append((vertex[0], vertex[1], vertex[3], vertex[2]))
        f.append((vertex[0], vertex[1], vertex[5], vertex[4]))
        f.append((vertex[0], vertex[2], vertex[6], vertex[4]))
        f.append((vertex[1], vertex[3], vertex[7], vertex[5]))
        f.append((vertex[2], vertex[3], vertex[7], vertex[6]))
        f.append((vertex[4], vertex[5], vertex[7], vertex[6]))
        faces.append(f)
    
    x = 


# execute main
if __name__ == '__main__':
    main()

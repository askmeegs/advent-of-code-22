"""
Lava is landing in a pond 
You want to determine a droplet's cooling rate by doing a 3D scan. 

The scan is low-res due to its high speed. 
1x1x1 cubes each represented with x y z position 
"""

def main():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    cubes = []
    for line in lines:
        ix, iy, iz = line.split(',')
        cubes.append((int(ix), int(iy), int(iz)))

    # we know that 1 cube is 1 unit of surface area
    # so we can start by declaring a massive cube containing all the cubes
    # then attempt to "carve out" the cubes 
    sa = 6 * len(cubes)

    for c in cubes:
        cX = c[0]
        cY = c[1]
        cZ = c[2]
        # how many are adjacent to this cube in each direction?
        total_adj_x = []
        total_adj_y = []
        total_adj_z = []
        for a in cubes:
            aX = a[0]
            aY = a[1]
            aZ = a[2]
            if abs(aX - cX) == 1 and aY == cY and aZ == cZ:
                total_adj_x.append(a)
            if aX == cX and abs(aY - cY) == 1 and aZ == cZ:
                total_adj_y.append(a)
            if aX == cX and aY == cY and abs(aZ - cZ) == 1:
                total_adj_z.append(a)
        # subtract the number of adjacent cubes from the total surface area
        sa -= len(total_adj_x) + len(total_adj_y) + len(total_adj_z)


    print("🏁 DONE: surface area is {}".format(sa))



# execute main
if __name__ == '__main__':
    main()

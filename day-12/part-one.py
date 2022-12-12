
def main(): 
    with open('small.txt', 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines] 
        # transform into a 2D grid of characters
        grid = [list(line) for line in lines]
        print(grid)

        # find S character in grid
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 'S':
                    grid[i][j] = 1 
                    start = (i, j)
                elif grid[i][j] == 'E':
                    grid[i][j] = 26
                    end = (i, j)
                # convert a-z to 1-26
                else:
                    grid[i][j] = ord(grid[i][j]) - 96
        print(grid)

        """
        Calculate shortest path in grid (# of steps) from S to E. 
        Rules for movement: heights represented a-z 
        You can move up,down, left, or right. 

        You can only move to a square if it's height is <= your current height + 1.
        """
        # calculate shortest path from start to end and return # of steps in shortest path
        steps = shortest_path(start, end, grid)
        print(steps)
    
def shortest_path(start, end, grid):
    # initialize queue with start
    queue = [start]
    # initialize visited set with start
    visited = set(start)
    # initialize steps to 0
    steps = 0
    # while queue is not empty
    while queue:
        # increment steps
        steps += 1
        # initialize new queue
        new_queue = []
        # for each node in queue
        for node in queue:
            # get neighbors of node
            neighbors = get_neighbors(node, grid)
            # for each neighbor
            for neighbor in neighbors:
                # if neighbor is end, return steps
                if neighbor == end:
                    return steps
                # if neighbor is not in visited
                if neighbor not in visited:
                    # add neighbor to visited
                    visited.add(neighbor)
                    # add neighbor to new queue
                    new_queue.append(neighbor)
        # set queue to new queue
        queue = new_queue
    # return -1 if no path found
    return -1


def get_neighbors(current, grid):
    neighbors = []
    # check up
    if current[0] > 0:
        if grid[current[0] - 1][current[1]] <= grid[current[0]][current[1]] + 1:
            neighbors.append((current[0] - 1, current[1]))
    # check down
    if current[0] < len(grid) - 1:
        if grid[current[0] + 1][current[1]] <= grid[current[0]][current[1]] + 1:
            neighbors.append((current[0] + 1, current[1]))
    # check left
    if current[1] > 0:
        if grid[current[0]][current[1] - 1] <= grid[current[0]][current[1]] + 1:
            neighbors.append((current[0], current[1] - 1))
    # check right
    if current[1] < len(grid[0]) - 1:
        if grid[current[0]][current[1] + 1] <= grid[current[0]][current[1]] + 1:
            neighbors.append((current[0], current[1] + 1))
    return neighbors



# execute main
if __name__ == '__main__':
    main()
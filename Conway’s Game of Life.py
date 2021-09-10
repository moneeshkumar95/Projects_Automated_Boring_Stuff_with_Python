import random, time, copy
WIDTH = 30
HEIGHT = 15
# Create a list of list for the cells:
nextCells = []
for x in range(WIDTH):
    column = []  # Create a new column.
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('X')  # Add a living cell.
        else:
            column.append('-')
        nextCells.append(column)
while True:
    print('')  # Separate each step with newlines.
    currentCells = copy.deepcopy(nextCells)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='')
        print()
    for x in range(WIDTH):
        for y in range(HEIGHT):
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1  # Top-left neighbor is alive.
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1  # Top neighbor is alive.
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1  # Top-right neighbor is alive.
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1  # Left neighbor is alive.
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1  # Right neighbor is alive.
            if currentCells[leftCoord][belowCoord] == '#':
                    numNeighbors += 1  # Bottom-left neighbor is alive.
            if currentCells[x][belowCoord] == '#':
                    numNeighbors += 1  # Bottom neighbor is alive.
            if currentCells[rightCoord][belowCoord] == '#':
                    numNeighbors += 1  # Bottom-right neighbor is alive.
            if currentCells[x][y] == '#' and (numNeighbors == 2 or
                                              numNeighbors == 3):
                # Living cells with 2 or 3 neighbors stay alive:
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                # Dead cells with 3 neighbors become alive:
                nextCells[x][y] = '#'
            else:
                # Everything else dies or stays dead:
                nextCells[x][y] = ' '
    time.sleep(1000)




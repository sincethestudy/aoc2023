
data = open('input.txt').read().splitlines()


commands = [(line.split(' ')) for line in data]

visited = set()
current = (0, 0)

brapp = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1)
}

for command in commands:
    dir = command[0]
    mag = int(command[1])
    color = command[2].strip('(').strip(')')

    for i in range(mag):
        current = (current[0] + brapp[dir][0], current[1] + brapp[dir][1])
        if current not in visited:
            visited.add(current)

max_x = max(visited, key=lambda x: x[0])[0]
min_x = min(visited, key=lambda x: x[0])[0]
max_y = max(visited, key=lambda x: x[1])[1]
min_y = min(visited, key=lambda x: x[1])[1]

grid = [['.' for _ in range(min_x, max_x+1)] for _ in range(min_y, max_y+1)]

for x, y in visited:
    grid[y-min_y][x-min_x] = '#'

def flood_fill(matrix, x, y, oldColor, newColor):
    # Stack for cells to be checked
    stack = [(x, y)]

    while stack:
        x, y = stack.pop()

        # Continue if the cell is out of bounds or not the old color
        if (x < 0 or x >= len(matrix) or 
            y < 0 or y >= len(matrix[0]) or 
            matrix[x][y] != oldColor or 
            matrix[x][y] == newColor):
            continue

        # Replace the color at (x, y)
        matrix[x][y] = newColor

        # Add the neighboring cells to the stack
        stack.append((x+1, y))
        stack.append((x-1, y))
        stack.append((x, y+1))
        stack.append((x, y-1))


#find element in matrix that is not a wall
found = False
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '.':
            if (i > 0 and any(grid[i-1][k] == '#' for k in range(i))) and \
               (j > 0 and any(grid[k][j-1] == '#' for k in range(i))) and \
               (i < len(grid)-1 and grid[i+1][j] == '.') and \
               (j < len(grid[i])-1 and grid[i][j+1] == '.'):
                print(i, j)
                flood_fill(grid, i, j, '.', '#')
                found = True
                break
    if found:
        break

# print('\n'.join([''.join(row) for row in grid]))

print(sum([row.count('#') for row in grid]))

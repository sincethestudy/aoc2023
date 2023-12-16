import os 
import time
from tqdm import tqdm
data = open('input.txt').read().split()

print(data)

lb = 0
rb = len(data[0])-1
ub = 0
db = len(data)-1

print(lb, rb, ub, db)

# ((Xdir, Ydir), (Xpos, Ypos))
from collections import deque
beams = deque([])

possible_starts = []

for x in range(lb, rb+1):
    possible_starts.append(((0,1), (x, ub)))
    possible_starts.append(((0,-1), (x, db)))

for y in range(ub, db+1):
    possible_starts.append(((1,0), (lb, y)))
    possible_starts.append(((-1,0), (rb, y)))


counts = []

for start in tqdm(possible_starts):
    visited = set()
    beams = deque([start])
    while beams:
        # time.sleep(0.1)
        beam = beams.popleft()

        xdir_prev, ydir_prev = beam[0]
        xpos_prev, ypos_prev = beam[1]

        if xpos_prev < lb or xpos_prev > rb or ypos_prev < ub or ypos_prev > db:
            # print('out of bounds')
            continue

        if ((xdir_prev, ydir_prev), (xpos_prev, ypos_prev)) in visited:
            # print('visited')
            continue

        visited.add(((xdir_prev, ydir_prev), (xpos_prev, ypos_prev)))

        # data_copy = [list(row) for row in data]
        # for gooba in visited:
        #     data_copy[gooba[1][1]][gooba[1][0]] = '#'
        # data_copy = [''.join(row) for row in data_copy]

        # os.system('cls' if os.name == 'nt' else 'clear')
        # print()
        # print(beam, len(visited))
        # print('\n'.join(data_copy[y] for y in range(ub, db+1)))

        #update dirs
        if data[ypos_prev][xpos_prev] == '/':
            if xdir_prev == 1:
                xdir, ydir = 0, -1
            elif xdir_prev == -1:
                xdir, ydir = 0, 1
            elif ydir_prev == 1:
                xdir, ydir = -1, 0
            elif ydir_prev == -1:
                xdir, ydir = 1, 0

            beams.append(((xdir, ydir), (xpos_prev+xdir, ypos_prev+ydir)))
            continue

        elif data[ypos_prev][xpos_prev] == '\\':
            if xdir_prev == 1:
                xdir, ydir = 0, 1
            elif xdir_prev == -1:
                xdir, ydir = 0, -1
            elif ydir_prev == 1:
                xdir, ydir = 1, 0
            elif ydir_prev == -1:
                xdir, ydir = -1, 0
                
            beams.append(((xdir, ydir), (xpos_prev+xdir, ypos_prev+ydir)))
            continue

        elif data[ypos_prev][xpos_prev] == '-':
            if abs(xdir_prev) == 1:
                beams.append(((xdir_prev, ydir_prev), (xpos_prev+xdir_prev, ypos_prev+ydir_prev)))
                continue

            else:
                beams.append(((1,0), (xpos_prev+1, ypos_prev)))
                beams.append(((-1,0), (xpos_prev-1, ypos_prev)))
                continue

        elif data[ypos_prev][xpos_prev] == '|':
            if abs(ydir_prev) == 1:
                beams.append(((xdir_prev, ydir_prev), (xpos_prev+xdir_prev, ypos_prev+ydir_prev)))
                continue

            else:
                beams.append(((0,1), (xpos_prev, ypos_prev+1)))
                beams.append(((0,-1), (xpos_prev, ypos_prev-1)))
                continue

        elif data[ypos_prev][xpos_prev] == '.':
            beams.append(((xdir_prev, ydir_prev), (xpos_prev+xdir_prev, ypos_prev+ydir_prev)))
            continue


    xx = set([x[1] for x in visited])
    counts.append(len(xx))
print(max(counts))
with open('input.txt', 'r') as file:
    data = [list(line.strip()) for line in file.readlines()]

to_add = []
for i in range(len(data)):
    if all(cell == '.' for cell in data[i]):
        to_add.append(i)

i_add = 0
for i in to_add:
    data.insert(i+i_add, ['.']*len(data[i]))
    i_add += 1

to_add = []
for i in range(len(data[0])):
    if all(row[i] == '.' for row in data):
        to_add.append(i)


i_add = 0
for i in to_add:
    for row in data:
        row.insert(i+i_add, '.')

    i_add += 1


counter = 1
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == '#':
            data[i][j] = str(counter)
            counter += 1

import itertools
import numpy as np

def find_coordinates(data, target):
    for i, row in enumerate(data):
        for j, cell in enumerate(row):
            if cell == target:
                return (i, j)

def manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def shortest_path(data, start, end):
    start_coordinates = find_coordinates(data, start)
    end_coordinates = find_coordinates(data, end)
    return manhattan_distance(start_coordinates, end_coordinates)

numbers = [str(i) for i in range(1, counter)]
pairs = list(itertools.combinations(numbers, 2))
sum_of_paths = 0

print(len(pairs))

for pair in pairs:
    start, end = pair
    path = shortest_path(data, start, end)
    sum_of_paths += path

print(sum_of_paths)
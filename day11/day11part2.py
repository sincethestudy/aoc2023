with open('input.txt', 'r') as file:
    data = [list(line.strip()) for line in file.readlines()]

empty_rows = []
empty_cols = []

for i in range(len(data)):
    if all(cell == '.' for cell in data[i]):
        empty_rows.append(i)

for i in range(len(data[0])):
    if all(row[i] == '.' for row in data):
        empty_cols.append(i)

print(empty_rows)
print(empty_cols)

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
    expansion_factor = 1000000
    row_empty_count = sum(x in range(min(point1[0], point2[0]), max(point1[0], point2[0])) for x in empty_rows)
    col_empty_count = sum(y in range(min(point1[1], point2[1]), max(point1[1], point2[1])) for y in empty_cols)

    x_distance = abs(point1[0] - point2[0]) + row_empty_count*(expansion_factor-1)
    y_distance = abs(point1[1] - point2[1]) + col_empty_count*(expansion_factor-1)

    return x_distance + y_distance

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
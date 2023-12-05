import collections

with open('input.txt', 'r') as file:
    schematic = file.readlines()

schematic = [row.strip() for row in schematic]


def is_symbol(char):
    return not char.isdigit() and char != '.'

def find_full_number(x,y):
    full_number = ''
    i = x
    furthest_right = x
    furthest_left = x
    while i >= 0 and schematic[y][i].isdigit():
        furthest_left = i
        full_number = schematic[y][i] + full_number
        i -= 1
    i = x + 1
    while i < len(schematic[y]) and schematic[y][i].isdigit():
        furthest_right = i
        full_number += schematic[y][i]
        i += 1
    return full_number, furthest_left, furthest_right
    
def check_adjacent(x,y):
    adjacent_cells = [(x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y), (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1)]
    for cell in adjacent_cells:
        cell_x, cell_y = cell
        if cell_x >= 0 and cell_y >= 0 and cell_y < len(schematic) and cell_x < len(schematic[cell_y]):
            if is_symbol(schematic[cell_y][cell_x]):
                return (schematic[cell_y][cell_x], cell_x, cell_y)
    return False

def find_numbers():
    numbers = []
    for y, row in enumerate(schematic):
        skip_to = -1
        for x, char in enumerate(row):
            if x <= skip_to:
                continue
            else:
                skip_to = -1
                if char.isdigit():
                    num, start, end = find_full_number(x,y)
                    skip_to = end
                    numbers.append((int(num), start, end, y))
            
    return numbers

numbas = find_numbers()
# print(numbas)

def check_full_number(xRange, y):
    for x in range(xRange[0], xRange[1]+1):
        adjacent = check_adjacent(x,y)
        if adjacent:
            if adjacent[0] == '*':
                print('adjacent to', adjacent[0], 'at', adjacent[1], adjacent[2], 'from', x, y)
                return ('*', adjacent[1], adjacent[2])
            return (True)
    return False

def check_numbers():
    list_numbers = []
    gear_numbers = []
    for num in numbas:
        checked = check_full_number((num[1], num[2]), num[3])
        if checked:
            if type(checked)==tuple and checked[0] == '*':
                gear_numbers.append((num, checked[1], checked[2]))
            else:
                list_numbers.append(num)
    return list_numbers, gear_numbers

def gear_mults():
    _, gear_numbers = check_numbers()
    print(gear_numbers)
    cal = 0
    for i in gear_numbers:
        for j in gear_numbers:
            if i != j:
                if i[1] == j[1] and i[2] == j[2]:
                    print(i[1], j[1], i[2], j[2], i[0][0], j[0][0])
                    cal += i[0][0] * j[0][0]

    return cal/2

def sum_numbers():
    return sum(num[0] for num in check_numbers())

def duplicates():
    return [item for item, count in collections.Counter([num[0] for num in numbas]).items() if count > 1]

print(gear_mults())
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
        # print(cell_x, cell_y)
        if cell_x >= 0 and cell_y >= 0 and cell_y < len(schematic) and cell_x < len(schematic[cell_y]):
            if is_symbol(schematic[cell_y][cell_x]):
                print('adjacent to', schematic[cell_y][cell_x], 'at', cell_x, cell_y, 'from', x, y)
                return True
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
        if check_adjacent(x,y):
            return True
    return False

def check_numbers():
    list_numbers = []
    for num in numbas:
        if check_full_number((num[1], num[2]), num[3]):
            list_numbers.append(num)
        else:
            print('rejected', num)
    return list_numbers

def mark_checked_numbers():
    schematic_copy = [list(row) for row in schematic]
    checked_numbers = check_numbers()
    all_numbers = find_numbers()
    rejected_numbers = [num for num in all_numbers if num not in checked_numbers]
    for num in checked_numbers:
        for x in range(num[1], num[2]+1):
            schematic_copy[num[3]][x] = 'X'
    for num in rejected_numbers:
        for x in range(num[1], num[2]+1):
            schematic_copy[num[3]][x] = 'R'
    with open('debug.txt', 'w') as f:
        for row in schematic_copy:
            f.write(''.join(row))

# mark_checked_numbers()


def sum_numbers():
    return sum(num[0] for num in check_numbers())

def duplicates():
    return [item for item, count in collections.Counter([num[0] for num in numbas]).items() if count > 1]

print(sum_numbers())
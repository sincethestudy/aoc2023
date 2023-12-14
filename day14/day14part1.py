data = open('input.txt', 'r').read().splitlines()

data_r = [list(i) for i in zip(*data[::-1])]


new_data = []
for row in data_r:

    frees = []
    blocks = [-1]
    rocks = []
    for i, char in enumerate(row):
        if char == '.':
            frees.append(i)

        elif char == '#':
            blocks.append(i)

        elif char == 'O':
            rocks.append(i)

    blocks.append(len(row))

    new_row = row.copy()
    for j,blocker in enumerate(blocks[:-1]):
        free = [i for i in frees if i > blocker and i < blocks[j+1]]
        rock = [i for i in rocks if i > blocker]

        while free and rock:
            if free[-1] > rock[0]:
                new_row[free[-1]] = 'O'
                new_row[rock[0]] = '.'
                rock.pop(0)

            free.pop(-1)

    new_data.append(new_row)
    print(new_row)

count = 0
for i, row in enumerate(new_data):
    for j, char in enumerate(row):
        if char == 'O':
            count += 1*j + 1

print(count)


    
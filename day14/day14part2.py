from tqdm import tqdm
data_rr = open('input.txt', 'r').read().splitlines()



c = 4000000000
pattern = []
prev_data = data_rr.copy()
pfound = 0
pfoundat = 0
for i in range(c):
    data_r = [list(j) for j in zip(*prev_data[::-1])].copy()

    new_data = []
    for row in data_r:

        frees = []
        blocks = [-1]
        rocks = []
        for j, char in enumerate(row):
            if char == '.':
                frees.append(j)

            elif char == '#':
                blocks.append(j)

            elif char == 'O':
                rocks.append(j)

        blocks.append(len(row))

        new_row = row.copy()
        for j,blocker in enumerate(blocks[:-1]):
            free = [g for g in frees if g > blocker and g < blocks[j+1]]
            rock = [g for g in rocks if g > blocker]

            while free and rock:
                if free[-1] > rock[0]:
                    new_row[free[-1]] = 'O'
                    new_row[rock[0]] = '.'
                    rock.pop(0)

                free.pop(-1)

        new_data.append(new_row)

    prev_data = new_data.copy()
    count = 0

    if i%4 == 3 and i > 0:
        for h, row in enumerate([list(j) for j in zip(*prev_data[::-1])]):
            for j, char in enumerate(row):
                if char == 'O':
                    count += 1*j + 1
                    

        # print()
        # print('\n'.join([''.join(row) for row in prev_data]))

        stu = ''
        for row in prev_data:
            stu += ''.join(row)

        print(count)

        if stu in pattern:
            print("Pattern found at {} cycle of {}".format(pattern.index(stu), int((i+1)/4 - pattern.index(stu))))

            offset = int(pattern.index(stu)+1)
            cycle = int((i+1)/4 - pattern.index(stu)-1)
            break

        pattern.append(stu)
            


    if pfound:
        break

moves = (int(c/4)-offset)%cycle
print(offset, cycle, moves)

for i in range(moves*4):
    data_r = [list(j) for j in zip(*prev_data[::-1])]

    new_data = []
    for row in data_r:

        frees = []
        blocks = [-1]
        rocks = []
        for j, char in enumerate(row):
            if char == '.':
                frees.append(j)

            elif char == '#':
                blocks.append(j)

            elif char == 'O':
                rocks.append(j)

        blocks.append(len(row))

        new_row = row.copy()
        for j,blocker in enumerate(blocks[:-1]):
            free = [g for g in frees if g > blocker and g < blocks[j+1]]
            rock = [g for g in rocks if g > blocker]

            while free and rock:
                if free[-1] > rock[0]:
                    new_row[free[-1]] = 'O'
                    new_row[rock[0]] = '.'
                    rock.pop(0)

                free.pop(-1)

        new_data.append(new_row)
        # print(new_row)

    prev_data = new_data.copy()
    count = 0

    if i%4 == 3 and i > 0:
        for h, row in enumerate([list(j) for j in zip(*prev_data[::-1])]):
            for j, char in enumerate(row):
                if char == 'O':
                    count += 1*j + 1

print(count)
    







    
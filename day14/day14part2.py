from tqdm import tqdm
data_rr = open('input.txt', 'r').read().splitlines()

c = 4000000000
pattern = []
prev_data = data_rr.copy()
offset = 0
for i in range(c):
    data_r = [''.join(list(j)) for j in zip(*prev_data[::-1])]

    new_data = []
    for row in data_r:
        r = '#'.join([''.join(sorted(x)) for x in row.split('#')])
        new_data.append(r)

    prev_data = new_data.copy()

    if i%4 == 3 and i > 0:
        count = sum(j+1 for i, row in enumerate([list(j) for j in zip(*prev_data[::-1])]) for j, char in enumerate(row) if char == 'O')
        stu = ''.join(y for x in prev_data for y in x )

        if stu in pattern:
            offset = int(pattern.index(stu)+1)
            cycle = int((i+1)/4 - pattern.index(stu)-1)
            break

        pattern.append(stu)

    if offset:
        break

moves = (int(c/4)-offset)%cycle

for i in range(moves*4):
    data_r = [''.join(list(j)) for j in zip(*prev_data[::-1])]

    new_data = []
    for row in data_r:
        r = '#'.join([''.join(sorted(x)) for x in row.split('#')])
        new_data.append(r)

    prev_data = new_data.copy()

    if i%4 == 3 and i > 0:
        count = sum(j+1 for i, row in enumerate([list(j) for j in zip(*prev_data[::-1])]) for j, char in enumerate(row) if char == 'O')


print(count)
    







    
data = open('test.txt', 'r').read().splitlines()

#rotate
data_r = [''.join(list(i)) for i in zip(*data[::-1])]

new_data = []
for row in data_r:
    r = '#'.join([''.join(sorted(x)) for x in row.split('#')])
    new_data.append(r)

count = sum(j+1 for i, row in enumerate(new_data) for j, char in enumerate(row) if char == 'O')

print(count)


    
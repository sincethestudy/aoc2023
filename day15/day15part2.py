data = open("input.txt").read().split(',')

boxes = [list() for _ in range(256)]


for item in data:
    val = 0
    if '=' in item:
        it = item.split('=')

        for c in it[0]:
            ascii_c = ord(c)
            val += ascii_c
            val *= 17
            val %= 256

        idx = [x[0] for x in boxes[val]]

        if it[0] in idx:
            ind = idx.index(it[0])
            boxes[val][ind] = (it[0],it[1])
            continue

        boxes[val].append((it[0], it[1]))

    else:
        it = item.split('-')

        for c in it[0]:
            ascii_c = ord(c)
            val += ascii_c
            val *= 17
            val %= 256


        idx = [x[0] for x in boxes[val]]

        if it[0] in idx:
            ind = idx.index(it[0])
            del boxes[val][ind]

power = 0

for i,box in enumerate(boxes):
    temp=0
    if box:
        for j, lens in enumerate(box):
            temp = int(lens[1]) * (j+1) * (i+1)
            print(temp)
            power += temp

print(power)

# vals = []
# for item in data:
#     val = 0
#     for i, c in enumerate(item):
#         ascii_c = ord(c)

#         val += ascii_c
#         val *= 17
#         val %= 256

#     vals.append(val)

# print(sum(vals))



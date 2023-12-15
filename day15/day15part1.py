

data = open("input.txt").read().split(',')

print(data)

vals = []
for item in data:
    val = 0
    for i, c in enumerate(item):
        ascii_c = ord(c)

        val += ascii_c
        val *= 17
        val %= 256

    vals.append(val)

print(sum(vals))



with open('input.txt', 'r') as file:
    schematic = file.readlines()

schematic = [row.strip() for row in schematic]

total = 0
for card in schematic:
    print(card)
    splot = card.split(': ')[1]
    winners = splot.split(' | ')[0]
    mine = splot.split(' | ')[1]
    win_arr = winners.split(' ')
    mine_arr = mine.split(' ')

    cur = 0
    multiplier = 0
    for i in win_arr:
        for j in mine_arr:
            if i == j and i.isdigit() and j.isdigit():
                # print('match')
                # print(i)
                # print(j)
                # print('match')
                print(i, j)
                if multiplier == 0:
                    multiplier = 1
                else:
                    multiplier *= 2

    print(multiplier)

    total += multiplier

print(total)
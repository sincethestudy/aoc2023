with open('input.txt', 'r') as file:
    schematic = file.readlines()

schematic = [row.strip() for row in schematic]

total = 0

schematic_lines_count = [1]*len(schematic)
print(schematic_lines_count)

#split each card beforehand
split_cards = []
for card in schematic:
    splot = card.split(': ')[1]
    winners = splot.split(' | ')[0]
    mine = splot.split(' | ')[1]
    win_arr = winners.split(' ')
    mine_arr = mine.split(' ')

    set_win = set(win_arr)
    set_mine = set(mine_arr)
    # print(set_win, set_mine)
    set_win = {i for i in set_win if i.isdigit()}
    set_mine = {i for i in set_mine if i.isdigit()}
    matching_items = len(set_win.intersection(set_mine))
    split_cards.append(matching_items)

for idx, card in enumerate(schematic):
    for p in range(0, schematic_lines_count[idx]):
        print(f"Card {idx} {schematic_lines_count[idx]}")
        split_card = split_cards[idx]
        cur_winning = 1
        for i in range(0, split_card):
            schematic_lines_count[idx+cur_winning] += 1
            cur_winning += 1

total = sum(schematic_lines_count)
print(total)
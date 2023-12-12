
data = open('input.txt').read().splitlines()
hands, bids = zip(*[line.split() for line in data])

rank = 'AKQT98765432J'

def tuplize(hand):
    h = []
    for c in rank:
        h.append(tuple(sorted([hand.replace('J', c).count(x) for x in set(hand.replace('J', c))], reverse=True)))

    return list(sorted(h, reverse=True))[0]

def sort_me(hand):
    return (tuplize(hand), [-rank.index(x) for x in hand])

tony = sorted(hands, key=sort_me, reverse=True)

print(sum([int(bids[hands.index(x)])*(i+1) for i, x in enumerate(reversed(tony))]))
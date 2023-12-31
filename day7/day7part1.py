
data = open('input.txt').read().splitlines()
hands, bids = zip(*[line.split() for line in data])

rank = 'AKQJT98765432'

def tuplize(hand):
    return tuple(sorted([hand.count(x) for x in set(hand)], reverse=True))

def sort_me(hand):
    return (tuplize(hand), [-rank.index(x) for x in hand])

tony = sorted(hands, key=sort_me, reverse=True)

print(sum([int(bids[hands.index(x)])*(i+1) for i, x in enumerate(reversed(tony))]))
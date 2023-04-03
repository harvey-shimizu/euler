from collections import Counter

hands = (line.split() for line in open('p054_poker.txt'))
print(hands)
values = {r:i for i,r in enumerate('23456789TJQKA', 2)}
print(values)
straights = [(v, v-1, v-2, v-3, v-4) for v in range(14, 5, -1)] + [(14, 5, 4, 3, 2)]
print(straights)
ranks = [(1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(),(),(3,2),(4,1)]

def hand_rank(hand):
    score, score1 = zip(*sorted(((v, values[k]) for k,v in Counter(x[0] for x in hand).items()), reverse=True))
    score = ranks.index(score)
    if len(set(card[1] for card in hand)) == 1: score = 5  # flush
    if score1 in straights: score = 8 if score == 5 else 4  # str./str. flush
    return score

#print("P1 wins", sum(hand_rank(hand[:5]) > hand_rank(hand[5:]) for hand in hands))

hh = ['2H', '2D', '2C', '2S', '4S']
s1, s2 = zip(*sorted(((v, values[k]) for k,v in Counter(x[0] for x in hh).items()), reverse=True))
print(s1, s2)

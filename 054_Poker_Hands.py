'''

In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand	 	Player 1	 	Player 2	 	Winner
1	 	5H 5C 6S 7S KD
Pair of Fives
 	2C 3S 8S 8D TD
Pair of Eights
 	Player 2
2	 	5D 8C 9S JS AC
Highest card Ace
 	2C 5C 7D 8S QH
Highest card Queen
 	Player 1
3	 	2D 9C AS AH AC
Three Aces
 	3D 6D 7D TD QD
Flush with Diamonds
 	Player 2
4	 	4D 6S 9H QH QC
Pair of Queens
Highest card Nine
 	3D 6D 7H QD QS
Pair of Queens
Highest card Seven
 	Player 1
5	 	2H 2D 4C 4D 4S
Full House
With Three Fours
 	3C 3D 3S 9S 9D
Full House
with Three Threes
 	Player 1
The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?

'''

import csv
import re

pattern = '(\w\w) (\w\w) (\w\w) (\w\w) (\w\w) (\w\w) (\w\w) (\w\w) (\w\w) (\w\w)'
suits = {'C':1, 'D':2, 'H':3, 'S':4}
cards = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
roles = {'HC':1, '1P':2, '2P':3, '3C':4, 'ST':5, 'FL':6, 'FH':7, '4C':8, 'SF':9, 'RF':10}

hands=[]
with open('p054_poker.txt', 'r') as f:
    #for h in csv.reader(f, delimiter='\n'):
    for h in csv.reader(f, delimiter=' '):
        hands.append([c for c in h])

l = 5
n = 0
h0 = hands[:1][0][0]
hh = hands[:1][0][:5]

hh = ['5H', '5C', '6S', '7S', 'KD']
hh = ['2C', '5C', '7D', '8S', 'QH']
hh = ['2D', '9C', 'AS', 'AH', 'AC']
hh = ['4D', '6S', '9H', 'QH', 'QC']
hh = ['5D', '8C', '9S', 'JS', 'AC']
hh = ['3D', '6D', '7H', 'QD', 'QS']
hh = ['3D', '6D', '7D', 'TD', 'QD']
hh = ['9H', '3D', '3H', '3C', '9S']
hh = ['2H', '2D', '4D', '4C', '4S']
hh = ['2H', '2D', '2C', '2S', '4S']

nCount = 0
matchNum = []
mCount = 0
matchMark = []
highestNum = 0
for n in range(0,5):
    h = hh[n]
    for i in hh[n+1:5]:
        if h[0] == i[0]:
            nCount += 1
            matchNum.append(h[0])
        elif h[1] == i[1]:
            mCount += 1
            matchMark.append(h[0])
        elif cards[i[0]] > highestNum:
            highestNum = cards[i[0]]
        else:
            pass
#print(matchNum, nCount, matchMark, mCount, highestNum)

def handScoring(s, h):
    if s == 0: ofset = 0
    else: ofset = 5

    r = re.compile(pattern).match(h)
    c1 = r.group(1+ofset)
    c2 = r.group(2+ofset)
    c3 = r.group(3+ofset)
    c4 = r.group(4+ofset)
    c5 = r.group(5+ofset)

#handScoring(0, hands[:1][0][0])

'''
Analysis:

If we can quantify each hand into an array of tuples we can quickly compare each hand and determine a winner or a tie.
The first tuple would consist between 2 and 5 elements representing the frequency of card values sorted in descending order. The second tuple would consist of the same number of elements as the first but describe the value sorted and weighted by frequency in descending order.

Let’s check out how this would look for a few typical hands for both players:
    p1 = TH 6H 9H QH JH [(1, 1, 1, 1, 1), (12, 11, 10, 9, 6)], score = 0
    p2 = 9H 4D JC KS JS [(2, 1, 1, 1), (11, 13, 9, 4)], score = 1

    p1 = 7C 7S KC KS JC [(2, 2, 1), (13, 7, 11)], score = 2
    p2 = 7H 7D KH KD 9S [(2, 2, 1), (13, 7, 9)], score = 2

    Ties in similar scores are broken by checking the second tuple

    By simply comparing hands as p1>p2 we can determine the winner between the two players. The only complication left is to calculate and rank straights and flushes.

'''

from collections import Counter
hands = (line.split() for line in open('p054_poker.txt'))

values = {r:i for i,r in enumerate('23456789TJQKA', 2)}
straights = [(v, v-1, v-2, v-3, v-4) for v in range(14, 5, -1)] + [(14, 5, 4, 3, 2)]
ranks = [(1,1,1,1,1),(2,1,1,1),(2,2,1),(3,1,1),(),(),(3,2),(4,1)]

def hand_rank(hand):
    score = zip(*sorted(((v, values[k]) for k,v in Counter(x[0] for x in hand).items()), reverse=True))
    score[0] = ranks.index(score[0])
    if len(set(card[1] for card in hand)) == 1: score[0] = 5  # flush
    if score[1] in straights: score[0] = 8 if score[0] == 5 else 4  # str./str. flush
    return score

print("P1 wins", sum(hand_rank(hand[:5]) > hand_rank(hand[5:]) for hand in hands))

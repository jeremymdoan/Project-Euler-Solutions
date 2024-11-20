# https://projecteuler.net/problem=54
# I haven't completed this one yet

from collections import Counter

face_cards = {'A':14, 'K':13, 'Q':12, 'J':11, 'T':10}
suits = ['C','H','D','S']
hand_ranks = {
    "royalFlush": 2000,
    "straightFlush": 800,
    "fourKind": 700,
    "fullHouse": 600,
    "flush": 500,
    "straight": 400,
    "threeKind": 300,
    "twoPair": 200,
    "pair": 100,
    "highCard": 0
}

def convert_face_cards(a):
    return int(a) if a.isnumeric() else face_cards[a]

def highCards(hand):
    hand_count = Counter(hand[0])
    value = None
    if len(hand_count) == 5:
        value = (max(hand[0]),'highCard')
    return value

def isPair(hand):
    hand_count = Counter(hand[0])
    value = None
    if len(hand_count) == 4:
        for i in hand_count:
            if hand_count[i] == 2:
                value = (i,'pair')
    return value

def isTwoPair(hand):
    hand_count = Counter(hand[0])
    value = None
    pairs = []
    for i in hand_count:
        if hand_count[i]==2:
            pairs.append(i)
    if len(pairs) == 2:
        value = (max(pairs), 'twoPair')
    return value

def isThreeKind(hand):
    hand_count = Counter(hand[0])
    value = None
    for i in hand_count:
        if hand_count[i]==3:
            value = (i,'threeKind')
    return value 

def isStraight(hand):
    value = (max(hand[0]),'straight')
    for i in range(4):
        if not hand[0][i+1]-hand[0][i] == 1:
            value = None
    return value

def isFlush(hand):
    value = None
    if len(Counter(hand[1]))==1:
        value = (max(hand[0]), 'flush')
    return value

def isFullHouse(hand):
    hand_count = Counter(hand[0])
    value = None
    if len(hand_count) == 2:
        value =  (sum(hand[0]),'fullHouse')
    return value

def isFourKind(hand):
    hand_count = Counter(hand[0])
    value = None
    for i in hand_count:
        if hand_count[i]==4:
            value = (i,'fourKind')
    return value 

def isStraightFlush(hand):
    value = None
    if isStraight(hand) and isFlush(hand):
        value =  (max(hand[0]),'straightFlush')
    return value

def isRoyalFlush(hand):
    value = None
    if isStraightFlush(hand) and highCards(hand)==14:
        value = (2000,'royalFlush')
    return value

hand_functions = [isRoyalFlush, isStraightFlush, isFourKind, isFullHouse, isFlush, isStraight, isThreeKind, isTwoPair, isPair, highCards]

def handValue(hand):
    hand_separated = separateHand(hand)
    for func in hand_functions:
        hand_value = func(hand_separated)
        if hand_value:
            return hand_value


def separateHand(hand):
    return [sorted([convert_face_cards(a[0]) for a in hand]), [a[1] for a in hand]]

def main():
    with open('C:\\Users\\jeremy.doan\\OneDrive - S&P Global\\Code\\Project Euler\\p054_poker.txt', 'r') as rounds:
        hand1_wins =  0
        for round in rounds:
            hands = round.replace('\n', '').split(' ')
            hand1, hand2 = sorted(hands[:5]), sorted(hands[5:])        
            hand1_value, hand2_value = handValue(hand1), handValue(hand2)
            if hand_ranks[hand1_value[1]] > hand_ranks[hand2_value[1]]:
                hand1_wins += 1
            elif (hand_ranks[hand1_value[1]] == hand_ranks[hand2_value[1]]):
                if (hand1_value[0]> hand2_value[0]):
                    hand1_wins += 1
                elif hand1_value[0] == hand2_value[0]:
                    h1, h2 = sorted(separateHand(hand1)[0]), sorted(separateHand(hand2)[0])
                    while True:
                        high1, high2 = max(h1), max(h2)            
                        if high1 > high2:
                            hand1_wins += 1
                            break
                        elif high1 < high2:
                            break
                        else:
                            h1.pop(h1.index(high1))
                            h2.pop(h2.index(high2))
        print(hand1_wins)


if __name__ == "__main__":
    main()
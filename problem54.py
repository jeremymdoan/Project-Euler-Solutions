# https://projecteuler.net/problem=54
# I haven't completed this one yet

from collections import Counter

face_cards = {'A':14, 'K':13, 'Q':12, 'J':11, 'T':10}

def convert_face_cards(a):
    return int(a) if a.isnumeric() else face_cards[a]

def highCards(hand):
    hand_count = Counter(hand[0])
    values = []
    for i in hand_count:
        if hand_count[i]==1:
            values.append(i)
    return values

def isPair(hand):
    hand_count = Counter(hand[0])
    for i in hand_count:
        if hand_count[i]==2:
            return [i]
    return []

def isTwoPair(hand):
    hand_count = Counter(hand[0])
    pairs = []
    for i in hand_count:
        if hand_count[i]==2:
            pairs.append(i)
    return pairs

def isThreeKind(hand):
    hand_count = Counter(hand[0])
    for i in hand_count:
        if hand_count[i]==3:
            return [i]
    return []

def isStraight(hand):
    for i in range(4):
        if not hand[0][i+1]-hand[0][i] == 1:
            return []
    return hand[0]

def isFlush(hand):
    if len(Counter(hand[1]))==1:
        return hand[0]
    return []

def isFullHouse(hand):
    hand_count = Counter(hand[0])
    if len(hand_count) == 2:
        return [isThreeKind(hand_count), isPair(hand_count)]
    return []

def isFourKind(hand):
    hand_count = Counter(hand[0])
    for i in hand_count:
        if hand_count[i]==4:
            return [i]
    return []

def isStraightFlush(hand):
    if isStraight(hand) and isFlush(hand):
        return hand[0]
    return []

def isRoyalFlush(hand):
    if isStraightFlush(hand) and highCards(hand)[0]==14:
        return hand[0]
    return []

hand_functions = [isRoyalFlush, isStraightFlush, isFourKind, isFullHouse, isFlush, isStraight, isThreeKind, isTwoPair, isPair, highCards]

def handValue(hand):
    hand_separated = separateHand(hand)
    for func in hand_functions:
        hand_value = func(hand_separated)
        if hand_value:
            return hand_value


def separateHand(hand):
    return [[convert_face_cards(a[0]) for a in hand], [a[1] for a in hand]]

def compareHands(hand1, hand2):
    return True

with open('p054_poker.txt', 'r') as rounds:
    hand1_wins, hand2_wins = 0, 0
    for round in rounds:
        hands = round.replace('\n', '').split(' ')
        hand1, hand2 = sorted(hands[:5]), sorted(hands[5:])
        hand1_values, hand2_values = handValue(hand1), handValue(hand2)
        """
        if hand1_values[0] > hand2_values[0]:
            hand1_wins += 1
        elif hand1_values[0] < hand2_values[0]:
            hand2_wins += 1
        elif hand1_values[0] == hand2_values[0]:
        """
        print(handValue(hand1), handValue(hand2))
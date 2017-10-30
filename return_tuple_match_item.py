hand = [(2, "Club"), (4, "Heart"), (2, "Diamond"), (2, "Club"), (8, "Spades")]

def match_tuple_list(ls):
    matched = []
    for card in hand:
        if hand.count(card) > 1:
            matched.append(card)
    return (list(set(matched)))



print (match_tuple_list(hand))
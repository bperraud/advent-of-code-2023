with open('input.txt', encoding = 'utf-8') as f:
    data = [x.strip('\n') for x in f.readlines()]

card_rank = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

def compare_hand(hand1 : str, hand2 : str) -> bool :
    hand1_count = [hand1.count(card) for card in card_rank if card != "J"]
    hand2_count = [hand2.count(card) for card in card_rank if card != "J"]
    hand1_count[hand1_count.index(max(hand1_count))] += hand1.count("J")
    hand2_count[hand2_count.index(max(hand2_count))] += hand2.count("J")

    while ((max(hand1_count) ) == (max(hand2_count) ) and ((max(hand1_count) ) > 1) ) :
        hand1_count.remove(max(hand1_count))
        hand2_count.remove(max(hand2_count))
    if (max(hand1_count) > max(hand2_count)) :
        return True
    elif (max(hand1_count) < max(hand2_count)) :
        return False
    for card1, card2 in zip(hand1, hand2):
        if card1 != card2 :
            return card_rank.index(card1) < card_rank.index(card2)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if compare_hand(arr[j][0], arr[j + 1][0]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

hands = []
for line in data :
    hands.append(line.split())

bubble_sort(hands)
print(sum( int(elem[1]) * (i + 1) for i, elem in enumerate(hands)))

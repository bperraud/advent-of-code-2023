import sys

data = sys.stdin.read().splitlines()
winning_card = []
for line in data :
	list1, list2 = ((part.split()) for part in line.split(":")[1].split("|"))
	winning_card.append(sum(elem in list2 for elem in list1))

for card in range (len(winning_card) - 1, -1, -1) :
	winning_card[card] = sum(winning_card[i] for i in range(card, card + winning_card[card] + 1) if i < len(winning_card))

print(sum(winning_card) + len(winning_card))

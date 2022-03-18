import random

with open('cards.txt', 'r') as game:
    cards = game.readlines()
print(cards)

if len(cards) < 10:
  raise Exception("Sorry, there are not enough cards to play!")
else:
    print("The game can begin!")

random_cards = random.sample(cards, k=len(cards))
print(random_cards)

print(f"The randomly selected card is {random.choice(random_cards)}")

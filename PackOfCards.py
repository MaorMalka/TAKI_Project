import random

CARDSCOLOR = ["Red", "Green", "Blue", "Yellow"]
CARDS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "plus two", "plus",
         "Change direction", "stop", "change color", "crazy card", "taki", "colorfulTaki"]
POPCARDS = list()

class PackOfCards:

    def __init__(self):
        self.cards = list()
        for color in CARDSCOLOR:
            for card in CARDS:
                self.cards.append((color, card))
        random.shuffle(self.cards)

    def pick_a_card(self):
        card = self.cards.pop()
        POPCARDS.append(card)
        return card

    def divideCards(self):
        if len(self.cards) < 8:
            self.cards += POPCARDS
            random.shuffle(self.cards)
        myCards = list()
        for _ in range(8):
            myCards.append(self.pick_a_card())



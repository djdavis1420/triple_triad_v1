import random
import copy
from src.models.all_cards import CARDS


class Player:
    def __init__(self):
        self.deck = copy.deepcopy(CARDS)
        self.hand = []
        self.cards = []
        self.name = None
        self.generate_hand()
        self.generate_cards()

    def generate_hand(self):
        while len(self.hand) < 5:
            self.hand.append(random.choice(self.deck))
        return self.hand

    def generate_cards(self):
        for item in self.hand:
            self.cards.append(item['name'])
        return self.cards

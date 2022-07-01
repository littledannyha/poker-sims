import itertools

from typing import List, Tuple

from treys.evaluator import Evaluator
from treys.deck import Deck
from treys.card import Card

ALL_CARD_STRINGS = [x[0] + x[1] for x in itertools.product(Card.STR_RANKS, ['c','d','h','s'])]

def generate_hand(hand_str: str)-> List[Card]:
  """Generates hand from a space separated list of cards
     Example: As 2c 3h 4d 5s
  """
  return [Card.new(x) for x in hand_str.split()]

def pp_hands(hand_combos: List[Tuple[Card]]) -> None:
  """Print out an arrary of hands"""
  for hand in hand_combos:
    Card.print_pretty_cards(hand)


class Round:
    def __init__(self):
        self.evaluator = Evaluator()
        self.deck = Deck()
        self.hand = self.deck.draw(5)

    def print_hand(self):
        Card.print_pretty_cards(self.hand)


    @staticmethod
    def all_hands():
        return ([Card.new(card) for card in cards] for cards in itertools.combinations(ALL_CARD_STRINGS, 5))


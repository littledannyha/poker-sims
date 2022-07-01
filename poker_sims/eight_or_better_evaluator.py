import itertools
from typing import Sequence, List
from collections import Counter

from treys.card import Card
from util import pp_hands


class EightOrBetterEvaluator:
    """

    """

    VALID_RANKS = {12, 0, 1, 2, 3, 4, 5, 6} # A thru 8 ranks
    RANKS_WITH_ACES_LOW = {-1, 0, 1, 2, 3, 4, 5, 6} # A thru 8 ranks
    ALL_COMBOS = [tuple(sorted(hand)) for hand in itertools.combinations(RANKS_WITH_ACES_LOW, 5)]
    COMBOS_BY_RANK = {combo: rank for rank, combo in enumerate(sorted(ALL_COMBOS))}
    
    

    def __init__(self) -> None:
      pass

    @staticmethod
    def convert_hand_to_sorted_rank_tuple(hand: List[Card]) -> List[int]:
      return tuple(sorted([Card.get_rank_int(card) if Card.get_rank_int(card) != 12 else -1 for card in hand]))

    @staticmethod
    def valid_eight_or_better_hand(cards: list[int]) -> bool:
      if len(cards) != 5:
        return False

      rank_counts = Counter([Card.get_rank_int(c) for c in cards])
      if max(rank_counts.values()) > 1:
        return False

      return all([rank in EightOrBetterEvaluator.VALID_RANKS for rank in rank_counts])

    def evaluate(self, cards: list[int], board: list[int]) -> int:
        """
        This is the function that the user calls to get a hand rank. 

        No input validation because that's cycles!
        """
        all_hand_combos = [x for x in itertools.combinations(cards, 2)]
        all_board_combos = [x for x in itertools.combinations(cards, 3)]
        all_possible_combos = [x for x in itertools.product(all_hand_combos, all_board_combos)]
        all_valid_eight_or_better_hands = [EightOrBetterEvaluator.convert_hand_to_sorted_rank_tuple(x[0] + x[1]) for x in all_possible_combos if EightOrBetterEvaluator.valid_eight_or_better_hand(x[0] + x[1])]
        if not all_valid_eight_or_better_hands:
          return None

        return min([EightOrBetterEvaluator.COMBOS_BY_RANK[tuple(sorted(hand))] for hand in all_valid_eight_or_better_hands])


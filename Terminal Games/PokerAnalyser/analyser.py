import random
from itertools import combinations
from collections import Counter
from typing import List

# Define the card deck
SUITS = ["H", "D", "C", "S"]  # Hearts, Diamonds, Clubs, Spades
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
DECK = [f"{rank}{suit}" for rank in RANKS for suit in SUITS]


class PokerAnalyzer:
    def __init__(self):
        self.in_hand_cards = []
        self.community_cards = []

    def set_in_hand_cards(self, cards: List[str]):
        self.validate_cards(cards)
        self.in_hand_cards = cards

    def set_community_cards(self, cards: List[str]):
        self.validate_cards(cards)
        self.community_cards = cards

    def rank_hand(self, hand):
        """Evaluate the rank of a poker hand."""
        # Separate ranks and suits
        ranks = [card[:-1] for card in hand]
        suits = [card[-1] for card in hand]

        # Convert rank to values for comparison
        rank_values = sorted([RANKS.index(rank) for rank in ranks], reverse=True)
        rank_count = Counter(rank_values)
        suit_count = Counter(suits)

        # Check for flush
        is_flush = any(count >= 5 for count in suit_count.values())
        # Check for straight
        is_straight = any(
            all(rank + offset in rank_values for offset in range(5))
            for rank in rank_values
        )
        # Special case: Ace-low straight
        if set(rank_values[-4:]) == {12, 0, 1, 2, 3}:
            is_straight = True

        # Determine hand rank
        if is_straight and is_flush:
            return (8, rank_values)  # Straight flush
        elif 4 in rank_count.values():
            return (7, rank_values)  # Four of a kind
        elif sorted(rank_count.values()) == [2, 3]:
            return (6, rank_values)  # Full house
        elif is_flush:
            return (5, rank_values)  # Flush
        elif is_straight:
            return (4, rank_values)  # Straight
        elif 3 in rank_count.values():
            return (3, rank_values)  # Three of a kind
        elif list(rank_count.values()).count(2) == 2:
            return (2, rank_values)  # Two pair
        elif 2 in rank_count.values():
            return (1, rank_values)  # One pair
        else:
            return (0, rank_values)  # High card

    def simulate(self, num_simulations: int = 10000):
        """Simulate games to calculate probabilities based on hand rankings."""
        remaining_deck = [
            card
            for card in DECK
            if card not in self.in_hand_cards + self.community_cards
        ]
        my_wins = 0
        opponent_wins = 0
        my_best_hand = []
        opponent_best_hand = []

        for _ in range(num_simulations):
            random.shuffle(remaining_deck)
            opponent_hand = remaining_deck[:2]
            community = (
                self.community_cards + remaining_deck[2 : 7 - len(self.community_cards)]
            )

            # Form full hands
            my_hand = self.in_hand_cards + community
            opponent_full_hand = opponent_hand + community

            # Evaluate hands
            my_rank = self.rank_hand(my_hand)
            opponent_rank = self.rank_hand(opponent_full_hand)

            # Update best hands
            if my_rank > self.rank_hand(my_best_hand):
                my_best_hand = my_hand
            if opponent_rank > self.rank_hand(opponent_best_hand):
                opponent_best_hand = opponent_full_hand

            # Determine winner
            if my_rank > opponent_rank:
                my_wins += 1
            elif opponent_rank > my_rank:
                opponent_wins += 1

        winning_percentage = (my_wins / num_simulations) * 100
        return winning_percentage, my_best_hand, opponent_best_hand

    def print_results(self, winning_percentage, my_hand, opponent_hand):
        print(f"Winning Percentage: {winning_percentage:.2f}%")
        print(f"Your Probable Winning Hand: {', '.join(my_hand)}")
        print(f"Opponent's Best Hand: {', '.join(opponent_hand)}")

    def validate_cards(self, cards: List[str]):
        """Validate card inputs."""
        valid_suits = set(SUITS)
        valid_ranks = set(RANKS)
        for card in cards:
            if len(card) < 2 or len(card) > 3:
                raise ValueError(f"Invalid card format: {card}")
            rank, suit = card[:-1], card[-1]
            if rank not in valid_ranks or suit not in valid_suits:
                raise ValueError(f"Invalid card: {card}")


def shorthand_to_full(cards: List[str]) -> List[str]:
    """Convert shorthand cards to full card names with validation."""
    suit_map = {"H": "Hearts", "D": "Diamonds", "C": "Clubs", "S": "Spades"}
    valid_ranks = set(RANKS)  # ['2', '3', ..., 'A']
    valid_suits = set(suit_map.keys())  # ['H', 'D', 'C', 'S']

    full_cards = []
    for card in cards:
        if len(card) < 2 or len(card) > 3:  # e.g., "3D" or "10H"
            raise ValueError(f"Invalid card format: {card}")
        rank, suit = card[:-1], card[-1]
        if rank not in valid_ranks or suit not in valid_suits:
            raise ValueError(f"Invalid card: {card}")
        full_cards.append(f"{rank} of {suit_map[suit]}")
    return full_cards


def get_cards(prompt: str) -> List[str]:
    while True:
        try:
            cards = input(prompt).upper().split(", ")
            # Validate the input
            shorthand_to_full(cards)
            return cards
        except ValueError as e:
            print(f"Error: {e}. Please try again.")


def main():
    analyzer = PokerAnalyzer()

    print("Welcome to Texas Hold'em Poker Analyzer!")
    in_hand = get_cards("Enter your hand cards (e.g., '3D, 4C'): ")
    analyzer.set_in_hand_cards(in_hand)

    community = get_cards("Enter the community cards (if available, e.g., '5H, 6S'): ")
    analyzer.set_community_cards(community)

    num_simulations = input("Enter number of simulations (default 10,000): ")
    num_simulations = int(num_simulations) if num_simulations else 10000

    winning_percentage, my_hand, opponent_hand = analyzer.simulate(num_simulations)

    # Convert shorthand back to full names for output
    my_hand_full = shorthand_to_full(my_hand)
    opponent_hand_full = shorthand_to_full(opponent_hand)

    analyzer.print_results(winning_percentage, my_hand_full, opponent_hand_full)


if __name__ == "__main__":
    main()


# 2D, 3C
# 5D, 10C, KD

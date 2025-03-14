from analyser import PokerAnalyzer, shorthand_to_full


def automated_test():
    analyzer = PokerAnalyzer()

    # Test Case 1: Basic Hand and Community Cards
    print("=== Test Case 1 ===")
    analyzer.set_in_hand_cards(["3D", "4C"])
    analyzer.set_community_cards(["5H", "6S", "7C"])
    winning_percentage, my_hand, opponent_hand = analyzer.simulate(1000)
    print(f"Winning Percentage: {winning_percentage:.2f}%")
    print(f"My Best Hand: {shorthand_to_full(my_hand)}")
    print(f"Opponent's Best Hand: {shorthand_to_full(opponent_hand)}\n")

    # Test Case 2: Another Set of Inputs
    print("=== Test Case 2 ===")
    analyzer.set_in_hand_cards(["KH", "AD"])
    analyzer.set_community_cards(["10S", "JD", "QS"])
    winning_percentage, my_hand, opponent_hand = analyzer.simulate(1000)
    print(f"Winning Percentage: {winning_percentage:.2f}%")
    print(f"My Best Hand: {shorthand_to_full(my_hand)}")
    print(f"Opponent's Best Hand: {shorthand_to_full(opponent_hand)}\n")


if __name__ == "__main__":
    automated_test()

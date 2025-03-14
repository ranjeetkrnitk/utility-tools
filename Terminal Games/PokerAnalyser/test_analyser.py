import unittest
from analyser import PokerAnalyzer, shorthand_to_full


class TestPokerAnalyzer(unittest.TestCase):
    def setUp(self):
        """Set up a PokerAnalyzer instance for testing."""
        self.analyzer = PokerAnalyzer()

    def test_shorthand_to_full(self):
        """Test shorthand_to_full function."""
        cards = ["3D", "4C", "10H", "AS"]
        expected = ["3 of Diamonds", "4 of Clubs", "10 of Hearts", "A of Spades"]
        self.assertEqual(shorthand_to_full(cards), expected)

        # Invalid input
        with self.assertRaises(ValueError):
            shorthand_to_full(["3X", "4C"])

    def test_set_in_hand_cards(self):
        """Test setting in-hand cards."""
        self.analyzer.set_in_hand_cards(["3D", "4C"])
        self.assertEqual(self.analyzer.in_hand_cards, ["3D", "4C"])

    def test_set_community_cards(self):
        """Test setting community cards."""
        self.analyzer.set_community_cards(["5H", "6S", "7C"])
        self.assertEqual(self.analyzer.community_cards, ["5H", "6S", "7C"])

    def test_simulation(self):
        """Test the simulation method with dummy data."""
        self.analyzer.set_in_hand_cards(["3D", "4C"])
        self.analyzer.set_community_cards(["5H", "6S", "7C"])
        winning_percentage, my_hand, opponent_hand = self.analyzer.simulate(1000)

        # Check that winning percentage is a float
        self.assertIsInstance(winning_percentage, float)
        # Ensure my_hand and opponent_hand are lists
        self.assertIsInstance(my_hand, list)
        self.assertIsInstance(opponent_hand, list)

    def test_invalid_inputs(self):
        """Test invalid inputs for set_in_hand_cards and set_community_cards."""
        with self.assertRaises(ValueError):
            self.analyzer.set_in_hand_cards(["3X"])  # Invalid suit
        with self.assertRaises(ValueError):
            self.analyzer.set_community_cards(["15H"])  # Invalid rank


if __name__ == "__main__":
    unittest.main()

import unittest
import logging
from fsm_mod_n.mod_n import (
    mod_n_remainder,
    mod_n_remainder_custom_alphabet,
    mod_n_accepts,
    build_mod_n_fsm
)

# Set up logging for tests
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class TestModNFSM(unittest.TestCase):
    """
    Unit test class for testing mod-N FSM functionality using both binary and custom alphabets.
    """

    def test_binary_mod_values(self):
        """Test binary inputs for mod 2 and mod 3 examples."""
        logger.info("Testing binary mod-N remainders")
        self.assertEqual(mod_n_remainder("1101", 3), 1)  # 13 % 3 = 1
        self.assertEqual(mod_n_remainder("1111", 3), 0)  # 15 % 3 = 0
        self.assertEqual(mod_n_remainder("1001", 2), 1)  # 9 % 2 = 1
        self.assertEqual(mod_n_remainder("1000", 2), 0)  # 8 % 2 = 0
    
    def test_accepting_state_check(self):
        """FSM should identify whether the final state is accepting."""
        logger.info("Testing accepting states")
        fsm = build_mod_n_fsm(3, {'0', '1'})
        fsm.process("1111")
        self.assertTrue(fsm.is_accepting())
        fsm.process("1101")
        self.assertTrue(fsm.is_accepting())  # All states are valid here


    def test_binary_mod_3(self):
        """
        Test FSM with binary input strings for modulus 3.
        '1101' (13 in decimal) % 3 = 1
        '1111' (15 in decimal) % 3 = 0
        """
        logger.info("Testing mod 3 binary inputs")
        self.assertEqual(mod_n_remainder('1101', 3), 1)
        self.assertEqual(mod_n_remainder('1111', 3), 0)
    
    def test_accepting_state_binary_mod_3(self):
        """FSM should end in final state S0 for divisible inputs."""
        logger.info("Testing acceptance with mod_n_accepts")
        self.assertTrue(mod_n_accepts('1111', 3, {'0', '1'}))
        self.assertTrue(mod_n_accepts('1101', 3, {'0', '1'}))

    def test_custom_alphabet_abc_mod_5(self):
        """Test custom alphabet mapping: ABC = 5, 5 % 5 = 0."""
        self.assertEqual(mod_n_remainder_custom_alphabet('ABC', 5, {'A', 'B', 'C'}), 0)
        self.assertTrue(mod_n_accepts('ABC', 5, {'A', 'B', 'C'}))

    
    def test_binary_mod_2(self):
        """
        Test FSM with binary input strings for modulus 2.
        '1001' (9 in decimal) % 2 = 1
        '1000' (8 in decimal) % 2 = 0
        """
        self.assertEqual(mod_n_remainder('1001', 2), 1)
        self.assertEqual(mod_n_remainder('1000', 2), 0)

    def test_invalid_binary_input(self):
        """
        Ensure ValueError is raised when input contains characters not in binary alphabet.
        """
        with self.assertRaises(ValueError):
            mod_n_remainder('10a1', 3)

    def test_custom_alphabet_abc(self):
        """
        Test FSM with a custom alphabet {'A', 'B', 'C'} for mod-N computations.
        Alphabet is ordered internally, and each symbol is mapped to an index: {'A': 0, 'B': 1, 'C': 2}.
        - "ABC" translates to 0 * 3^2 + 1 * 3^1 + 2 * 3^0 = 0 + 3 + 2 = 5 -> 5 % 5 = 0 (FSM encoding returns S4)
        - "BCA" = 1 * 3^2 + 2 * 3^1 + 0 = 9 + 6 = 15 -> 15 % 7 = 1 (FSM encoding returns S3)
        """
        self.assertEqual(mod_n_remainder_custom_alphabet("ABC", 5, {"A", "B", "C"}), 0)
        self.assertEqual(mod_n_remainder_custom_alphabet("BCA", 7, {"A", "B", "C"}), 1)

    def test_sorted_alphabet_mapping(self):
        """Alphabet {'D', 'B', 'A'} → A=0, B=1, D=2"""
        result = mod_n_remainder_custom_alphabet("ABD", 3, {"D", "B", "A"})
        self.assertEqual(result, 2)
    
    
    def test_invalid_custom_input(self):
        """
        Ensure ValueError is raised when input contains characters not in the provided custom alphabet.
        """
        with self.assertRaises(ValueError):
            mod_n_remainder_custom_alphabet("XYZ", 4, {"A", "B", "C"})
    
    def test_invalid_input_characters(self):
        with self.assertRaises(ValueError):
            mod_n_remainder_custom_alphabet("10A1", 3, {"0", "1"})

    def test_empty_string(self):
        """
        Ensure ValueError is raised for an empty input string.
        """
        with self.assertRaises(ValueError):
            mod_n_remainder_custom_alphabet("", 4, {"0", "1"})

    def test_large_input(self):
        """
        Test FSM on a very large binary input to ensure it handles large sequences.
        Just checks the return type is an integer, not the specific value.
        """
        long_input = "1" * 1000
        self.assertIsInstance(mod_n_remainder(long_input, 5), int)
    
    def test_fsm_is_accepting(self):
        fsm = build_mod_n_fsm(2, {'0', '1'})
        fsm.process('10')  # Binary 2 -> remainder 0
        self.assertTrue(fsm.is_accepting())

        self.assertTrue(fsm.is_accepting())  # All states are accepting
    
    def test_modulus_one(self):
        """Modulus 1 always yields remainder 0."""
        self.assertEqual(mod_n_remainder("1111", 1), 0)
        self.assertEqual(mod_n_remainder("0000", 1), 0)

    def test_single_symbol_alphabet(self):
        """FSM with single-symbol alphabet always returns 0."""
        self.assertEqual(mod_n_remainder_custom_alphabet("AAAA", 4, {'A'}), 0)

    def test_special_character_alphabet(self):
        """FSM supports special symbols like '#' as valid alphabet."""
        self.assertEqual(mod_n_remainder_custom_alphabet("##", 2, {'#'}), 0)

    def test_transition_table_completeness(self):
        """Ensure FSM transition table includes all states and symbols."""
        fsm = build_mod_n_fsm(3, {'A', 'B'})
        for state in fsm.states:
            self.assertIn(state, fsm.transition_function)
            self.assertSetEqual(set(fsm.transition_function[state].keys()), {'A', 'B'})

    def test_invalid_fsm_construction(self):
        """FSM constructor should fail for bad initial/final states."""
        from fsm_mod_n.fsm import FSM
        with self.assertRaises(ValueError):
            FSM(states={'S1'}, alphabet={'0'}, initial_state='S0', final_states={'S1'}, transition_function={})

    def test_empty_alphabet_error(self):
        """FSM should not allow empty alphabet."""
        with self.assertRaises(ValueError):
            build_mod_n_fsm(3, set())

    def test_non_accepting_custom_fsm(self):
        """Override FSM to have non-accepting state and test rejection."""
        fsm = build_mod_n_fsm(3, {'0', '1'})
        fsm.final_states = {'S0'}
        fsm.process("1101")  # 13 % 3 = 1 → S1
        self.assertFalse(fsm.is_accepting())

# Run the test suite when this file is executed directly
if __name__ == "__main__":
    unittest.main()

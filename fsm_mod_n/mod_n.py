import logging
from typing import Dict, Set
from fsm_mod_n.fsm import FSM  # Importing the generic FSM class

# Set up logger for this module
logger = logging.getLogger(__name__)

def build_mod_n_fsm(n: int, alphabet: Set[str]) -> FSM:
    """
    Constructs a finite state machine (FSM) that computes the remainder
    of a number (represented using a given alphabet) modulo n.

    Alphabet is sorted and each symbol is assigned a digit:
    Example: {'C', 'A', 'B'} → A=0, B=1, C=2.

    Args:
        n (int): The modulus value.
        alphabet (Set[str]): Set of valid input symbols.

    Returns:
        FSM: A configured FSM capable of computing mod-n remainder.
    """
    if n <= 0:
        raise ValueError("Modulus must be positive.")
    if not alphabet:
        raise ValueError("Alphabet must not be empty.")

    logger.info(f"Building FSM for mod {n} with alphabet {alphabet}")

    # Create a state for each possible remainder value: S0 to S(n-1)
    states = {f"S{i}" for i in range(n)}
    initial_state = 'S0'  # Start at remainder 0
    final_states = states  # All states are considered valid final states

    transition_function: Dict[str, Dict[str, str]] = {}

    # Sort the alphabet to ensure consistent indexing
    sorted_alphabet = sorted(alphabet)

    # Map each symbol in the alphabet to a unique integer value
    symbol_map = {symbol: idx for idx, symbol in enumerate(sorted_alphabet)}

    # Build the transition table
    for i in range(n):  # For each state
        transitions = {}
        for symbol in alphabet:
            val = symbol_map[symbol]
            # Compute next state based on current state and input symbol
            next_state = (i * len(alphabet) + val) % n
            transitions[symbol] = f'S{next_state}'
        transition_function[f'S{i}'] = transitions

    # Return an FSM instance with all required components
    return FSM(states, alphabet, initial_state, final_states, transition_function)

def mod_n_remainder_custom_alphabet(input_string: str, n: int, alphabet: Set[str]) -> int:
    """
    Uses a finite state machine to compute the remainder of a string-based number
    in a custom alphabet modulo n.

    Args:
        input_string (str): The input string to process.
        n (int): The modulus value.
        alphabet (Set[str]): The set of valid input symbols.

    Returns:
        int: The remainder of the number represented by the input string modulo n.
    """
    if not input_string:
        raise ValueError("Input string cannot be empty.")

    # Ensure every character in the input is valid
    if any(ch not in alphabet for ch in input_string):
        raise ValueError(f"Invalid character in input string. Valid alphabet: {alphabet}")

    # Build the FSM for the given alphabet and modulus
    fsm = build_mod_n_fsm(n, alphabet)

    # Process the input string through the FSM
    final_state = fsm.process(input_string)

    # Extract the numeric remainder from the final state name (e.g., 'S2' -> 2)
    return int(final_state[1:])

def mod_n_remainder(binary_string: str, n: int) -> int:
    """
    Convenience wrapper for computing mod-n remainder using a binary alphabet.

    Args:
        binary_string (str): Input string composed of '0' and '1'.
        n (int): The modulus value.

    Returns:
        int: The remainder of the binary number modulo n.
    """
    return mod_n_remainder_custom_alphabet(binary_string, n, {'0', '1'})


def mod_n_accepts(input_string: str, n: int, alphabet: Set[str]) -> bool:
    """Returns True if the FSM ends in an accepting state."""
    fsm = build_mod_n_fsm(n, alphabet)
    fsm.process(input_string)
    return fsm.is_accepting()
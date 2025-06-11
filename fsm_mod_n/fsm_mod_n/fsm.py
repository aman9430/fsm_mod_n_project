import logging
from typing import Any, Dict, Set

# Configure logging to write messages to 'fsm.log' with time, level, and message.
logging.basicConfig(
    filename='fsm.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class FSM:
    """
    A generic Finite State Machine (FSM) implementation.

    Attributes:
        states (Set[Any]): Set of all possible states.
        alphabet (Set[Any]): Set of input symbols.
        initial_state (Any): The initial state of the FSM.
        final_states (Set[Any]): Set of final/accepting states.
        transition_function (Dict[Any, Dict[Any, Any]]): State transition rules.
        current_state (Any): Current state of the FSM during processing.
    """

    def __init__(
        self,
        states: Set[Any],
        alphabet: Set[Any],
        initial_state: Any,
        final_states: Set[Any],
        transition_function: Dict[Any, Dict[Any, Any]]
    ):
        # Validate that the initial state is within the defined states
        if initial_state not in states:
            raise ValueError("Initial state must be one of the defined states.")
        
        # Validate that all final states are within the defined states
        if not final_states.issubset(states):
            raise ValueError("Final states must be a subset of the states.")

        # Initialize FSM attributes
        self.states = states
        self.alphabet = alphabet
        self.initial_state = initial_state
        self.final_states = final_states
        self.transition_function = transition_function
        self.current_state = initial_state

        logger.info(f"FSM initialized with states={states}, alphabet={alphabet}, initial_state={initial_state}")

    def reset(self):
        """
        Resets the FSM to the initial state.
        """
        self.current_state = self.initial_state
        logger.debug("FSM reset to initial state")

    def transition(self, symbol: Any):
        """
        Performs a state transition based on the current state and input symbol.

        Args:
            symbol (Any): The input symbol.

        Raises:
            ValueError: If the symbol is not in the FSM's alphabet.
        """
        if symbol not in self.alphabet:
            logger.error(f"Symbol '{symbol}' not in alphabet {self.alphabet}")
            raise ValueError(f"Invalid symbol: {symbol}")

        # Retrieve the next state from the transition function
        next_state = self.transition_function[self.current_state][symbol]
        logger.info(f"Transition: ({self.current_state}, '{symbol}') -> {next_state}")
        self.current_state = next_state

    def process(self, input_sequence: str) -> Any:
        """
        Processes a sequence of input symbols through the FSM.

        Args:
            input_sequence (str): Sequence of input symbols.

        Returns:
            Any: The final state after processing the sequence.
        """
        self.reset()
        logger.info(f"Processing input: {input_sequence}")
        
        for symbol in input_sequence:
            self.transition(symbol)
        
        logger.info(f"Final state: {self.current_state}")
        return self.current_state
    
    def is_accepting(self) -> bool:
        """Returns True if the current state is a final (accepting) state."""
        return self.current_state in self.final_states

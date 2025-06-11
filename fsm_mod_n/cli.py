import argparse
from fsm_mod_n.mod_n import mod_n_remainder_custom_alphabet

def main():
    # Set up argument parser for command-line inputs
    parser = argparse.ArgumentParser(description="FSM-based mod-N calculator for custom alphabets.")
    
    # Required positional argument: input string to be evaluated
    parser.add_argument("input_string", help="Input string to compute remainder")
    
    # Required positional argument: modulus N
    parser.add_argument("modulus", type=int, help="Modulus N")
    
    # Optional argument: custom alphabet as a comma-separated string (defaults to binary alphabet "0,1")
    parser.add_argument("--alphabet", help="Comma-separated alphabet (default: 0,1)", default="0,1")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Convert the comma-separated alphabet string into a set of characters
    alphabet = set(args.alphabet.split(","))

    try:
        # Call the FSM-based function to compute the remainder
        remainder = mod_n_remainder_custom_alphabet(args.input_string, args.modulus, alphabet)
        
        # Output the result to the console
        print(f"Remainder of {args.input_string} mod {args.modulus} = {remainder}")
    except ValueError as e:
        # Catch and print any input-related or FSM-related errors
        print(f"Error: {e}")

# Execute the main function when the script is run directly
if __name__ == "__main__":
    main()


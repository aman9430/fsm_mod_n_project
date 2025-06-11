# FSM Mod-N Calculator

A generic Finite State Machine (FSM) library to compute the remainder of a number represented as a string in a custom alphabet, modulo **N**, without converting it to an integer. This project includes a CLI tool and comprehensive unit tests.

---

## Features

- Generic FSM implementation using object-oriented design
- Support for any modulus **N**
- Custom alphabets (not limited to binary)
- Command-line interface (CLI)
- Comprehensive unit tests using `unittest`
- Logging of FSM transitions to `fsm.log`

---

## Project Structure

```

fsm\_mod\_n\_project/
├── fsm\_mod\_n/
│   ├── __init__.py
│   ├── fsm.py          # Generic FSM class
│   ├── mod_n.py        # Mod-N FSM builder and logic
│   └── cli.py          # CLI entry point
├── tests/
│   ├── __init__.py
│   └── test_mod_n.py   # Unit tests for FSM functionality
├── setup.py            # Project setup for packaging
├── requirements.txt    # Optional dependencies file
└── README.md           # Project documentation

````

---

## Installation

```bash
# Clone the repo
git clone https://github.com/your-username/fsm_mod_n_project.git
cd fsm_mod_n_project

# Install the package
pip install .
````

> Alternatively, for development:

```bash
pip install -e .
```

---

## Running Tests

```bash
python -m unittest discover tests
```

---

## Usage

### CLI

```bash
fsm-cli <input_string> <modulus> [--alphabet <comma-separated-alphabet>]
```

### Examples

```bash
fsm-cli 1101 3
# Output: Remainder of 1101 mod 3 = 1

fsm-cli ABC 5 --alphabet A,B,C
# Output: Remainder of ABC mod 5 = 0
```

---

## FSM Mod-N Concept

The FSM avoids converting the input string to an integer and instead:

* Uses states `S0` to `S(N-1)` for remainder tracking.
* Transitions through states based on current symbol and state.
* Returns the final state's numeric value as the remainder.

---

## Example FSM Transition Table (Mod 3, Binary)

| Current State | Input = 0 | Input = 1 |
| ------------- | --------- | --------- |
| S0            | S0        | S1        |
| S1            | S2        | S0        |
| S2            | S1        | S2        |

---

## Sample Test Coverage

* Binary FSM (mod 2, 3)
* Custom alphabets (e.g., `A, B, C`)
* Large input sequences
* Edge cases (empty string, invalid characters)
* FSM acceptance checks

Run tests with:

```bash
python -m unittest tests/test_mod_n.py
```

---
## Author

**Aman Singh**
[amansingh940330@gmail.com](mailto:amansingh940330@gmail.com)

---

## Requirements (optional)

```text
Python >= 3.7
```

---

## TODO (Optional)

* Add support for FSM visualization
* Add JSON/YAML FSM config support
* Use `pytest`, validate FSM structure directly
* CI/CD add GitHub Actions for automatic testing
* Add `Dockerfile` for containerization
* Add `pyproject.toml` for modern packaging


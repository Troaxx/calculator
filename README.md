# Calculator

A simple command-line calculator application written in Python that performs basic arithmetic operations.

## Description

This calculator is a user-friendly command-line application that allows users to perform basic mathematical operations including addition, subtraction, multiplication, division, and exponentiation. The program runs in a loop, allowing users to perform multiple calculations until they choose to exit.

## Features

- Addition of two numbers
- Subtraction of two numbers
- Multiplication of two numbers
- Division of two numbers
- Exponentiation (raising a number to a power)
- Clean menu-driven interface
- Input validation

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Troaxx/calculator.git
   ```

2. Navigate to the project directory:
   ```bash
   cd calculator
   ```

3. Run the calculator:
   ```bash
   python calculator.py
   ```

## Usage

1. Run the program using the command above
2. Select an operation from the menu by entering the corresponding number (1-6)
3. Follow the prompts to enter the required numbers
4. View the result
5. Continue with more calculations or select option 6 to quit

Example:
```
Welcome to the Calculator Menu!
1 | Add
2 | Subtract
3 | Multiply
4 | Exponents
5 | Divide
6 | Quit

Pick an option from the options above: 1
Enter the first number 5
Enter the second number 3
Total: 8.0
```

## Functions

- `add_menu()`: Adds two numbers
- `subtract_menu()`: Subtracts the second number from the first
- `multiplication()`: Multiplies two numbers
- `exponents()`: Raises the first number to the power of the second
- `division()`: Divides the first number by the second
- `main()`: Contains the menu loop and handles user input

## Error Handling

The calculator handles basic input errors. When an invalid menu option is selected, an appropriate error message is displayed.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Troaxx (danny)

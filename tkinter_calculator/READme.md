# Python Calculator with Tkinter

## Overview
This is a simple **Python Calculator** application built using the **Tkinter** library. It supports basic arithmetic operations like **addition**, **subtraction**, **multiplication**, **division**, **modulus**, as well as **square** and **square root** functionalities.

The app provides an easy-to-use GUI for performing mathematical calculations with a user-friendly interface.

## Features
- **Basic operations**: Addition, Subtraction, Multiplication, Division
- **Additional operations**: Modulus, Square, Square Root
- **Error handling**: Handles division by zero and invalid inputs gracefully
- **Responsive GUI**: Built using Tkinter for a simple, interactive user interface

## Requirements
Before running the program, make sure you have Python installed on your system. The program uses the following libraries:
- **Tkinter** (comes pre-installed with Python)
- **math** (comes pre-installed with Python)

To check if you have Tkinter installed, you can run the following command:
```bash
python -m tkinter
```
## If Tkinter is installed, a small window will appear.

## Installation
You can run the Python calculator directly without any installation steps, as the code uses built-in Python libraries.

1. **Clone or Download** this repository:
   ```bash
   git clone https://github.com/yourusername/calculator-app.git
   ```
2. **Navigate to the directory** where the code is saved.

3. **Run the Python script**:
   ```bash
   python calculator.py
   ```

## How It Works

The application creates a graphical user interface (GUI) with buttons for each number, operator, and special function. Here’s how the app works:

- **User Interaction**: When the user presses buttons (numbers, operators, etc.), the corresponding value is added to the input box.
- **Evaluate Expression**: Pressing the `=` button evaluates the mathematical expression entered in the input box using Python’s `eval()` function.
- **Display Result**: The result is displayed in the input box.

## Code Explanation

### Key Functions

- **`press(key)`**: This function appends the pressed key (number or operator) to the input field.
- **`clear()`**: Clears the input field.
- **`equal()`**: Evaluates the mathematical expression entered in the input field using the `eval()` function. Displays the result or an error message if the input is invalid.
- **`square()`**: Computes the square of the input number.
- **`square_root()`**: Computes the square root of the input number.

## How to Use
- **Input**: Type numbers and operators using the calculator's buttons.
- **Clear**: Click the "C" button to clear the current input.
- **Square**: Click "x²" to calculate the square of the number.
- **Square Root**: Click "√" to calculate the square root.
- **Evaluate**: Click "=" to evaluate the mathematical expression.

## License
This project is open-source and available for personal and educational use. Feel free to modify and enhance it as you see fit.

## Contact
If you have any questions or feedback, feel free to reach out via [divyabgowda034@gmail.com].

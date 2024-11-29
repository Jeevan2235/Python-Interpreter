# Python Interpreter for a Simplified Programming Language

## Project Overview
This project is a Python-based interpreter designed to process and execute code written in a simplified programming language. The interpreter works by performing lexical analysis, parsing the input to create an Abstract Syntax Tree (AST), and executing the resulting instructions. It demonstrates key concepts of interpreter design, including tokenization, parsing, and AST traversal, providing practical insight into these fundamental areas.

The project was completed as part of the **CS 609: Final Project Assignment** at Southeast Missouri State University, adhering to the requirements specified in the course guidelines.

---

## Key Features
1. **Variable Declaration and Initialization**
   - Allows defining variables and assigning values.
   - Example:
     ```python
     let a = 5;
     let b = a + 3;
     ```

2. **Support for Arithmetic Operations**
   - Performs basic mathematical operations such as addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`).
   - Example:
     ```python
     let c = a * b;
     ```

3. **Printing Output**
   - Outputs the values of variables using a `print` statement.
   - Example:
     ```python
     print(a);
     print(c);
     ```

4. **Sequential Execution**
   - Executes multiple statements in the order they appear.
   - Example:
     ```python
     let x = 10;
     let y = x * 2;
     print(x);
     print(y);
     ```

5. **Handling Whitespace and Semicolons**
   - Ignores whitespace and requires statements to end with a semicolon (`;`).

---

## Project Structure
1. **`lexer.py`**
   - Breaks the input source code into tokens, including keywords, identifiers, numbers, operators, and punctuation.

2. **`parser.py`**
   - Converts the tokens into an Abstract Syntax Tree (AST), representing the logical structure of the program.

3. **`ast_nodes.py`**
   - Defines the classes for different AST node types, such as `AssignNode`, `BinOpNode`, and `PrintNode`.

4. **`interpreter.py`**
   - Interprets the AST by evaluating expressions, handling variable assignments, and executing print commands.

5. **`examples/`**
   - Contains example programs and test cases to showcase the interpreter's functionality.

---

## How to Use

### Requirements
- Python 3.7 or newer.

### Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/Jeevan2235/Python-Interpreter.git
   cd interpreter

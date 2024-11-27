import os
from Lexer import Lexer
from Parser import Parser
from Interpreter import Interpreter

def main(input_file):
    # Grab the input file and read its contents
    with open(input_file, 'r') as file:
        source_code = file.read()
    
    # Turn the source code into tokens (break it into chunks)
    lexer = Lexer(source_code)
    tokens = lexer.tokenize()
    print("Tokens:", tokens)  # Optional: Print tokens for debugging, if needed
    
    # Take those tokens and turn them into an AST (structured representation)
    parser = Parser(tokens)
    ast = []
    while parser.current_pos < len(tokens):  # Keep parsing until we're out of tokens
        ast.append(parser.parse())
    
    # Run the AST through the interpreter to get results
    interpreter = Interpreter()
    for node in ast:
        interpreter.visit(node)

if __name__ == "__main__":
      # Run through all files in the 'examples' folder
      dirname = "./examples"
      for filename in os.listdir(dirname):
            print("The output for file---" + filename + "----- \n")
            main(dirname + "/" + filename)
            print("\n")

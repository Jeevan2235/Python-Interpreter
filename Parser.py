from AST_node import AssignNode, BinOpNode, PrintNode

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_pos = 0

    def parse(self):
        # Figure out what kind of statement we have (assignment or print)
        token_type, token_value = self.tokens[self.current_pos]
        if token_type == "LET":
            node = self.parse_assignment()  # Handle assignment
            self.consume("SEMI")  # Make sure there's a semicolon at the end
            return node
        elif token_type == "PRINT":
            node = self.parse_print()  
            self.consume("SEMI") 
            return node
        else:
            # If it's not something we know, throw an error
            raise SyntaxError(f"Unexpected token: {token_type}")

    def parse_assignment(self):
        # Deal with 'let <ID> = <expression>'
        self.consume("LET") 
        variable_name = self.consume("ID")[1] 
        self.consume("ASSIGN") 
        expr = self.parse_expression() 
        return AssignNode(var_name=variable_name, expr=expr)

    def parse_print(self):
        # Deal with 'print(<expression>)'
        self.consume("PRINT") 
        self.consume("LPAREN")
        expr = self.parse_expression()  # Get the stuff inside the parentheses
        self.consume("RPAREN") 
        return PrintNode(expr=expr)

    def parse_expression(self):
        # Handle numbers, variable names, or parentheses
        if self.tokens[self.current_pos][0] == "LPAREN":
            self.consume("LPAREN") 
            expr = self.parse_expression() 
            self.consume("RPAREN") 
            return expr

        elif self.tokens[self.current_pos][0] in ("NUMBER", "ID"):
            left = self.consume(self.tokens[self.current_pos][0])  # Take the number or variable
        else:
            # If it's none of these, something went wrong
            raise SyntaxError(f"Expected a NUMBER, ID, or LPAREN, got {self.tokens[self.current_pos]}")

        # Deal with binary operators (+, -, *, /)
        while (self.current_pos < len(self.tokens) and 
               self.tokens[self.current_pos][0] in ("PLUS", "MINUS", "MUL", "DIV")):
            op = self.consume(self.tokens[self.current_pos][0])  # Grab the operator
            if self.tokens[self.current_pos][0] in ("NUMBER", "ID", "LPAREN"):
                right = self.parse_expression()  # Parse the right-hand side
                left = BinOpNode(left=left[1], op=op[0], right=right)  # Combine into a binary operation node
            else:
                # Something is missing after the operator
                raise SyntaxError(f"Expected a NUMBER, ID, or LPAREN after {op}, got {self.tokens[self.current_pos]}")

        # Return the final parsed expression
        return left[1] if isinstance(left, tuple) else left

    def consume(self, expected_type):
        # Take the next token if it matches what we want
        if self.current_pos < len(self.tokens) and self.tokens[self.current_pos][0] == expected_type:
            current_token = self.tokens[self.current_pos]
            self.current_pos += 1
            return current_token
        # If it doesn't match, complain loudly
        raise SyntaxError(f"Expected {expected_type}, got {self.tokens[self.current_pos][0]} at position {self.current_pos}")

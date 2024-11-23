import re

class Lexer:

    def __init__(self, source_code):
        #sets up the lexer with the code we are going to process
        self.source_code = source_code
        self.tokens = []

    def tokenize(self):
        #turns the source code into tokens
        patterns = [
            ("NUMBER", r'\d+'),
            ("PLUS", r'\+'),
            ("MINUS", r'-'),
            ("MUL", r'\*'),
            ("DIV", r'/'),
            ("ASSIGN", r'='),
            ("SEMI", r';'),
            ("LPAREN", r'\('),
            ("RPAREN", r'\)'),
            ("WHITESPACE", r'\s+'),
            ("LET", r'let'),
            ("PRINT", r'print'),
            ("ID", r'[a-zA-Z_][a-zA-Z0-9_]*')
        ]
        combined_pattern = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in patterns)

        #go through the code to find the matches
        for match in re.finditer(combined_pattern, self.input_code):
            token_type = match.lastgroup
            token_value = match.group(token_type)

            if token_type != "WHITESPACE": # if it is just whitespace ignore 
                if token_type=="NUMBER": # if it is an number turn into integer
                    token_value = int(token_value)
                    
                # append the tokens
                self.tokens.append((token_type, token_value))

        return self.tokens

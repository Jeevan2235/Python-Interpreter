from AST_node import AssignNode, BinOpNode, PrintNode

class Interpreter:
    def __init__(self):
        self.vars = {}

    def visit(self, node):
        if isinstance(node, AssignNode):
            self.vars[node.var_name] = node.expr  
        elif isinstance(node, BinOpNode):
            if node.op == "PLUS":
                return node.left + node.right
            elif node.op == "MINUS":
                return node.left - node.right
            elif node.op == "MUL":
                return left * right
            elif node.op == "DIV":
                return node.left / node.right
        elif isinstance(node, PrintNode):
            print(node.expr)
        elif isinstance(node, int):
            return node
        elif isinstance(node, str):
            return self.vars[node]
        else:
            raise ValueError("Node type not supported")

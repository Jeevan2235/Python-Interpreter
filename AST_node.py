

class ASTNode:
    pass

class AssignNode(ASTNode):
    def __init__(self, var_name, expr):
        self.var_name = var_name
        self.expr = expr

class BinOpNode(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class PrintNode(ASTNode):
    def __init__(self, expr):
        self.expr = expr

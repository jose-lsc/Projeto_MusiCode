# evaluator.py
from .ast import Program, Assign, Print, BinOp, Num, Var

class EvalError(Exception):
    pass

class Evaluator:
    def __init__(self):
        self.env = {}

    def eval(self, node):
        if isinstance(node, Program):
            result = None
            for s in node.statements:
                result = self.eval(s)
            return result
        if isinstance(node, Assign):
            val = self.eval(node.expr)
            self.env[node.name] = val
            return val
        if isinstance(node, Print):
            val = self.eval(node.expr)
            print(val)
            return val
        if isinstance(node, BinOp):
            l = self.eval(node.left)
            r = self.eval(node.right)
            if node.op == '+': return l + r
            if node.op == '-': return l - r
            if node.op == '*': return l * r
            if node.op == '/':
                if r == 0:
                    raise EvalError("Division by zero")
                return l // r
            raise EvalError(f'Unknown operator {node.op}')
        if isinstance(node, Num):
            return node.value
        if isinstance(node, Var):
            if node.name in self.env:
                return self.env[node.name]
            raise EvalError(f'Undefined variable {node.name}')
        raise EvalError('Unknown AST node')

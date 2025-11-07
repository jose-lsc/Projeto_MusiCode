# parser.py
from typing import List
from .lexer import Token, tokenize
from .ast import Program, Assign, Print, BinOp, Num, Var

class ParserError(Exception):
    pass

class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.pos = 0
        self.cur = self.tokens[self.pos]

    def advance(self):
        self.pos += 1
        if self.pos < len(self.tokens):
            self.cur = self.tokens[self.pos]
        else:
            self.cur = Token('EOF', None, -1, -1)

    def eat(self, token_type):
        if self.cur.type == token_type:
            self.advance()
        else:
            raise ParserError(f'Expected {token_type} but got {self.cur.type} at line {self.cur.line} col {self.cur.col}')

    def parse(self):
        stmts = []
        while self.cur.type != 'EOF':
            if self.cur.type == 'EOF':
                break
            stmts.append(self.statement())
        return Program(stmts)

    def statement(self):
        if self.cur.type == 'ID':
            name = self.cur.value
            self.eat('ID')
            self.eat('ASSIGN')
            expr = self.expr()
            self.eat('SEMI')
            return Assign(name, expr)
        elif self.cur.type == 'PRINT':
            self.eat('PRINT')
            self.eat('LPAREN')
            expr = self.expr()
            self.eat('RPAREN')
            self.eat('SEMI')
            return Print(expr)
        else:
            raise ParserError(f'Invalid statement starting with {self.cur.type} at line {self.cur.line}')

    def expr(self):
        node = self.term()
        while self.cur.type in ('PLUS', 'MINUS'):
            op = self.cur.value
            if self.cur.type == 'PLUS':
                self.eat('PLUS')
            else:
                self.eat('MINUS')
            node = BinOp(node, op, self.term())
        return node

    def term(self):
        node = self.factor()
        while self.cur.type in ('TIMES', 'DIV'):
            op = self.cur.value
            if self.cur.type == 'TIMES':
                self.eat('TIMES')
            else:
                self.eat('DIV')
            node = BinOp(node, op, self.factor())
        return node

    def factor(self):
        tok = self.cur
        if tok.type == 'NUMBER':
            self.eat('NUMBER')
            return Num(int(tok.value))
        elif tok.type == 'ID':
            self.eat('ID')
            return Var(tok.value)
        elif tok.type == 'LPAREN':
            self.eat('LPAREN')
            node = self.expr()
            self.eat('RPAREN')
            return node
        else:
            raise ParserError(f'Unexpected token {tok.type} at line {tok.line} col {tok.col}')

def parse_code(source: str):
    tokens = tokenize(source)
    p = Parser(tokens)
    return p.parse()

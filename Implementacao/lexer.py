# lexer.py
import re
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Token:
    type: str
    value: Optional[str]
    line: int
    col: int

TOKEN_SPEC = [
    ('NUMBER',   r'\d+'),
    ('ID',       r'[A-Za-z_][A-Za-z0-9_]*'),
    ('ASSIGN',   r'='),
    ('PLUS',     r'\+'),
    ('MINUS',    r'-'),
    ('TIMES',    r'\*'),
    ('DIV',      r'/'),
    ('LPAREN',   r'\('),
    ('RPAREN',   r'\)'),
    ('SEMI',     r';'),
    ('SKIP',     r'[ \t]+'),
    ('NEWLINE',  r'\n'),
    ('MISMATCH', r'.'),
]

MASTER_RE = re.compile('|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_SPEC))

KEYWORDS = {'print'}

def tokenize(code: str) -> List[Token]:
    tokens: List[Token] = []
    line = 1
    line_start = 0
    for mo in MASTER_RE.finditer(code):
        kind = mo.lastgroup
        value = mo.group()
        col = mo.start() - line_start + 1
        if kind == 'NUMBER':
            tokens.append(Token('NUMBER', value, line, col))
        elif kind == 'ID':
            if value in KEYWORDS:
                tokens.append(Token(value.upper(), value, line, col))
            else:
                tokens.append(Token('ID', value, line, col))
        elif kind == 'NEWLINE':
            line += 1
            line_start = mo.end()
        elif kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise SyntaxError(f'Unexpected character {value!r} at line {line} col {col}')
        else:
            tokens.append(Token(kind, value, line, col))
    tokens.append(Token('EOF', None, line, 1))
    return tokens

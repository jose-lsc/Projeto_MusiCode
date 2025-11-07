# ast.py
from dataclasses import dataclass
from typing import Any, List

class Node:
    pass

@dataclass
class Program(Node):
    statements: List[Node]

@dataclass
class Assign(Node):
    name: str
    expr: Node

@dataclass
class Print(Node):
    expr: Node

@dataclass
class BinOp(Node):
    left: Node
    op: str
    right: Node

@dataclass
class Num(Node):
    value: int

@dataclass
class Var(Node):
    name: str

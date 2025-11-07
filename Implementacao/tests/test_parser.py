# tests/test_parser.py
import io
import sys
import pytest
from Implementacao.parser import parse_code
from Implementacao.evaluator import Evaluator, EvalError

def capture_stdout(fn, *args, **kwargs):
    old = sys.stdout
    sys.stdout = io.StringIO()
    try:
        fn(*args, **kwargs)
        return sys.stdout.getvalue()
    finally:
        sys.stdout = old

def test_assign_and_print():
    src = """
    x = 1 + 2 * (3 + 4);
    print(x);
    """
    ast = parse_code(src)
    ev = Evaluator()
    out = capture_stdout(ev.eval, ast)
    assert out.strip() == "15"

def test_multiple_assigns():
    src = """
    a = 10;
    b = a + 5;
    print(b);
    """
    ast = parse_code(src)
    ev = Evaluator()
    out = capture_stdout(ev.eval, ast)
    assert out.strip() == "15"

def test_undefined_var():
    src = "print(x);"
    ast = parse_code(src)
    ev = Evaluator()
    with pytest.raises(EvalError):
        ev.eval(ast)

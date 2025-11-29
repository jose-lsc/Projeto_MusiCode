class AST:
    def __init__(self, nodos=None):
        self.nodos = nodos or []

    def __repr__(self):
        return f"AST({self.nodos})"

class NodoInstrumento(AST):
    def __init__(self, instrumento):
        self.instrumento = instrumento

    def __repr__(self):
        return f"Instrumento({self.instrumento})"


class NodoNota(AST):
    def __init__(self, nota):
        self.nota = nota

    def __repr__(self):
        return f"Nota({self.nota})"


class NodoPlay(AST):
    def __repr__(self):
        return "Play()"


class NodoStop(AST):
    def __repr__(self):
        return "Stop()"

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.posicaoAtual = 0

    def peek(self):
        return self.tokens[self.posicaoAtual] if self.posicaoAtual < len(self.tokens) else None

    def advance(self):
        token = self.peek()
        if token:
            self.posicaoAtual += 1
        return token
    
    def esperado(self, tokenEsperado):
        proximoToken = self.advance()
        if proximoToken["token"] != tokenEsperado:
            raise SyntaxError(f"Erro de sintaxe, token esperado ${tokenEsperado}")
        return self.advance()

    def parse(self):
        primeiraAnalise = True
        while self.peek() is not None:
            token = self.peek()
            print(token)
            if primeiraAnalise == True:
                if token["token"] != "play{}":
                    raise SyntaxError("O código deve começar com play{ e fechar } no final")
                primeiraAnalise = False
                self.advance()
                continue
            if token["tipo_token"] == "Palavra_Chave_Instrumento":
                self.advance()
                self.esperado(";")
                continue
            if token["tipo_token"] == "Palavra_Chave_Nota":
                self.advance()
                self.esperado(";")
                continue
            if token["tipo_token"] == "Palavra_Chave_Stop":
                self.advance()
                self.esperado(";")
                continue
            if token["tipo_token"] == "Palavra_Chave_Repetir":
                self.advance()
                self.esperado(";")
                continue
            self.advance()
            

tokens = [
    {'status': True, 'token': 'play{}', 'tipo_token': 'Palavra_Chave_Play'}, 
    {'status': True, 'token': 'instrumento(violao)', 'tipo_token': 'Palavra_Chave_Instrumento'}, 
    {'status': True, 'token': ';', 'tipo_token': 'Palavra_Chave_Ponto_Virgula'}, 
    {'status': True, 'token': 'nota(A2)', 'tipo_token': 'Palavra_Chave_Nota'},
    {'status': True, 'token': ';', 'tipo_token': 'Palavra_Chave_Ponto_Virgula'}, 
    {'status': True, 'token': 'nota(A2)', 'tipo_token': 'Palavra_Chave_Nota'}, 
    {'status': True, 'token': ';', 'tipo_token': 'Palavra_Chave_Ponto_Virgula'},
    {'status': True, 'token': 'nota(B4)', 'tipo_token': 'Palavra_Chave_Nota'}, 
    {'status': True, 'token': ';', 'tipo_token': 'Palavra_Chave_Ponto_Virgula'}, 
    {'status': True, 'token': 'nota(G4)', 'tipo_token': 'Palavra_Chave_Nota'}, 
    {'status': True, 'token': ';', 'tipo_token': 'Palavra_Chave_Ponto_Virgula'}, 
    {'status': True, 'token': 'stop()', 'tipo_token': 'Palavra_Chave_Stop'}, 
    {'status': True, 'token': ';', 'tipo_token': 'Palavra_Chave_Ponto_Virgula'}
]
 
parser = Parser(tokens)
parser.parse()
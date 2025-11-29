from Compilador.lib.parser.ast.ast import (AST, NodoInstrumento, NodoNota, NodoPlay, NodoStop)


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.posicaoAtual = 0

        # Regras semânticas
        self.temInstrumento = False
        self.temNota = False
        self.stopChamado = False
        self.contadorStops = 0

        self.nodos = []

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
        self.programa()

        if not self.temInstrumento:
            raise Exception("Erro semântico: após play{} deve aparecer instrumento(...)")
        if not self.temNota:
            raise Exception("Erro semântico: precisa haver pelo menos uma nota antes do stop()")
        if self.contadorStops == 0:
            raise Exception("Erro semântico: stop() ausente — o programa deve terminar com stop()")
        if self.contadorStops > 1:
            raise Exception("Erro semântico: stop() só pode aparecer uma vez")

        ultimo_significativo = self._ultimo_token_significativo()
        if ultimo_significativo is None or ultimo_significativo.get("tipo_token") != "Palavra_Chave_Stop":
            raise Exception("Erro semântico: o último comando válido do programa deve ser stop() (ignorar ';')")

        return AST(self.nodos)
        print("Parse e análise semântica finalizados sem erros!")

    def programa(self):
        primeiro = self.peek()
        if primeiro is None or primeiro.get("token") != "play{}":
            raise SyntaxError("O código deve começar com play{}")
        self.advance()

        prox = self.peek()
        if prox is None:
            raise Exception("Erro semântico: esperado instrumento(...) após play{}")
        if prox.get("tipo_token") != "Palavra_Chave_Instrumento":
            raise Exception("Erro semântico: após play{} deve vir instrumento(...)")
        
        self.comandos()

    def comandos(self):
        tok = self.peek()
        if tok is None:
            return  
        tipo = tok["tipo_token"]

        if tipo in ("Palavra_Chave_Instrumento", "Palavra_Chave_Nota", "Palavra_Chave_Stop", "Palavra_Chave_Repetir"):
            self.comando()
            self.comandos()
        else:
            
            if tipo == "Palavra_Chave_Ponto_Virgula":
                self.advance()
                self.comandos()
            else:
                return

    def comando(self):
        tok = self.peek()
        if tok is None:
            return
        tipo  = tok.get("tipo_token")
        token = tok.get("token")
       
        if tipo == "Palavra_Chave_Instrumento":
            
            if self.temInstrumento:
                raise Exception("Erro semântico: instrumento() só pode aparecer uma vez")
            self.temInstrumento = True

            token_val = tok["token"]  # exemplo: instrumento(violao)
            self.nodos.append(NodoInstrumento(token_val))

            self.advance()            
            
            if self.peek() and self.peek().get("token") == ";":
                self.advance()
            else:
                raise Exception(f"Erro semântico: esperado ; Apos token {token} ")
            return

        if tipo == "Palavra_Chave_Nota":
            if self.stopChamado:
                raise Exception("Erro semântico: não pode ter nota depois de stop()")
            self.temNota = True

            token_val = tok["token"]  # exemplo: nota(A2)
            self.nodos.append(NodoNota(token_val))

            self.advance()
            
            if self.peek() and self.peek().get("token") == ";":
                self.advance()
            else:
                raise Exception(f"Erro semântico: esperado ; Apos token {token} ")
            return

        if tipo == "Palavra_Chave_Stop":
            self.stopChamado = True
            self.contadorStops += 1

            token_val = tok["token"]  # stop()
            self.nodos.append(NodoStop())

            self.advance()
            if self.peek() and self.peek().get("token") == ";":
                self.advance()
            else:
                raise Exception(f"Erro semântico: esperado ; Apos token {token} ")
        
            proximo = self.peek()
            while proximo is not None and proximo.get("token") == ";":
                self.advance()
                proximo = self.peek()
            if proximo is not None:
                raise Exception("Erro semântico: nada pode aparecer após stop(), exceto ';' finais")
            return

        if tipo == "Palavra_Chave_Repetir":   
            token_val = tok["token"]  # repetir(X)
            self.nodos.append(NodoRepetir(token_val))  

            self.advance()
            if self.peek() and self.peek().get("token") == ";":
                self.advance()
            return
        
        raise SyntaxError(f"Comando inválido: {tok}")
    def _ultimo_token_significativo(self):
        for t in reversed(self.tokens):
            if t.get("token") != ";":
                return t
        return None
    
# tokens = [
#     {'status': True, 'token': 'play{}', 'tipo_token': 'Palavra_Chave_Play'}, 
#     {'status': True, 'token': 'instrumento(violao)', 'tipo_token': 'Palavra_Chave_Instrumento'}, 
#     {'status': True, 'token': ';', 'tipo_token': 'Palavra_Chave_Ponto_Virgula'}, 
#     {'status': True, 'token': 'nota(A2)', 'tipo_token': 'Palavra_Chave_Nota'},
#     {'status': True, 'token': ';', 'tipo_token': 'Palavra_Chave_Ponto_Virgula'}, 
#     {'status': True, 'token': 'nota(A2)', 'tipo_token': 'Palavra_Chave_Nota'}, 
#     {'status': True, 'token': ';', 'tipo_token': 'Palavra_Chave_Ponto_Virgula'},
#     {'status': True, 'token': 'nota(B4)', 'tipo_token': 'Palavra_Chave_Nota'}, 
#     {'status': True, 'token': ';', 'tipo_token': 'Palavra_Chave_Ponto_Virgula'}, 
#     {'status': True, 'token': 'nota(G4)', 'tipo_token': 'Palavra_Chave_Nota'}, 
#     {'status': True, 'token': ';', 'tipo_token': 'Palavra_Chave_Ponto_Virgula'}, 
#     {'status': True, 'token': 'stop()', 'tipo_token': 'Palavra_Chave_Stop'}, 
#     {'status': True, 'token': ';', 'tipo_token': 'Palavra_Chave_Ponto_Virgula'},
# ]
 
# parser = Parser(tokens)
# parser.parse()
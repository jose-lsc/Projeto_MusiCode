

class estado_base:
    
    def __init__(self, identificador, tipo_token, estado_final = False):
        self.identificador  = identificador #Nome do estado, ex : q0.1
        self.estado_final   = estado_final #booleano mostrando de aquele estado é o final de um afd
        self.tipo_token     = tipo_token
        self.transicoes     = {}    #recebe um dicionario no formato {simbolo : proximo estado}

    def adicionar_transicao(self, simbolo, proximo_estado):
        self.transicoes[simbolo] = proximo_estado

    def __repr__(self):
        return f"<Estado {self.identificador}, final={self.estado_final}, token={self.tipo_token}>"

    
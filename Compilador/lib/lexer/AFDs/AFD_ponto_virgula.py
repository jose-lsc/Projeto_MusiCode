class AFD:
    def __init__(self, estados, estado_inicial, estados_finais, transicoes):
        self.estados = estados
        self.estados = estados
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais
        self.transicoes = transicoes

    def processar(self, entrada):
        estado_atual = self.estado_inicial
        for simbolo in entrada:
            if simbolo != ';' and estado_atual == "q0":
                continue
            if simbolo not in self.transicoes.get(estado_atual, {}) and estado_atual == "q1":
                return False 
            estado_atual = self.transicoes[estado_atual][simbolo]
        return estado_atual in self.estados_finais
        
estados = {'q0', 'q1'}
estado_inicial = 'q0'
estados_finais = {'q1'}  
transicoes = {
    'q0': {';': 'q1'},
    'q1': {},  
}

afd = AFD(estados, estado_inicial, estados_finais, transicoes)

# Testes Unitarios
entrada_1 = '";"'
entrada_2 = ';'
entrada_3 = "abcd;"
entrada_4 = '"er;ro' 
entrada_5 = 'isso  ;;   não é uma string'  

print(f"Entrada: {entrada_1} -> Aceito? {afd.processar(entrada_1)}")  
print(f"Entrada: {entrada_2} -> Aceito? {afd.processar(entrada_2)}")  
print(f"Entrada: {entrada_3} -> Aceito? {afd.processar(entrada_3)}")  
print(f"Entrada: {entrada_4} -> Aceito? {afd.processar(entrada_4)}")
print(f"Entrada: {entrada_5} -> Aceito? {afd.processar(entrada_5)}")



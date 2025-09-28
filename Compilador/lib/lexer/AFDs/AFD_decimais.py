class AFD:
    def __init__(self):
        self.estados = {'q0', 'q1', 'q2', 'q3'}
        self.estado_inicial = 'q0'
        self.estados_finais =  {'q3'}
        digitos = [str(d) for d in range(10)]
        self.transicoes = {
            'q0': {d: 'q1' for d in digitos},     
            'q1': {d: 'q1' for d in digitos},     
        }
        self.transicoes['q1']['.'] = 'q2'
        self.transicoes["q2"] = {d: 'q3' for d in digitos}
        self.transicoes["q3"] = {d: 'q3' for d in digitos}

    def processar(self, entrada: str) -> bool:
        estado_atual = self.estado_inicial
        for simbolo in entrada:
            
            if simbolo not in self.transicoes.get(estado_atual, {}):
                return False
            estado_atual = self.transicoes[estado_atual][simbolo]
        return estado_atual in self.estados_finais

estados = {'q0', 'q1', 'q2', 'q3'}
estado_inicial = 'q0'
estados_finais = {'q3'}

digitos = [str(d) for d in range(10)]
transicoes = {
    'q0': {d: 'q1' for d in digitos},     
    'q1': {d: 'q1' for d in digitos},     
}
transicoes['q1']['.'] = 'q2'
transicoes["q2"] = {d: 'q3' for d in digitos}
transicoes["q3"] = {d: 'q3' for d in digitos}

afd = AFD()

if __name__ == "__main__":
    # Testes Unitarios
    entradas = ["", "12345", "abc", '"erro', "0.56", "00.7", "12.a", "12.3"]
    for ent in entradas:
        print(f"{ent!r}: {afd.processar(ent)}")
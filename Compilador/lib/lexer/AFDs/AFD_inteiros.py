class AFD:
    def __init__(self):
        self.estados = {'q0', 'q1'}
        self.estado_inicial = 'q0'
        self.estados_finais = {'q1'}
        digitos = [str(d) for d in range(10)]
        self.transicoes = {
            'q0': {d: 'q1' for d in digitos},      
            'q1': {d: 'q1' for d in digitos},      
        }

    def processar(self, entrada: str) -> bool:
        estado_atual = self.estado_inicial
        for simbolo in entrada:
            
            if simbolo not in self.transicoes.get(estado_atual, {}):
                return False
            estado_atual = self.transicoes[estado_atual][simbolo]
        return estado_atual in self.estados_finais



estados = {'q0', 'q1'}
estado_inicial = 'q0'
estados_finais = {'q1'}


digitos = [str(d) for d in range(10)]
transicoes = {
    'q0': {d: 'q1' for d in digitos},      
    'q1': {d: 'q1' for d in digitos},      
}

afd = AFD()

if __name__ == "__main__":
    # Testes Unitarios
    entradas = ["", "12345", "abc", '"erro', "0", "007", "12a", "12.3"]
    for ent in entradas:
        print(f"{ent!r}: {afd.processar(ent)}")
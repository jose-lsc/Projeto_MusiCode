class AFD:
    def __init__(self):
        self.estados = {'q0', 'q1', 'q2'}
        self.estado_inicial = 'q0'
        self.estados_finais = {'q1', 'q2'}
        self.transicoes = {
            'q0': {'$': 'q1'},         
            'q1': {c: 'q1' for c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789$"},  
        }

    def processar(self, entrada) -> bool:
        
        if isinstance(entrada, int):
            entrada = str(entrada)

        estado_atual = self.estado_inicial
        for simbolo in entrada:
            
            if simbolo not in self.transicoes.get(estado_atual, {}):
                return False
            estado_atual = self.transicoes[estado_atual][simbolo]
        
        return estado_atual in self.estados_finais

estados = {'q0', 'q1', 'q2'}
estado_inicial = 'q0'
estados_finais = {'q1', 'q2'}

transicoes = {
    'q0': {'$': 'q1'},         
    'q1': {c: 'q1' for c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789$"},  
}

afd = AFD()

if __name__ == "__main__":
    # Testes Unitarios
    entradas = ["$var", "$_1", "$abc123", "$1234", "$$123", "$var$123", "var", "$var!", "$"]
    for ent in entradas:
        print(f"{ent!r}: {afd.processar(ent)}")
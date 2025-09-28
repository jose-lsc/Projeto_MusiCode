class AFD:
    def __init__(self):
        self.estados = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6'}
        self.estado_inicial = 'q0'
        self.estados_finais = {'q6'}
        self.transicoes = {
            'q0': {'s': 'q1'},         
            'q1': {'t': 'q2'},         
            'q2': {'o': 'q3'},         
            'q3': {'p': 'q4'},         
            'q4': {'(': 'q5'},
            "q5" :{")" : "q6"}
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

estados = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6'}
estado_inicial = 'q0'
estados_finais = {'q6'}

# Transições
transicoes = {
    'q0': {'s': 'q1'},         
    'q1': {'t': 'q2'},         
    'q2': {'o': 'q3'},         
    'q3': {'p': 'q4'},         
    'q4': {'(': 'q5'},
    "q5" :{")" : "q6"}
}

if __name__ == "__main__":
    afd = AFD()

    # Testes Unitarios
    entradas = [
        "stop",               
        "stop()",            
        "stop(A)",              
        "stop(123?A)",          
        "stop(--R)",              
        "not123",             
        "stop@123",           
        "stopG999#?a",        
    ]

    for ent in entradas:
        print(f"{ent!r}: {afd.processar(ent)}")
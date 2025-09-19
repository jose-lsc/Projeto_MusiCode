class AFD:
    def __init__(self, estados, estado_inicial, estados_finais, transicoes):
        self.estados = estados
        self.estado_inicial = estado_inicial
        self.estados_finais = estados_finais
        self.transicoes = transicoes

    def processar(self, entrada) -> bool:
        
        if isinstance(entrada, int):
            entrada = str(entrada)

        estado_atual = self.estado_inicial
        for simbolo in entrada:
            if simbolo != '}' and estado_atual == "q5":
                continue
            if simbolo not in self.transicoes.get(estado_atual, {}) and estado_atual != "q5":
                return False
            estado_atual = self.transicoes[estado_atual][simbolo]
        
        return estado_atual in self.estados_finais

estados = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6'}
estado_inicial = 'q0'
estados_finais = {'q6'}

# Transições
transicoes = {
    'q0': {'p': 'q1'},         
    'q1': {'l': 'q2'},         
    'q2': {'a': 'q3'},         
    'q3': {'y': 'q4'},  
    'q4': {'{': 'q5'}, 
    'q5': {'}': 'q6'}, 
    'q6': {}
}

afd = AFD(estados, estado_inicial, estados_finais, transicoes)

# Testes Unitarios
entradas = [
    "play{}",               
    "instrumento(vi ola o)",            
    "",              
    ")",          
    "play{pode qualquer coisa aqui dentro}",         
    "play{dasda}}",           
    '"play{}"',        
]

for ent in entradas:
    print(f"{ent!r}: {afd.processar(ent)}")

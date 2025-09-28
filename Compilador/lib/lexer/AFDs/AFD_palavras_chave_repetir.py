class AFD:
    def __init__(self):
        self.estados = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6','q7', 'q8', 'q9'}
        self.estado_inicial = 'q0'
        self.estados_finais = {'q9'}
        self.transicoes = {
            'q0': {'r': 'q1'},         
            'q1': {'e': 'q2'},         
            'q2': {'p': 'q3'},         
            'q3': {'e': 'q4'},  
            'q4': {'t': 'q5'}, 
            'q5': {'i': 'q6'}, 
            'q6': {'r': 'q7'},
            'q7': {'(': 'q8'},
            'q8': {')': 'q9'},
        }

    def processar(self, entrada) -> bool:
        
        if isinstance(entrada, int):
            entrada = str(entrada)

        estado_atual = self.estado_inicial
        for simbolo in entrada:
            if simbolo != ')' and estado_atual == "q8":
                continue
            if simbolo not in self.transicoes.get(estado_atual, {}) and estado_atual != "q5":
                return False
            estado_atual = self.transicoes[estado_atual][simbolo]
        
        return estado_atual in self.estados_finais

estados = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6','q7', 'q8', 'q9'}
estado_inicial = 'q0'
estados_finais = {'q9'}

# Transições
transicoes = {
    'q0': {'r': 'q1'},         
    'q1': {'e': 'q2'},         
    'q2': {'p': 'q3'},         
    'q3': {'e': 'q4'},  
    'q4': {'t': 'q5'}, 
    'q5': {'i': 'q6'}, 
    'q6': {'r': 'q7'},
    'q7': {'(': 'q8'},
    'q8': {')': 'q9'},
}

afd = AFD()

# Testes Unitarios
entradas = [
    "repetir{}",               
    "instrumento(vi ola o)",            
    "",              
    ")",          
    "repetir{pode qualquer coisa aqui dentro}",         
    "repetir{dasda}}",           
    '"repetir{}"',        
]

if __name__ == "__main__":
    for ent in entradas:
        print(f"{ent!r}: {afd.processar(ent)}")
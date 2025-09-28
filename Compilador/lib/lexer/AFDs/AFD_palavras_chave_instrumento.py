class AFD:
    def __init__(self):
        self.estados = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15'
           'q16', 'q17', 'q18', 'q19'}
        self.estado_inicial = 'q0'
        self.estados_finais = {'q19'}
        self.transicoes =  {
            'q0': {'i': 'q1'},         
            'q1': {'n': 'q2'},         
            'q2': {'s': 'q3'},         
            'q3': {'t': 'q4'},  
            'q4': {'r': 'q5'}, 
            'q5': {'u': 'q6'}, 
            'q6': {'m': 'q7'}, 
            'q7': {'e': 'q8'}, 
            'q8': {'n': 'q9'}, 
            'q9': {'t': 'q10'}, 
            'q10': {'o': 'q11'},        
            'q11': {'(': 'q12'},
            'q12': {'v': 'q13'},
            'q13': {'i': 'q14'},
            'q14': {'o': 'q15'},
            'q15': {'l': 'q16'},
            'q16': {'a': 'q17'},
            'q17': {'o': 'q18'},
            'q18': {')': 'q19'},
            'q19': {'': 'q19'}
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

estados = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15'
           'q16', 'q17', 'q18', 'q19'}
estado_inicial = 'q0'
estados_finais = {'q19'}

# Transições
transicoes = {
    'q0': {'i': 'q1'},         
    'q1': {'n': 'q2'},         
    'q2': {'s': 'q3'},         
    'q3': {'t': 'q4'},  
    'q4': {'r': 'q5'}, 
    'q5': {'u': 'q6'}, 
    'q6': {'m': 'q7'}, 
    'q7': {'e': 'q8'}, 
    'q8': {'n': 'q9'}, 
    'q9': {'t': 'q10'}, 
    'q10': {'o': 'q11'},        
    'q11': {'(': 'q12'},
    'q12': {'v': 'q13'},
    'q13': {'i': 'q14'},
    'q14': {'o': 'q15'},
    'q15': {'l': 'q16'},
    'q16': {'a': 'q17'},
    'q17': {'o': 'q18'},
    'q18': {')': 'q19'},
    'q19': {'': 'q19'}
}

afd = AFD()

# Testes Unitarios
entradas = [
    "instrumento(violao)",               
    "instrumento(vi ola o)",            
    "",              
    ")",          
    "instrumento(viao)",              
    "instrumento()",             
    "instrto(violao)",           
    "notaG999#?a",        
]

if __name__ == "__main__":
    for ent in entradas:
        print(f"{ent!r}: {afd.processar(ent)}")
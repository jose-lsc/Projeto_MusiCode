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
            
            if simbolo not in self.transicoes.get(estado_atual, {}):
                return False
            estado_atual = self.transicoes[estado_atual][simbolo]
        
        return estado_atual in self.estados_finais

estados = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7'}
estado_inicial = 'q0'
estados_finais = {'q7'}

# Transições
transicoes = {
    'q0': {'n': 'q1'},         # Inicia com 'n' para "nota"
    'q1': {'o': 'q2'},         # Depois 'o' para "nota"
    'q2': {'t': 'q3'},         # Depois 't' para "nota"
    'q3': {'a': 'q4'},         # Depois 'a' para "nota"
    'q4': {'(': 'q5'},
    'q5': {                     # Depois de "nota", aceita os caracteres válidos
        'a': 'q6', 'b': 'q6', 'c': 'q6', 'd': 'q6', 'e': 'q6', 'f': 'q6', 'g': 'q6',  
        'A': 'q6', 'B': 'q6', 'C': 'q6', 'D': 'q6', 'E': 'q6', 'F': 'q6', 'G': 'q6',
    },
    'q6': {                     # Permite continuar aceitando os mesmos caracteres
        '0': 'q6', '1': 'q6', '2': 'q6', '3': 'q6', '4': 'q6', '5': 'q6', '6': 'q6', '7': 'q6', '8': 'q6', '9': 'q6', '#' : 'q6', ')' : "q7"
    },
    "q7" : {" " : "q7"}
}

afd = AFD(estados, estado_inicial, estados_finais, transicoes)

# Testes Unitarios
entradas = [
    "nota",               
    "nota(123)",            
    "nota(A)",              
    "nota(123?A)",          
    "nota(aR)",              
    "not123",             
    "nota@123",           
    "notaG999#?a",        
]

for ent in entradas:
    print(f"{ent!r}: {afd.processar(ent)}")

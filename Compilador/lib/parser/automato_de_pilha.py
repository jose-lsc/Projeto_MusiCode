# Transições funcionam:
#   δ(q,a,X)=(p,γ)

# Símbolo	Significado
# q	estado atual
# a	símbolo de entrada lido (ou ε se não ler nada)
# X	topo atual da pilha
# p	próximo estado
# γ	sequência de símbolos que substitui X no topo da pilha (pode empilhar vários ou nenhum)




class AutomatoPilha:
    def __init__(self):
        #Estados
        self.Q = {"q0", "q1", "qf"}
        self.q0 = "q0"
        self.estadoFinal = "qf"
        self.Z0 = "Z0" #fundo da pilha
        self.pilha = [self.Z0]

        #transicoes
        self.transicoes = {
            #inicio
            ('q0', '', 'Z0'): ('q1', ['Program', 'Z0']),

            #leitura do primeiro token play{}, como é uma pilha, temos que colocar "Invertido" pois o ultimo que entra é o primeiro que sai
            ('q1', '', "Program") : ('q1', ['}', "statement", "{", "play"]),

            # transicoes terminais, afinal o codigo começa com play{ e termina com }
            ('q1', 'play', 'play'): ('q1', []),
            ('q1', '{', '{'): ('q1', []),
            ('q1', '}', '}'): ('q1', []),

            #leitura dos possíveis tokens em statement
            ('q1', '', 'Statement'): ('q1', ['InstrumentoStmt']),
            ('q1', '', 'InstrumentoStmt') : ('q1', [';', ')', "violao", "(", "instrumento"]),


            ('q1', '', 'Statement'): ('q1', ['NumericStmt']),
            ('q1', '', 'Statement'): ('q1', ['IdentificadoresStmt']),
            ('q1', '', 'Statement'): ('q1', ['repetirStmt']),
            ('q1', '', 'Statement'): ('q1', ['stopStmt']),
            ('q1', '', 'Statement'): ('q1', ['notaStmt']),
            ('q1', '', 'Statement'): ('q1', ['stringStmt']),
            ('q1', '', 'Statement'): ('q1', ['ponto_virgulaStmt'])

        }
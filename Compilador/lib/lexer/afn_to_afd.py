# Posições de cada AFD
# String - 1
# decimal - 2
# Identificador - 3
# Inteiro - 4
# Palavra_Chave_Instrumento - 5
# Palavra_Chave_Nota - 6
# Palavra_Chave_Play - 7
# Palavra_Chave_Repetir - 8
# Palavra_Chave_Stop - 9
# Palavra_Chave_Ponto_Virgula - 10

from estado_base import estado_base

class AFD:
    def __init__(self):
        #dicionario que guarda as relações das posições com o tipo de token
        tipo_por_sufixo = {
            "1": "String",
            "2": "Decimal",
            "3": "Identificador",
            "4": "Inteiro",
            "5": "Palavra_Chave_Instrumento",
            "6": "Palavra_Chave_Nota",
            "7": "Palavra_Chave_Play",
            "8": "Palavra_Chave_Repetir",
            "9": "Palavra_Chave_Stop",
            "10": "Palavra_Chave_Ponto_Virgula"
        }
        
        #declaração antiga de estados
        estadosNomes = {
            "q0.1", "q0.2", "q0.3", "q0.4", "q0.5", "q0.6", "q0.7", "q0.8", "q0.9", "q0.10",
            "q1.1", "q1.2", "q1.3", "q1.4", "q1.5", "q1.6", "q1.7", "q1.8", "q1.9", "q1.10",
            "q2.1", "q2.2", "q2.3",         "q2.5", "q2.6", "q2.7", "q2.8", "q2.9", 
                    "q3.2"                  "q3.5", "q3.6", "q3.7", "q3.8", "q3.9", 
                                            "q4.5", "q4.6", "q4.7", "q4.8", "q4.9", 
                                            'q5.5', "q5.6", "q5.7", "q5.8", "q5.9", 
                                            'q6.5', "q6.6", "q6.7", "q6.8", "q6.9", 
                                            'q7.5', "q7.6",         "q7.8",
                                            'q8.5', "q8.6",         "q8.8",
                                            'q9.5', "q9.6",         "q9.8",
                                            'q10.5',
                                            'q11.5',
                                            'q12.5',
                                            'q13.5',
                                            'q14.5',
                                            'q15.5',
                                            'q16.5',
                                            'q17.5',
                                            'q18.5',
                                            'q19.5'
        }
        
        #declaração dos estados finais de cada afd
        self.estados_finais = { "q2.1", "q3.2", "q2.3", "q1.4", "q19.5", "q9.6", "q6.7", "q9.8", "q6.9","q1.10"}
        
        #Nova declaração de estado usando agora as classes para representa-los.
        #Usarei o for para economizar linhas
        self.estados = {}

        for nome in estadosNomes:
            is_final        = nome in self.estados_finais
            posicaoEstado   = nome.split(".")[-1]
            tipo_token      = tipo_por_sufixo[posicaoEstado]
            self.estados[nome] = estado_base(
                nome,
                tipo_token,
                is_final
            )

        self.estados_iniciais = { "q0.1", "q0.2", "q0.3", "q0.4", "q0.5", "q0.6", "q0.7", "q0.8", "q0.9", "q0.10"}

        digitos = [str(d) for d in range(10)]
        self.transicoes =  {
            #transições do string
            'q0.1': {'"': 'q1.1'}, 'q1.1': {'"': 'q2.1'}|{c: 'q1.1' for c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789$#-_{ }()" }, 'q2.1': {},
            
            #transições do decimal
            'q0.2': {d: 'q1.2' for d in digitos},'q1.2': { ".", "q2.2"}, "q2.2" : {d: 'q3.2' for d in digitos} ,    

            #transições do identificador
            'q0.3': {'$': 'q1.3'}, 'q1.3': {c: 'q2.3' for c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789$#-_(){ }"},

            #transicoes do inteiro
            'q0.4': {d: 'q1.4' for d in digitos}, 'q1.4': {d: 'q1.4' for d in digitos},

            #transicoes da palavra_chave_instrumento
            'q0.5': {'i': 'q1.5'},         
            'q1.5': {'n': 'q2.5'},         
            'q2.5': {'s': 'q3.5'},         
            'q3.5': {'t': 'q4.5'},  
            'q4.5': {'r': 'q5.5'}, 
            'q5.5': {'u': 'q6.5'}, 
            'q6.5': {'m': 'q7.5'}, 
            'q7.5': {'e': 'q8.5'}, 
            'q8.5': {'n': 'q9.5'}, 
            'q9.5': {'t': 'q10.5'}, 
            'q10.5': {'o': 'q11.5'},        
            'q11.5': {'(': 'q12.5'},
            'q12.5': {'v': 'q13.5'},
            'q13.5': {'i': 'q14.5'},
            'q14.5': {'o': 'q15.5'},
            'q15.5': {'l': 'q16.5'},
            'q16.5': {'a': 'q17.5'},
            'q17.5': {'o': 'q18.5'},
            'q18.5': {')': 'q19.5'},
            'q19.5': {'': 'q19.5'},


            #transicoes da palavra_chave_nota
            'q0.6': {'n': 'q1.6'},
            'q1.6': {'o': 'q2.6'},
            'q2.6': {'t': 'q3.6'},
            'q3.6': {'a': 'q4.6'},
            'q4.6': {'(': 'q5.6'},
            'q5.6': {                     
                'a': 'q6.6', 'b': 'q6.6', 'c': 'q6.6', 'd': 'q6.6', 'e': 'q6.6', 'f': 'q6.6', 'g': 'q6.6',  
                'A': 'q6.6', 'B': 'q6.6', 'C': 'q6.6', 'D': 'q6.6', 'E': 'q6.6', 'F': 'q6.6', 'G': 'q6.6',
            },
            'q6.6': {               
                '0': 'q7.6', '1': 'q7.6', '2': 'q7.6', '3': 'q7.6', '4': 'q7.6', '5': 'q7.6', '6': 'q7.6', '7': 'q7.6', '8': 'q7.6', '9': 'q7.6', 
            },
            "q7.6" : {'#' : 'q8.6', ')' : "q9.6"},
            "q8.6" : {')' : "q9.6"},
            "q9.6" : {" " : "q9.6"},


            #transicoes da palavra_chave_play
            'q0.7': {'p': 'q1.7'},         
            'q1.7': {'l': 'q2.7'},         
            'q2.7': {'a': 'q3.7'},         
            'q3.7': {'y': 'q4.7'},  
            'q4.7': {'{': 'q5.7'}, 
            'q5.7': {'}': 'q6.7'} | {c: 'q5.7' for c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789$#_-;()"}, 
            'q6.7': {},


            #transicoes da palavra_chave_repetir
            'q0.8': {'r': 'q1.8'},         
            'q1.8': {'e': 'q2.8'},         
            'q2.8': {'p': 'q3.8'},         
            'q3.8': {'e': 'q4.8'},  
            'q4.8': {'t': 'q5.8'}, 
            'q5.8': {'i': 'q6.8'}, 
            'q6.8': {'r': 'q7.8'},
            'q7.8': {'(': 'q8.8'},
            'q8.8': {')': 'q9.8'},

            #transicoes da palavra_chave_stop
            'q0.9': {'s': 'q1.9'},         
            'q1.9': {'t': 'q2.9'},         
            'q2.9': {'o': 'q3.9'},         
            'q3.9': {'p': 'q4.9'},         
            'q4.9': {'(': 'q5.9'},
            "q5.9" :{")" : "q6.9"},

            #transicoes do token ponto_virgula
            'q0.10': {';': 'q1.10'},
            'q1.10': {},

        }

    def processar(self, entrada):
        estados_atuais = self.estados_iniciais
        
        for simbolo in entrada:
            novos_estados = set()

            for estado_atual in estados_atuais:
                if simbolo in self.transicoes.get(estado_atual, {}):
                    novos_estados.add(self.transicoes[estado_atual][simbolo])
                #print(simbolo, estado_atual, novos_estados)
            if not novos_estados:
                
                return {
                        "status": False,
                        "token" : entrada,
                        "tipo_token": None
                    }
            estados_atuais = novos_estados
        for estado in estados_atuais:
             if estado in self.estados:  # Verifica se temos um objeto estado_base
                estado_obj = self.estados[estado]
                return {
                    "status": estado_obj.estado_final,
                    "token" : entrada,
                    "tipo_token": estado_obj.tipo_token
                }

afd = AFD()

# Testes Unitarios
entrada_1 = 'play{' \
'nota(A2)}'
entrada_2 = 'instrumento(violao)'
entrada_3 = 'stop()'
entrada_4 = 'stop(9)' 
entrada_5 = 'isso  ;;   não é uma string'  
if __name__ == "__main__":
    print(f"Entrada: {entrada_1} -> Aceito? {afd.processar(entrada_1)}")  
    print(f"Entrada: {entrada_2} -> Aceito? {afd.processar(entrada_2)}")  
    print(f"Entrada: {entrada_3} -> Aceito? {afd.processar(entrada_3)}")  
    print(f"Entrada: {entrada_4} -> Aceito? {afd.processar(entrada_4)}")
    print(f"Entrada: {entrada_5} -> Aceito? {afd.processar('instrumento();')}")
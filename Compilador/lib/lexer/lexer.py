from AFDs.AFD_Strings import AFD as AFD_string   
from AFDs.AFD_decimais import AFD as AFD_decimal     
from AFDs.AFD_inteiros import AFD as AFD_inteiro   
from AFDs.AFD_identificador import AFD as AFD_identificador     
from AFDs.AFD_palavras_chave_instrumento import AFD as                   AFD_palavraChaveInstrumento                                                   
from AFDs.AFD_palavras_chave_nota  import AFD as AFD_palavraChaveNota
from AFDs.AFD_palavras_chave_play import AFD as AFD_palavraChavePlay 
from AFDs.AFD_palavras_chave_repetir import AFD as AFD_palavraChaveRepetir
from AFDs.AFD_palavras_chave_stop import AFD as AFD_palavraChaveStop
from AFDs.AFD_ponto_virgula import AFD as AFD_pontoVirgula 

class Lexer:
    def __init__(self):

        self.afdString = AFD_string()
        self.afdDecimal = AFD_decimal()
        self.afdInteiro = AFD_inteiro()
        self.afdIdentificador = AFD_identificador()
        self.afdInstrumento = AFD_palavraChaveInstrumento()
        self.afdRepetir = AFD_palavraChaveRepetir()
        self.afdPontoVirgula = AFD_pontoVirgula()
        self.afdPlay = AFD_palavraChavePlay()
        self.afdStop = AFD_palavraChaveStop()
        self.afdNota = AFD_palavraChaveNota()
        



    def testarAfds(self, token, linha, coluna):
         
        if self.afdPlay.processar(token):
            return [{token: "Palavras-chave"}]
        elif self.afdStop.processar(token):
            return [{token: "Palavras-chave"}]
        elif self.afdNota.processar(token):
            return [{token: "Palavras-chave"}]
        elif self.afdString.processar(token):
            return [{token: "String"}]
        elif self.afdDecimal.processar(token):
            return [{token: "Decimal"}]
        elif self.afdInteiro.processar(token):
            return [{token: "Inteiro"}]
        elif self.afdIdentificador.processar(token):
            return [{token: "Identificador"}]
        elif self.afdInstrumento.processar(token):
            return [{token: "Palavras-chave"}]
        elif self.afdRepetir.processar(token):
            return [{token: "Palavras-chave"}]
        elif self.afdPontoVirgula.processar(token):
            return [{token: "Palavras-chave"}]
        else:
            return [{token: f"erro, linha:{str(linha)}, coluna:{str(coluna)}"}]
    def lexer(self, input_text):
        resultado = []
        tokenPlay = "" 
        tokensInternos = "" #variavel que vai guardar todos os tokens dentro do bloc play{}
        token = "" #variavel que sera usada para ler os tokens um a um dentro do play{}
        codigoGeral = [] #teste para ver se o token play existe e funciona 
        linha = 1
        coluna = 1

        for i in input_text:
            
            if i == ' ':
                tokensInternos += i
                continue
            if tokenPlay == "play{" and i != "}":
                #Eu fiz a divisão aqui pois o play é um bloco logico onde acontecera o codigo
                tokensInternos += i
            else:
                tokenPlay += i  
            codigoGeral.append(i)

        codigoGeral = ''.join(codigoGeral)
        
        result = self.afdPlay.processar(codigoGeral)
        
        if result == False:
            resultado.append({
                "token Play errado": "linha: "+ str(linha)
            })
        else:
            resultado.append({
                tokenPlay : "correto"
            })
        
        #Após verificarmos a existencia do token play{} ai sim podemos ver os outros
        print("\n\nTOKENS INTERNOS"+tokensInternos)
        inicioString = False
        for i in tokensInternos:
            if i == '"' or inicioString == True:
                if inicioString == True and i == '"':
                    token += i
                    resultado.append(self.testarAfds(token, linha, coluna))
                    token = ""
                    inicioString = False
                    continue
                inicioString = True
                token += i
                continue
            elif i == ' ':
                if len(token) > 0:
                    resultado.append(self.testarAfds(token, linha, coluna))
                    token = ""  
                continue  
            elif i == '\n':
                linha += 1  
                coluna = 1  
            else:
                token += i  
                coluna += 1 

        return resultado
        
#alguma variaveis para testes
variavelDeTeste = (
    'play{ testando stop(3) 12 32.1 tokens nota(A1) "testando string" foi foi ?? \n'
    'yagu repetir()  $identificador  instrumento(); instrumento(violao) }'
)
variavelDeTeste2 = (
    'play{ das instrumento(violao) nota(A1) nota(G3) nota(F) nota(A1) stop() ;}'
)

lexer = Lexer()
resultado = lexer.lexer(variavelDeTeste2)
print(resultado)
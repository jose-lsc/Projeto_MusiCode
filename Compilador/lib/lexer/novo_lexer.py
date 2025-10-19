from afn_to_afd import AFD

class Lexer:
    def __init__(self):
        self.afd = AFD()
    
    def classificar_token(self, token):

        return self.afd.processar(token)

    def lexer(self, input_text):
        resultado = []
        linha = 1
        coluna = 1
        token = ""
        tokensInternos = ""
        dentro_play = False
        brace_count = 0  # Conta { e } para delimitar bloco play

        i = 0
        while i < len(input_text):
            c = input_text[i]

            if c == '\n':
                linha += 1
                coluna = 1
                i += 1
                continue

            if dentro_play:
                
                if c == ";":
                    #ja que houve ponto e virgula para finalizar a logica ele busca o token que foi formado ate então
                    retornoAFD = self.classificar_token(tokensInternos)
                    if retornoAFD["status"] == False:
                        return {
                            "Erro": f"Token {tokensInternos} Invalido!!!",
                            "linha" : linha,
                            "coluna" : coluna - 1,
                            "token": tokensInternos, 
                        }
                    else:
                        resultado.append(retornoAFD)
                    resultado.append(self.classificar_token(";"))
                    i += 1
                    coluna += 1
                    continue

                if c.isspace():
                    if tokensInternos.strip() != "":
                        retornoAFD = self.classificar_token(tokensInternos)
                        if retornoAFD["status"] == False:
                            return {
                                "Erro": f"Token {tokensInternos} Invalido!!!",
                                "linha" : linha,
                                "coluna" : coluna,
                                "token": tokensInternos, 
                            }
                        else:
                            resultado.append(retornoAFD)
                        tokensInternos = ""
                    i += 1
                    coluna += 1
                    continue


                # Ler até fechar o bloco do play {...}
                if c == '{':

                    #verificar se outro token com chave pode aparecer dentro, se for o caso ele adiciona a logica de fechamento
                    brace_count += 1
                    tokensInternos += c
                elif c == '}':

                    #se tiver uma chave fechando '}' ele tira um na lógica de verificação do token play{}, se for 0 ele sabe que foi o token play{} que fechou, se for > 0, então se tratava de outro token com chaves '{}'
                    brace_count -= 1
                    tokensInternos += c
                    if brace_count == 0:
                        # Fechou bloco play
                        # Remove a palavra 'play' do início do token
                        #conteudo_play = token[len("play{"):-1].strip()

                        resultado.append({"token": "play{}", "tipo": "Palavra_Chave_Play"})

                        # # Agora tokenizar o conteúdo dentro do play
                        # # Aqui vamos dividir por espaços e símbolos simples
                        # sub_tokens = self.split_tokens(conteudo_play)
                        
                        # for t in sub_tokens:
                        #     retornoAFD = self.classificar_token(t)
                        #     if retornoAFD["status"] == False:
                        #         resultado.append({
                        #             "Erro": "O código sempre deve começar e finalizar com o bloco play{}\n",
                        #             "linha" : linha,
                        #             "coluna" : coluna,
                        #             "token": token, 
                        #         })
                        #     resultado.append(retornoAFD)
                        tokensInternos = ""
                        dentro_play = False
                    # else ainda dentro do bloco, continua
                else:
                    tokensInternos += c

                i += 1
                coluna += 1
                #tokensInternos += c
                continue

            else:
                # Fora do bloco play
                #aqui ele verifica se os proximos 5 letras do token se refere ao play{, pois todo o codigo do musicode deve começar com o bloco play{}
                if input_text[i:i+5] == "play{":
                    dentro_play = True
                    brace_count = 1
                    token = "play{"
                    i += 5
                    coluna += 5
                    continue

                return {
                    "Erro": "O código sempre deve começar e finalizar com o bloco play{}\n",
                    "linha" : linha,
                    "coluna" : coluna,
                    "token": token, 
                    }

        # Depois do loop, verifica token pendente
        if token:
            resultado.append(self.classificar_token(token))

        return resultado

    def split_tokens(self, text):
        # Dividir texto em tokens simples por espaços e símbolos
        import re
        # Aqui separa por espaços e por símbolos especiais
        tokens = re.findall(r'\w+\(.*?\)|".*?"|\w+|[();{}]', text)
        # Explicação da regex:
        # \w+\(.*?\) -> palavras com parênteses, tipo nota(A1)
        # ".*?" -> strings entre aspas
        # \w+ -> palavras simples
        # [();{}] -> símbolos
        return tokens

lexer = Lexer()

codigo_teste = """
play{
    instrumento(violao);
    nota(A2);
    nota(B4);
    stop();

    "nota()"
}
"""

retorno = lexer.lexer(codigo_teste)

print(retorno)

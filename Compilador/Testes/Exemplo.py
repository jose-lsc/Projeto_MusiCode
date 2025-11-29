def main():
    from Compilador.lib.lexer.novo_lexer import Lexer
    from Compilador.lib.parser.parser import Parser
    from Compilador.lib.parser.gerador_LLVM_IR import GeradorLLVM

    #Aqui é um exemplo de como você deve implementar o compilador
    #exemplo para compilar o codigo 
    # pathDoMeuPc\Projeto_MusiCode> python -m Compilador.Testes.Exemplo
    codigo = """
    play{
        instrumento(violao);
        nota(A2);
        nota(B4);
        nota(A2);
        nota(B4);
        nota(A2);
        nota(B4);
        stop();
    }
    """
    print("=== LEXER ===")
    lexer = Lexer()
    retorno = lexer.lexer(codigo)
    print(retorno)

    print("\n=== PARSER ===")
    parser = Parser(retorno)
    retornoParse = parser.parse()
    print(retornoParse)

    print("\n=== LLVM ===")
    llvm = GeradorLLVM().gerar(retornoParse)
    print(llvm)

if __name__ == "__main__":
    main()


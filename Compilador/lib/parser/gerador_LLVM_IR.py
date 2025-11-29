class GeradorLLVM:
    def gerar(self, ast):
        llvm = []
        llvm.append("; Código gerado pelo MusiCode")
        llvm.append("declare void @tocarInstrumento(i8*)")
        llvm.append("declare void @tocarNota(i8*)")
        llvm.append("declare void @parar()")

        llvm.append("\ndefine i32 @main() {")

        for comando in ast.nodos:
            nome = comando.__class__.__name__

            if nome == "NodoInstrumento":
                instrumento = comando.instrumento
                llvm.append(f'    call void @tocarInstrumento(c"{instrumento}\\00")')

            elif nome == "NodoNota":
                nota = comando.nota
                llvm.append(f'    call void @tocarNota(c"{nota}\\00")')

            elif nome == "NodoStop":
                llvm.append("    call void @parar()")

        llvm.append("    ret i32 0")
        llvm.append("}")

        return "\n".join(llvm)

# Definição Formal dos Tokens

- **Palavras-chave**:
    - **nota** → define uma nota
    - **instrumento** → define instrumento
    - **compasso** → define compasso
    - **repetir** → um bloco que repete o código dentro dele
    - **bpm** → define andamento
    - **play** → executa música
    - **stop** → encerra música
- **Símbolos especiais**:
    - **{  }** → agrupar blocos de música
    - **;** → fim de instrução
    - = → atribuição
- **Literais**:
    - **Notas**: (A-G)(#/b)?
    - **Números**: [0-9]+(/[0-9]+)
    - **Strings**: "[a-zA-Z]+"
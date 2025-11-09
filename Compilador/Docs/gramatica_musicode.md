
#  Definição Formal da Gramática
****
G = (V, Σ, P, S)

onde:

V = { Program, Statement, InstrumentoStmt, NotaStmt, StopStmt, RepetirStmt,
      StringStmt, NumericStmt, IdentificadoresStmt, 
      PontoVirgulaStmt, Number, Digit, LetterMusic, Character }

Σ = { "play", "instrumento", "nota", "stop", "repetir", "violao",
      "{", "}", "(", ")", ";", "\"", "#",
      "A", "B", "C", "D", "E", "F", "G",
      "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
      "$", ".", " " }

S = Program

P = O conjunto de produções segue abaixo, no formato EBNF.

## **Gramática em EBNF (Extended Backus–Naur Form)**

Program =  “play” “{” “statement” “}”

; Todos os códigos feitos nesta linguagem precisam começar com o token play{} e seguir o codigo dentro do bloco apenas

Statement = InstrumentoStmt 

| NumericStmt 

| IdentificadoresStmt

| repetirStmt 

| stopStmt 

| notaStmt 

| stringStmt 

| ponto_virgulaStmt .

InstrumentoStmt = “instrumento” “(” “violao” “)” “;”.

NumericStmt = Number [ "." Number ] ;

IdentificadoresStmt = “$” “Character”

repetirStmt =  “repetir” “(” “)”

stopStmt =  “stop” “(” “)”

notaStmt =  “nota” “(” “LetterMusic” “Number ” | “#” “)”

stringStmt = “ ” “  “Character” “ “ “

ponto_virgulaStmt = “;”

Number  = Digit { Digit } .

Digit         = "0" | "1" | ... | "9" .

LetterMusic = “A” | “B” | … | “G”

Character     = any printable ASCII character except ' and \ .

---

## **Gramática em BNF (Backus–Naur Form)**

<Program> ::= "play" "{" <StatementSeq> "}"

<StatementSeq> ::= <Statement> <StatementSeq>
| ε

<Statement> ::= <InstrumentoStmt>
| <NumericStmt>
| <IdentificadoresStmt>
| <repetirStmt>
| <stopStmt>
| <notaStmt>
| <stringStmt>
| <ponto_virgulaStmt>

<InstrumentoStmt> ::= "instrumento" "(" "violao" ")" ";"

<NumericStmt> ::= <Number> [ "." <Number> ] ;


<IdentificadoresStmt> ::= "$" <Character>

<repetirStmt> ::= "repetir" "(" ")"

<stopStmt> ::= "stop" "(" ")"

<notaStmt> ::= "nota" "(" <NotaArg> ")"

<NotaArg> ::= <LetterMusic> <Number>
| "#"

<stringStmt> ::= <StringLiteral>

<ponto_virgulaStmt> ::= ";"

<Number> ::= <Digit> <NumberTail>
<NumberTail> ::= <Digit> <NumberTail>
| ε

<Digit> ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"

<LetterMusic> ::= "A" | "B" | "C" | "D" | "E" | "F" | "G"

<StringLiteral> ::= "\"" <CharacterSeq> "\""

<CharacterSeq> ::= <Character> <CharacterSeq>
| ε

/* Character: qualquer caracter ASCII imprimível exceto ' e \  */
<Character> ::= /* terminal que corresponde a: qualquer caractere ASCII imprimível exceto ' e \ */
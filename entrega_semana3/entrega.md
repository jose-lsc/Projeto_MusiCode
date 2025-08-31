# Gramática Formal da Linguagem

# MusiCode

## Introdução

Este documento apresenta a primeira versão da gramática formal da linguagem
MusiCode. O objetivo principal da MusiCode é fornecer uma ferramenta de programação
para a criação e manipulação de estruturas musicais. A definição desta gramática segue
os princípios da Hierarquia de Chomsky, conforme solicitado na atividade proposta. Este
trabalho representa a fase inicial de estruturação sintática da linguagem, com foco na
clareza e na capacidade de descrição dos construtos fundamentais.

## 1. Definição do Alfabeto e Tokens

A base de qualquer linguagem formal reside na definição de seu alfabeto e de suas
unidades léxicas, os tokens. Para a linguagem MusiCode, esses elementos são
estabelecidos da seguinte forma:

### 1.1. Alfabeto (ΣmusiCode)

O alfabeto da linguagem MusiCode compreende o conjunto de todos os caracteres
válidos que podem ser utilizados na construção de programas. Ele é definido como a
união dos conjuntos de dígitos, dígitos numéricos, símbolos e identificadores, conforme
as especificações:

ΣmusiCode = { (Σdígitos U ΣdígitosNuméricos U Σsímbolos U Σidentificadores)}

```
Σdígitos : {_, a, ..., z, A, ..., Z}
Σinteiros : {0, ..., 9}
Σdecimais : { Σinteiros. Σinteiros}
Σsímbolos : {+, -, /, *, =, {}, (), [], ; , &, #}
Σstrings : {". ΣmusiCode ."}
```
#### •

#### •

#### •

#### •

#### •


### 1.2. Definição Formal dos Tokens

Os tokens são as menores unidades sintáticas com significado na linguagem, formadas a
partir das sequências de caracteres do alfabeto. As definições formais dos tokens da
MusiCode são as seguintes:

```
Palavras-chave : {nota, instrumento, compasso, repetir, bpm, play, stop, ...}
Identificadores : { ($). (Σdigito U Σinteiros) U {_} }
Comentários de Linha : { //. (Σdígitos U Σinteiros U Σsímbolos) - novaLinha.
novaLinha }
Comentários em Bloco : { /. (Σdígitos U Σinteiros U Σsímbolos). / }
```
## 2. Regras de Produção da Gramática Formal

A gramática formal da linguagem MusiCode é definida por um conjunto de regras de
produção que especificam como os tokens podem ser combinados para formar
sentenças válidas. A Notação Backus-Naur Estendida (EBNF) é utilizada para expressar
essas regras, visando clareza e precisão. O objetivo é estabelecer uma gramática livre de
contexto, cuja justificativa será apresentada na seção subsequente.

### 2.1. Estrutura Geral do Programa

Um programa MusiCode é composto por uma sequência de definições de músicas e
chamadas para execução dessas músicas:

```
< Programa > ::={ < DefinicaoMusica > | < ChamadaTocarMusica > }*
< DefinicaoMusica > ::="musica""{"< CorpoMusica >"}"
< CorpoMusica > ::= { < DeclaracaoInstrumento > | < DeclaracaoNota > |
< EstruturaRepeticao > | < DeclaracaoBPM > | < DeclaracaoCompasso > |
< Comentario > }*
< ChamadaTocarMusica > ::="tocar""("< Identificador >")"";"
```
### 2.2. Declarações e Expressões

Esta seção detalha as regras para as declarações e expressões fundamentais da
linguagem:

**2.2.1. Declaração de Instrumento**

Define o instrumento musical a ser utilizado:

```
< DeclaracaoInstrumento > ::="instrumento""="< String >";"
```
#### •

#### •

#### •

#### •


**2.2.2. Declaração de Nota**

Define uma nota musical específica e sua duração:

```
< DeclaracaoNota > ::="nota""("< NomeNota >","< DuracaoNota >")"";"
< NomeNota > ::="C"|"D"|"E"|"F"|"G"|"A"|"B"|"C#"|"Db"| ... // e outras
notas
< DuracaoNota > ::=< Inteiro >"/"< Inteiro > | < Decimal > | < Inteiro >
```
**2.2.3. Declaração de BPM (Batidas por Minuto)**

Define o andamento da composição musical:

```
< DeclaracaoBPM > ::="bpm""="< Inteiro >";"
```
**2.2.4. Declaração de Compasso**

Define a assinatura de tempo do compasso:

```
< DeclaracaoCompasso > ::="compasso""="< Inteiro >"/"< Inteiro >";"
```
### 2.3. Estruturas de Controle

Esta seção descreve as estruturas de controle implementadas na linguagem:

**2.3.1. Estrutura de Repetição**

Permite a repetição de um bloco de código musical um número especificado de vezes:

```
< EstruturaRepeticao > ::="repita"< Inteiro >"{"{ < DeclaracaoNota > |
< DeclaracaoBPM > | < DeclaracaoCompasso > | < Comentario > }*"}"
```
### 2.4. Elementos Léxicos (Terminais)

Os elementos terminais são os símbolos básicos da gramática que não podem ser
decompostos em unidades menores:

```
< String > ::=".*"// Qualquer sequência de caracteres entre aspas duplas
< Inteiro > ::= [0-9]+
< Decimal > ::= [0-9]+"."[0-9]+
< Identificador > ::="$"([ a-zA-Z0-9_ ]+) |"_"([ a-zA-Z0-9_ ]+) // Conforme
especificado nos tokens
< Comentario > ::= < ComentarioLinha > | < ComentarioBloco >
```

```
< ComentarioLinha > ::="//".* \ n
< ComentarioBloco > ::="/*".* "*/"
```
Esta é a versão inicial da gramática. Ela será objeto de refinamento e expansão para
incorporar construtos adicionais e garantir a não-ambiguidade. A classificação como
gramática livre de contexto será detalhada na próxima seção, juntamente com a
justificativa na hierarquia de Chomsky. [1]

## 3. Classificação da Gramática na Hierarquia de

## Chomsky

A gramática da linguagem MusiCode, conforme definida na Seção 2, é classificada como
uma **Gramática Livre de Contexto (Tipo 2)** na Hierarquia de Chomsky. Esta
classificação é fundamentada na estrutura das regras de produção e na adequação para
a descrição de linguagens de programação.

### 3.1. Características de uma Gramática Livre de Contexto

Uma Gramática Livre de Contexto (GLC) é definida por regras de produção na forma
A → β, onde A é um único símbolo não-terminal e β é uma sequência arbitrária de
símbolos terminais e/ou não-terminais. A característica distintiva de uma GLC é que a
aplicação de uma regra de produção para substituir A por β não depende do contexto
em que A aparece na cadeia de símbolos [1].

### 3.2. Justificativa para a Classificação da MusiCode

As regras de produção propostas para a MusiCode aderem estritamente ao formato
Não-Terminal → Sequência de Símbolos. Por exemplo:

```
<Programa> ::= { <DefinicaoMusica> | <ChamadaTocarMusica> }*
<DeclaracaoInstrumento> ::= "instrumento" "=" <String> ";"
<EstruturaRepeticao> ::= "repita" <Inteiro> "{" { <DeclaracaoNota> | ... }* "}"
```
Em nenhum caso, a aplicação de uma regra é condicionada pelos símbolos adjacentes
ao não-terminal no lado esquerdo da produção. Esta propriedade é intrínseca às
Gramáticas Livres de Contexto. A vasta maioria das linguagens de programação
modernas utiliza GLCs para especificar sua sintaxe devido à sua capacidade de
descrever estruturas hierárquicas (como aninhamento de blocos, expressões e
chamadas de função) e à sua eficiência para análise sintática por compiladores [1].

#### •

#### •

#### •


### 3.3. Comparação com Outros Tipos da Hierarquia de Chomsky

Para validar a classificação da MusiCode, é pertinente compará-la com os demais tipos
da Hierarquia de Chomsky:

```
Gramáticas Irrestritas (Tipo 0) : São as mais expressivas, capazes de descrever
qualquer linguagem recursivamente enumerável. Contudo, sua complexidade
computacional as torna impraticáveis para a definição de linguagens de
programação, dado o problema da indecidibilidade (a verificação de uma sentença
pode não terminar) [1]. A MusiCode não exige tal nível de expressividade.
```
```
Gramáticas Sensíveis ao Contexto (Tipo 1) : Nestas gramáticas, as regras de
produção dependem do contexto. Embora mais poderosas que as GLCs, sua
análise é significativamente mais complexa e, para a maioria dos aspectos
sintáticos de linguagens de programação, não são estritamente necessárias.
Condições que poderiam ser consideradas sensíveis ao contexto (e.g., a
obrigatoriedade de declaração de uma variável antes de seu uso) são tipicamente
tratadas na fase de análise semântica do compilador, e não na gramática sintática
[1].
```
```
Gramáticas Regulares (Tipo 3) : São as menos expressivas, adequadas para
descrever linguagens regulares, como padrões de texto (expressões regulares) ou a
estrutura de tokens (análise léxica). A MusiCode, com suas estruturas aninhadas e
hierárquicas (e.g., blocos de repetição e definições de música), possui uma
complexidade que excede a capacidade de uma gramática regular [1].
```
Em suma, a escolha de uma Gramática Livre de Contexto para a MusiCode representa o
equilíbrio ideal entre a expressividade necessária para descrever a sintaxe da linguagem
e a simplicidade que permite uma análise eficiente por ferramentas de compilação.

## 4. Exemplos de Derivações para Construtos Importantes

Para demonstrar a aplicação das regras de produção da gramática da MusiCode, são
apresentados exemplos de derivações para construtos essenciais da linguagem. Cada
derivação ilustra a sequência de substituições de não-terminais por suas produções até
que a sentença final seja composta exclusivamente por símbolos terminais.

### 4.1. Derivação de uma Declaração de Instrumento

Consideremos a derivação da declaração instrumento = "piano";:

```
<Programa>
```
#### •

#### •

#### •

#### 1.


```
-> <DefinicaoMusica>
-> "musica" "{" <CorpoMusica> "}"
-> "musica" "{" <DeclaracaoInstrumento> "}"
-> "musica" "{" "instrumento" "=" <String> ";" "}"
-> "musica" "{" "instrumento" "=" "\"piano\"" ";" "}"
```
Resultado: musica { instrumento = "piano"; }

### 4.2. Derivação de uma Declaração de Nota

Consideremos a derivação da declaração nota(C, 1/4);:

```
<Programa>
-> <DefinicaoMusica>
-> "musica" "{" <CorpoMusica> "}"
-> "musica" "{" <DeclaracaoNota> "}"
-> "musica" "{" "nota" "(" <NomeNota> "," <DuracaoNota> ")" ";" "}"
-> "musica" "{" "nota" "(" "C" "," <DuracaoNota> ")" ";" "}"
-> "musica" "{" "nota" "(" "C" "," <Inteiro> "/" <Inteiro> ")" ";" "}"
-> "musica" "{" "nota" "(" "C" "," "1" "/" "4" ")" ";" "}"
```
Resultado: musica { nota(C, 1/4); }

### 4.3. Derivação de uma Estrutura de Repetição

Consideremos a derivação do exemplo repita 2 { nota(G, 1/4); }:

```
<Programa>
-> <DefinicaoMusica>
-> "musica" "{" <CorpoMusica> "}"
-> "musica" "{" <EstruturaRepeticao> "}"
-> "musica" "{" "repita" <Inteiro> "{" { <DeclaracaoNota> }* "}" "}"
-> "musica" "{" "repita" "2" "{" <DeclaracaoNota> "}" "}"
-> "musica" "{" "repita" "2" "{" "nota" "(" <NomeNota> "," <DuracaoNota> ")" ";" "}"
"}"
-> "musica" "{" "repita" "2" "{" "nota" "(" "G" "," "1" "/" "4" ")" ";" "}" "}"
```
Resultado: musica { repita 2 { nota(G, 1/4); } }

Esses exemplos demonstram a capacidade da gramática livre de contexto da MusiCode
em gerar sentenças válidas, refletindo a estrutura hierárquica esperada da linguagem.
[1]

#### 2.

#### 3.

#### 4.

#### 5.

#### 6.

#### 1.

#### 2.

#### 3.

#### 4.

#### 5.

#### 6.

#### 7.

#### 8.

#### 1.

#### 2.

#### 3.

#### 4.

#### 5.

#### 6.

#### 7.

#### 8.


## 5. Análise de Ambiguidade Potencial e Estratégias de

## Resolução

A ambiguidade em gramáticas é um desafio significativo em linguagens de
programação, pois permite múltiplas interpretações para uma única sequência de
símbolos, resultando em inconsistências. Embora a gramática atual da MusiCode seja
relativamente simples, é fundamental identificar e propor soluções para potenciais
fontes de ambiguidade.

### 5.1. Precedência e Associatividade de Operadores

Na presente versão da MusiCode, as expressões aritméticas são restritas a valores
numéricos simples para durações de notas e BPMs. No entanto, a inclusão futura de
expressões mais complexas (e.g., bpm = 60 + 10 * 2;) exigirá a correta definição da
precedência e associatividade dos operadores. O material de estudo [1] ilustra como
uma gramática ambígua pode levar a interpretações incorretas de expressões como
id + id * id.

**Estratégia de Resolução:**

Para garantir a precedência correta dos operadores (e.g., multiplicação antes da adição),
a gramática deve ser reestruturada para estabelecer níveis hierárquicos distintos para
expressões, termos e fatores, conforme sugerido no material de estudo [1]. Um exemplo
adaptado seria:

```
< Expressao > ::=< Expressao >"+"< Termo > | < Termo >
< Termo > ::= < Termo >"*"< Fator > | < Fator >
< Fator > ::="("< Expressao >")"| < Identificador > | < Numero >
```
Esta abordagem impõe a ordem de avaliação das operações, eliminando a
ambiguidade. A associatividade (esquerda ou direita) pode ser controlada pela escolha
da recursão à esquerda ou à direita nas regras de produção.

### 5.2. O Problema do 'Dangling Else' (Else Pendurado)

Embora a MusiCode não inclua atualmente estruturas condicionais (if-else), é crucial
considerar o problema do 'dangling else' caso sejam implementadas no futuro. Este
problema surge quando uma cláusula else pode ser associada a múltiplos if s em uma
estrutura aninhada, gerando ambiguidade.

**Exemplo de Ambiguidade:**


```
if (condicao1)
if (condicao2)
acao1 ;
else
acao2 ;
```
Neste cenário, acao2 pode ser interpretada como pertencente ao primeiro if ou ao
segundo if.

**Estratégias de Resolução:**

Diversas estratégias podem ser empregadas para resolver o problema do 'dangling else':

```
Regra de Associação Padrão : A convenção mais comum é associar a cláusula else
ao if mais próximo. Esta regra pode ser formalizada na gramática através de
produções que distinguem if s com e sem else [1].
Uso de Delimitadores Explícitos : A exigência de delimitadores de bloco (e.g., {}
em C/Java ou end em Pascal) para todas as cláusulas if e else elimina a
ambiguidade, pois o escopo de cada bloco se torna explicitamente definido.
```
### 5.3. Ambiguidade em Comentários

A definição de comentários em bloco (/* ... */) pode introduzir ambiguidade se não for
tratada adequadamente, especialmente em casos de aninhamento ou quando o
delimitador de fim de comentário (*/ ) aparece dentro do próprio comentário. A
especificação atual é genérica em relação ao conteúdo interno.

**Estratégia de Resolução:**

Para comentários em bloco, a regra deve ser mais precisa, garantindo que o conteúdo
entre /* e */ não seja interpretado como o delimitador de fechamento. Esta questão é
tipicamente resolvida na fase de análise léxica, onde o analisador reconhece o
comentário como um único token e ignora seu conteúdo até encontrar o */
correspondente.

### 5.4. Ambiguidade na Definição de Identificadores

A regra para identificadores Identificadores = { ($). (Σdigito U Σinteiros) U {_} } pode ser
interpretada de forma ambígua. A notação de união (U ) pode sugerir que um
identificador pode começar com $ seguido por dígitos/inteiros OU começar com _.
Para maior clareza sobre a estrutura de um identificador (iniciando com $ ou _ e
seguido por uma sequência alfanumérica ou sublinhado), a regra deve ser mais
explícita.

#### 1.

#### 2.


**Estratégia de Resolução:**

A revisão da regra para uma definição mais precisa é recomendada. Por exemplo:

```
< Identificador > ::=("$"|"_") (< Digito > | < Letra > |"_")*
< Digito > ::= [0-9]
< Letra > ::= [ a-zA-Z ]
```
Esta regra estabelece claramente que um identificador inicia com $ ou _ e pode ser
seguido por zero ou mais dígitos, letras ou sublinhados. É essencial que as definições de
Σdígitos e Σinteiros sejam consistentes com o uso de <Digito> e <Letra> na definição
de identificadores.

### 5.5. Considerações Finais sobre Ambiguidade

A eliminação completa da ambiguidade em uma gramática formal pode, em alguns
casos, aumentar sua complexidade. O processo de balancear expressividade e
simplicidade, conforme destacado na atividade, é iterativo e fundamental para o
desenvolvimento da linguagem. A análise e resolução de ambiguidades são etapas
contínuas que acompanham a evolução da gramática.

### Referências

[1] Material de estudo fornecido pelo usuário (Capturas de tela de 29/08/2025).



# Linguagens Regulares e Expressões Regulares

## Especificação completa usando expressões regulares

**Literais :** 

Strings:  [” ^”/]|//

Números Inteiros: [+|-]\d+

Números decimais [+|-]\d+\.d*

**Identificadores:** [$][a-zA-Z0-9]

**Delimitadores:** \( , \), \{,  \}

**Comentários:** [//. *]

**Palavras-chave:** {nota, instrumento, compasso, repetir, bpm, play, stop, …}

**definição da nota :** [A-G](https://www.notion.so/Linguagens-Regulares-e-Express-es-Regulares-26400fe977a080088d65f4e99f1b4ede?pvs=21)?[0-9]?[#]?

**espaços em branco:** [ \t\r\n]+

## Análise de ambiguidades e regras de resolução

Assim como ensinado no material, o ideal é priorizar o “maior match” ou seja, em casos de identificadores com mesmo nome de palavras-chave ($nota e nota ou “nota”) vai ser priorizado o tipo (string ou numero) e caso não haja ocorrência de string, verificar o simbolo $ antes de qualquer palavra.

Aspas duplas dentro de string podem ser interpretadas com comentário, faremos então a validação para ver se não é uma string.

definir ; depois de palavras-chave como nota, se caso houver nota(C) nota(B), vai dar erro, então verificar se ao final da função teremos ;

## Estratégia para tratamento de erros léxicos

Verificar montagem de tokens, por exemplo, se a variável $(qualquer letra ou digito) tiver $$token, o segundo $ não é uma letra nem digito e sim simbolo especial, nesses casos não poderá gerar 

E na parte do relato, o analisador vai indicar o erro na linha .

## Primeiros esboços de mensagens de erro para usuários

Primeiro ao descobrir erros, buscaremos a localização da linha de erro, e para a mensagem de erro, talvez categorizar tipos de erros, por exemplo: erros com identificadores mal escritos, jogar um código de erro e apartir disso pegar a mensagem de erro e trazer no console.

# Classificação de erros lexicos

**Caractere inválido:** simbolos que não pertencem ao alfabetos precisam ser um dos primeiros parâmetros a serem analisados, e disparar um erro de acordo.
**Identificador mal formado:** por exemplo, começando com letra inválida (fora do padr~ao $[\d | [a-zA-Z]
**Token não reconhecido:** algo que não bate com nenhum padrão dos identificadores ou das palavras-chave
**Fim inesperado** linhas que não sao finalizadas com ; podem causar erro na hora de interpretar as funções

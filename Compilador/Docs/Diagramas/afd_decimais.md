# Diagrama do AFD - Reconhecimento de números decimais

```mermaid
stateDiagram-v2
    [*] --> q0
    q0 --> q1: 0-9

    q1 --> q1: 0-9
    q1 --> q2: "."

    q2 --> q3: 0-9

    q3 --> q3: 0-9
    q3 --> [*]

### Explicação:
- **q0** → estado inicial.  
  - Lendo um dígito (0–9) vai para **q1**.  
- **q1** → aceita inteiros (mas não é final).  
  - Continua em loop com dígitos.  
  - Se aparecer `"."`, passa para **q2**.  
- **q2** → espera **obrigatoriamente um dígito** depois do ponto decimal.  
- **q3** → estado final de aceitação.  
  - Continua em loop com dígitos.  

 Aceita: `"12345"`, `"0.56"`, `"00.7"`, `"12.3"`  
 Rejeita: `""`, `"abc"`, `"12.a"`, `"."`  



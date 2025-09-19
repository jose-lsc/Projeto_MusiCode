# Diagrama do AFD

```mermaid
stateDiagram-v2
    [*] --> q0
    q0 --> q1: "
    q1 --> q1: loop / qualquer símbolo exceto "
    q1 --> q2: "
    q1 --> q1: "\\"
    q2 --> [*]



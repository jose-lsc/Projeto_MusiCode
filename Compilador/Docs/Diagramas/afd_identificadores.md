# Diagrama do AFD - Reconhecimento de identificadores com `$`

```mermaid
stateDiagram-v2
    [*] --> q0
    q0 --> q1: "$"

    q1 --> q1: [a-zA-Z0-9$]

    q1 --> [*]

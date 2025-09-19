# Diagrama do AFD - Reconhecimento de números inteiros

```mermaid
stateDiagram-v2
    [*] --> q0
    q0 --> q1: 0-9
    q1 --> q1: 0-9
    q1 --> [*]



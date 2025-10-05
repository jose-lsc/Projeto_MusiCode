%% AFD resultante da conversão do AFN que contém 'ab'
graph LR
    
    start(( )) ---> S0
    
    %% Transições
    S0 -- a --> S1
    S0 -- b --> S0
    
    S1 -- a --> S1
    S1 -- b --> S2
    
    S2 -- a --> S3
    S2 -- b --> S3
    
    S3 -- a --> S3
    S3 -- b --> S3
    
    %% Aplicando estilo ao estado final
    classDef final fill:#f9f,stroke:#333,stroke-width:2px;
    S3:::final
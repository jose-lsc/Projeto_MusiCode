stateDiagram-v2
    [*] --> q0
    q0 --> q1 : s
    q1 --> q2 : t
    q2 --> q3 : o
    q3 --> q4 : p
    q4 --> q5 : (
    q5 --> q6 : )
    q6 --> [*]
    
    state q0 {
        [*] --> s
    }
    
    state q1 {
        t
    }
    
    state q2 {
        o
    }
    
    state q3 {
        p
    }
    
    state q4 {
        (
    }
    
    state q5 {
        )
    }
    
    state q6 {
        [*]
    }

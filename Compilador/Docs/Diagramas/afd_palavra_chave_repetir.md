stateDiagram-v2
    [*] --> q0
    q0 --> q1 : r
    q1 --> q2 : e
    q2 --> q3 : p
    q3 --> q4 : e
    q4 --> q5 : t
    q5 --> q6 : i
    q6 --> q7 : r
    q7 --> q8 : {
    q8 --> q9 : }
    q9 --> [*]
    
    state q0 {
        [*] --> r
    }
    
    state q1 {
        e
    }
    
    state q2 {
        p
    }
    
    state q3 {
        e
    }
    
    state q4 {
        t
    }
    
    state q5 {
        i
    }
    
    state q6 {
        r
    }
    
    state q7 {
        {
    }
    
    state q8 {
        }
    }
    
    state q9 {
        [*]
    }

stateDiagram-v2
    [*] --> q0
    q0 --> q1 : p
    q1 --> q2 : l
    q2 --> q3 : a
    q3 --> q4 : y
    q4 --> q5 : {
    q5 --> q6 : }
    q6 --> [*]
    
    state q0 {
        [*] --> p
    }
    
    state q1 {
        l
    }
    
    state q2 {
        a
    }
    
    state q3 {
        y
    }
    
    state q4 {
        {
    }
    
    state q5 {
        }
    }
    
    state q6 {
        [*]
    }

stateDiagram-v2
    [*] --> q0
    q0 --> q1 : n
    q1 --> q2 : o
    q2 --> q3 : t
    q3 --> q4 : a
    q4 --> q5 : (
    q5 --> q6 : a,b,c,d,e,f,g,A,B,C,D,E,F,G
    q5 --> q6 : 0,1,2,3,4,5,6,7,8,9,#
    q6 --> q6 : 0,1,2,3,4,5,6,7,8,9,#
    q6 --> q7 : )
    q7 --> q7 : " "
    q7 --> [*]
    
    state q0 {
        [*] --> n
    }
    
    state q1 {
        o
    }
    
    state q2 {
        t
    }
    
    state q3 {
        a
    }
    
    state q4 {
        (
    }
    
    state q5 {
        a,b,c,d,e,f,g,A,B,C,D,E,F,G
    }
    
    state q6 {
        0,1,2,3,4,5,6,7,8,9,#
    }
    
    state q7 {}

from collections import deque

def epsilon_closure(states, afn):
    
    closure = set(states)
    stack = list(states)
    while stack:
        state = stack.pop()
        if (state, '') in afn['transitions']:
            for next_state in afn['transitions'][(state, '')]:
                if next_state not in closure:
                    closure.add(next_state)
                    stack.append(next_state)
    return closure

def move(states, symbol, afn):
    
    result = set()
    for state in states:
        if (state, symbol) in afn['transitions']:
            result.update(afn['transitions'][(state, symbol)])
    return result

def afn_to_afd(afn):
    afd = {
        'initial': None,
        'states': set(),
        'alphabet': afn['alphabet'] - {''},
        'transitions': {},
        'final_states': set(),
        'token_types': {}
    }

    state_map = {}  
    queue = deque()

    
    start_closure = frozenset(epsilon_closure([afn['initial']], afn))
    state_map[start_closure] = 'S0'
    afd['initial'] = 'S0'
    afd['states'].add('S0')
    queue.append(start_closure)

    state_count = 1

    while queue:
        current = queue.popleft()
        current_name = state_map[current]

        for symbol in afd['alphabet']:
            move_result = move(current, symbol, afn)
            closure = frozenset(epsilon_closure(move_result, afn))

            if not closure:
                continue

            if closure not in state_map:
                state_map[closure] = f'S{state_count}'
                afd['states'].add(f'S{state_count}')
                queue.append(closure)
                state_count += 1

            dest_name = state_map[closure]
            afd['transitions'][(current_name, symbol)] = dest_name

    
    for state_set, state_name in state_map.items():
        for afn_final in afn['final_states']:
            if afn_final in state_set:
                afd['final_states'].add(state_name)
                afd['token_types'][state_name] = afn['token_types'][afn_final]
                break  

    return afd

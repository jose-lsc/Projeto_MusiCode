# lexer_play.py

from pprint import pprint

afd = {
    'initial': 'S0',
    'states': {'S0', 'S1', 'S2', 'S3', 'S4'},
    'alphabet': {'p', 'l', 'a', 'y'},
    'transitions': {
        ('S0', 'p'): 'S1',
        ('S1', 'l'): 'S2',
        ('S2', 'a'): 'S3',
        ('S3', 'y'): 'S4',
    },
    'final_states': {'S4'},
    'token_types': {
        'S4': 'KW_PLAY'
    }
}

def simulate_afd_greedy(afd, text, start_pos):
    state = afd['initial']
    last_token = None
    last_pos = start_pos

    i = start_pos
    while i < len(text):
        char = text[i]
        if (state, char) not in afd['transitions']:
            break
        state = afd['transitions'][(state, char)]
        i += 1
        if state in afd['final_states']:
            last_token = afd['token_types'][state]
            last_pos = i

    if last_token:
        return last_token, text[start_pos:last_pos], last_pos
    else:
        return None, text[start_pos], start_pos + 1  # erro léxico

def lexer(afd, text):
    tokens = []
    i = 0
    while i < len(text):
        if text[i].isspace():
            i += 1
            continue

        token_type, lexeme, next_pos = simulate_afd_greedy(afd, text, i)

        if token_type is None:
            tokens.append(('ERROR', lexeme))
        else:
            tokens.append((token_type, lexeme))

        i = next_pos

    return tokens

if __name__ == "__main__":
    frase = "play{}"
    resultado = lexer(afd, frase)

    print("Tokens:")
    for token_type, lexeme in resultado:
        print(f"{token_type}: '{lexeme}'")

# Exemplos de Programas

[====================================================]

Exemplo 1:

musica {
instrumento = "piano";
nota(C, 1/4);
nota(D, 1/4);
nota(E, 1/4);
nota(C, 1/2);
}

play(musica);

[====================================================]

Exemplo 2:

musica {
   instrumento = "guitarra";
   repetir 2 {
      nota(G, 1/4);
      nota(G, 1/4);
      nota(D, 1/2);
    }
}

play(musica);

[====================================================]
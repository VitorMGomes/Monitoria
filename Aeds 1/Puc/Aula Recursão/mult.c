#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include  <stdbool.h>


int multiplicacao(int multiplicando, int multiplicador)
{

    return multiplicador + multiplicacao(multiplicando, multiplicador - 1);
}


int main()
{

    int multiplicando = 7;
    int multiplicador = 5;

    int resp = multiplicacao(multiplicando, multiplicador);

    printf("%d", resp);
}


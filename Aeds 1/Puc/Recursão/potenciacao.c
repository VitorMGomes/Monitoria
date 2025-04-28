#include <stdlib.h>
#include <stdio.h>
#include <string.h>

// int multiplicar(int x, int y)
// {
//     return potenciacao(x, y, 0, 0);
// }

int potenciacao(int base, int expoente, int acumulador)
{
    if(expoente == 0)
    {
        return acumulador;
    }

    potenciacao(base, expoente - 1, acumulador * base);
}

int main()
{

    int num = 8;
    int x = 5;

    printf("O resultado é: %d\n", potenciacao(num, x, 1));

    return 0;
}
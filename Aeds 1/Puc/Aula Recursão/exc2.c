#include <stdlib.h>
#include <stdio.h>
#include <string.h>

// int multiplicar(int x, int y)
// {
//     return multiplicarOP(x, y, 0, 0);
// }

int multiplicar(int multiplicando, int multiplicador)
{
    if(multiplicador == 0)
    {
        return 0;
    }

    return multiplicando + multiplicar(multiplicando , multiplicador - 1);
}


int multiplicarOP(int valor, int multiplicador, int acumulador)
{
    if(multiplicador == 0)
    {
        return acumulador;
    }

    multiplicarOP(valor, --multiplicador, acumulador+valor);
}

int main()
{

    int num = 5;
    int x = 7;

    printf("O resultado é: %d\n", multiplicarOP(num, x, 0));

    return 0;
}
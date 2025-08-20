#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include  <stdbool.h>

bool desafio(int num, int div, int acumulador)
{
    if(div == 0)
    {
        return acumulador == num;
    }
    if(num % div == 0)
    {
        acumulador += div;
    }

    desafio(num, --div, acumulador);
}

int main()
{
    int i = 0;

    do
    {
        scanf("%d", &i);

        desafio(i, i - 1, 0) ? puts("É perfeito") : puts("Não é perfeito");

    }while(i >= 0);
}
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include  <stdbool.h>


int divisao(int a, int b, int acum)
{
    if(a > b)
    {
        divisao(a - b, b, acum + 1);
    }

    return 
}

int main()
{
    int dividendo = 29;
    int divisor = 7;

    int resultado = divisao(dividendo, divisor, 0); 
}
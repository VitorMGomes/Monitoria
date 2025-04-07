#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include  <stdbool.h>

bool desafio(int num, int div, int acumulador)
{
    if(div == 0 && acumulador == num)
    {
        return true;
    }
    else if(div == 0 && acumulador != num)
    {
        return false;
    }
    if(num % div == 0)
    {
        acumulador += div;
    }

    desafio(num, --div, acumulador);
}

int main()
{

}
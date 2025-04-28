#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main()
{
    int divisor = 4; //7
    int dividendo = 120;
    int resultado = 0;
    
    for(int i = dividendo; i >= divisor; resultado++)
    {
        i -= divisor;
    }

    printf("%d\n", resultado);

}
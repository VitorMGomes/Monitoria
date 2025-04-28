#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>


void fibonacci(int num1, int num2, int aux)
{
    if(aux <= 0)
    {
        return;
    }

    printf(" %d |", num1);
    fibonacci(num1 + num2, num1, --aux);
}


int main()
{
    //mostrar os N primeiros numeros da sequencia de fibonacci

    int n = 1;

    fibonacci(0, 1, n);
}
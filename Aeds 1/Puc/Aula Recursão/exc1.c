#include <stdlib.h>
#include <stdio.h>
#include <string.h>


int resultado_divisao(int n, int x, int i)
{
    if(n < x)
    {
        return i;
    }

    resultado_divisao(n - x, x, i + 1);
}

int main()
{
    int num = 45;
    int x = 7;

    printf("O resultado é: %d\n", resultado_divisao(num, x, 0));
}
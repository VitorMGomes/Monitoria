#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <string.h>

int calcularFatorial(int x) 
{
    if(x < 0)
    {
        printf("Não existe fatorial de um número negativo.");
        exit(1);
    }

    int resp = 1;

    for(int i = x; i > 1; i--)
    {
        resp = resp * i;
    }
    
    return resp;
}

int main()
{
    int num;

    do{
        
        scanf("%d", &num);

        int resp = calcularFatorial(num);

        printf("%d! é: %d\n", num, resp);

    }while(num >= 0);
}
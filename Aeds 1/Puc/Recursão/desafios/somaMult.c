#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include  <stdbool.h>



int soma_multiplicativa(int n)
{
    if(n < 0)
    {
        return -1;
    }
    else if(n == 0 || n == 1)
    {
        return n;
    }
    
    return soma_multiplicativa(n - 1) + n * soma_multiplicativa(n - 2);
}


int main()
{
    int n = 0;

    do{
        printf("(Número negativo para encerrar) Digite um valor:");
        scanf("%d", &n);

        printf("\nO resultado da soma multiplicativa é: %d\n\n\n", soma_multiplicativa(n));


    }while(n >= 0);
}
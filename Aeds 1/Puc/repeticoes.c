#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <string.h>


int repeticoes(char* palavra)
{
    int contador = 0;

    for(int i = 0; i < strlen(palavra) - 1; i++)
    {
        for(int j = i + 1; j < strlen(palavra);j++)
        {
            if(palavra[i] == palavra[j])
            {
                contador++;
                i = strlen(palavra);
            }
        }
    }

    //printf("%d", contador);

    return contador;

}

int main()
{

    int count = 0;

    while(count < 2)
    {
        char palavra[20];

        scanf(" %s", &palavra);

        if(repeticoes(palavra) > 0 )
        {
            count++;
        }

    }

}
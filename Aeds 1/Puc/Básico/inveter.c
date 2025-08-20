#include <stdio.h>
#include <stdlib.h>


int main()
{
    int numero;
    
    puts("Digite o número que deseja inverter (Número de 3 digitos): ");
    scanf("%d", &numero);

    int centena;
    int dezena;
    int unidade;

    unidade = numero % 10;

    numero = (numero - unidade) / 10;
 
    dezena = numero % 10;
    numero = (numero - dezena) / 10;

    centena = numero;

    int resultado = unidade * 100 + dezena * 10 + centena;

    printf("O número invertido é: %d\n", resultado);


}
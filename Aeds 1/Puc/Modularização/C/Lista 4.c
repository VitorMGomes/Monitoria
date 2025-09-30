#include <stdlib.h>

int par(num)
{
    return (num * 2);
}

void exercicio1()
{
    puts("Digite um numero");
    int num;
    scanf(num);

    int resp = par(num);

    print("O enésimo numero par é: %d", num);

}


void menu(int Questao)
{
    if(Questao == 1 )
    {
        exercicio1();
    }
    else if( Questao == 2)
    {
        exercicio2();
    }
}





int main()
{
    int Questao;

    print("Digite o número da questão: ");
    scanf("%d", &Questao);
    menu(Questao);





    return 0;
    
}
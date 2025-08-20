#include <stdlib.h>
#include <stdio.h>
#include <string.h>

typedef struct Data {
    int dia, mes, ano;
} Data;

typedef struct Pessoa {
    char *nome;
    float altura;
    Data data;
} Pessoa;

Data readData() {
    Data temp;
    scanf("%d", &temp.dia);
    scanf("%d", &temp.mes);
    scanf("%d", &temp.ano);
    return temp;
}

Pessoa newPessoa() {
    Pessoa temp;
    temp.nome = malloc(50 * sizeof(char));
    scanf(" %[^\n]", temp.nome); // lê nome com espaços
    scanf("%f", &temp.altura);
    temp.data = readData();
    return temp;
}

int main() {
    int nPessoas;
    scanf("%d", &nPessoas);

    Pessoa *pessoas = malloc(nPessoas * sizeof(Pessoa));

    for (int i = 0; i < nPessoas; i++) {
        pessoas[i] = newPessoa();
    }

    //Pode printar todas as pessoas aqui

    for (int i = 0; i < nPessoas; i++) {
        free(pessoas[i].nome);
    }
    free(pessoas);

    return 0;
}

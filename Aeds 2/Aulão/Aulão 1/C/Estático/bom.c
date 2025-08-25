#include <stdio.h>
#include <stdbool.h>

typedef struct Aluno {
    char  Nome[21];   // 20 + '\0'
    float Altura;
    bool  Aprovado;
} Aluno;

void readAluno(Aluno *temp) {
    scanf("%20s", temp->Nome);
    scanf("%f",  &temp->Altura);

    int aprovado;
    scanf("%d", &aprovado);
    temp->Aprovado = (aprovado != 0);
}

void printAluno(const Aluno *aluno) {
    printf("Nome: %s\n", aluno->Nome);
    printf("Altura: %.2f\n", aluno->Altura);
    printf("Status: %s\n", aluno->Aprovado ? "Aprovado" : "Reprovado");
    putchar('\n');
}

int main(void) {
    int x;

    Aluno alunos[x];

    // leitura
    for (int i = 0; i < x; i++) {
        readAluno(&alunos[i]);
    }

    // impressão
    for (int i = 0; i < x; i++) {
        printAluno(&alunos[i]);
    }

    return 0;
}

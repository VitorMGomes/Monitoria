#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int soma(char valor){
    if(valor == '\0'){
        return 0;
    }
    return (valor - '0') + soma(valor + 1);

}
int main(){
    char num[10];
    scanf("%s", num);
    int resp;
    while (strcmp(num, "FIM") != 0) {
        resp = soma(num); 
        printf("%d\n", resp);
        scanf("%s", num);
    }
}
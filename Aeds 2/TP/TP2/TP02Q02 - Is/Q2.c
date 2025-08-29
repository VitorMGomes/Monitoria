#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

bool stop(char *input)
{
    bool stop = false;

    if(strlen(input) == 3 && input[0] == 'F' && input[1] == 'I' && input[2] == 'M')
    {
        stop = true;
    }


    return stop;

}

bool isVogal(char *input)
{
    bool is = true;

    int len = strlen(input);
    for(int i = 0; i < len; i++) {
        char c = input[i];
        if (c >= 'A' && c <= 'Z') c = c - 'A' + 'a';
        if (c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u') {
            is = false;
            i = len;
        }
    }
    return is;
}

bool isConso(char *input)
{
    bool is = true;
    int len = strlen(input);
    for(int i = 0; i < len; i++) {
        char c = input[i];
        if (c >= 'A' && c <= 'Z') c = c - 'A' + 'a';
        if (c < 'a' || c > 'z') {
            is = false;
            i = len;
        }
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
            is = false;
            i = len;
        }
    }
    return is;
}

bool isInt(char *input)
{
    bool is = true;
    int len = strlen(input);
    if (len == 0) return false;
    for(int i = 0; i < len; i++) {
        if (input[i] < '0' || input[i] > '9') {
            is = false;
            i = len;
        }
    }
    return is;
}

bool isReal(char *input)
{
    bool is = true;
    int len = strlen(input);
    int cont = 0;
    if (len == 0) return false;
    for(int i = 0; i < len; i++) {
        if ((input[i] < '0' || input[i] > '9') && input[i] != '.' && input[i] != ',') {
            is = false;
            i = len;
        }
        if (input[i] == '.' || input[i] == ',') {
            cont++;
            if (cont > 1) {
                is = false;
                i = len;
            }
        }
    }
    return is;
}





int main()
{
    char input[1024];
    fgets(input, 1024, stdin);
    int len = strlen(input);
    if (len > 0 && input[len-1] == '\n') input[len-1] = '\0';

    while(!stop(input))
    {
        if(isVogal(input))
            printf("SIM ");
        else
            printf("NAO ");

        if(isConso(input))
            printf("SIM ");
        else
            printf("NAO ");

        if(isInt(input))
            printf("SIM ");
        else
            printf("NAO ");

        if(isReal(input))
            printf("SIM\n");
        else
            printf("NAO\n");

        fgets(input, 1024, stdin);
        len = strlen(input);
        if (len > 0 && input[len-1] == '\n') input[len-1] = '\0';
    }
    return 0;
}
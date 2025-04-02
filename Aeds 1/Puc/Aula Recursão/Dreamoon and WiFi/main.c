#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main()
{
    char s1[10];
    char s2[10];
    
    int n = 0;
    int unde = 0;

    scanf("%s", s1);
    getchar();
    scanf("%s", s2);

    for(int i = 0; i < strlen(s1); i++)
    {
        if(s1[i] == '+')
        {
            n++;
        }
        else if(s1[i] == '-')
        {
            n--;
        }
    }

    for(int i = 0; i < strlen(s2); i++)
    {
        if(s2[i] == '+')
        {
            n++;
        }
        else if(s2[i] == '-')
        {
            n--;
        }
        else if(s2[i] == '?')
        {
            unde++;
        }
    }

    if(n > unde)
    {
        printf("a");
    }
    
}
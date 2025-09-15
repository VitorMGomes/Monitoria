#include <stdio.h>
#include <stdbool.h>


bool primo(int num, int cont, bool resp)
{
    if(resp == false)
    {
        return false;
    }
    if(cont == num - 1)
    {
        return true;
    }
    if(num % cont == 0)
    {
        resp = false;
    }

    return primo(num, cont + 1, resp);
}



int main()
{
    int num;
    scanf(" %d", &num);

    bool resp = primo(num, 2, true);
}
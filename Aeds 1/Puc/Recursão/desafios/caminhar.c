#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include  <stdbool.h>

int caminhar(int x, int y)
{
    if(x <= 0 || y <= 0)
    {
        return 0;
    }
    else if(x == 1 && y == 1)
    {
        return 1;
    }
    else {
    return caminhar(--x,y) + caminhar(x,--y);
    }
}

int main()
{
    int a = 4;
    int b = 4;

    printf("%d", caminhar(a, b));
}
#include <stdlib.h>
#include <stdio.h>
#include <string.h>


int fatorial(int n)
{
    if(n == 0)
    {
        return 1;
    }
    else{
        return n * fatorial(n-1);
    }
}


int main()
{

}


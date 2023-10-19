#include <stdio.h>

int main()
{
    int x, y;
    x = y = 1;
    int z = 2;
    int result;
    result = -++x + y-- + z--;
    printf("%d\n", result);
    printf("x %d\n", x);
    printf("y %d\n", y);
    printf("z %d\n", z);
}
#include <stdio.h>

int gcd(int a, int b)
{
    while (b != 0)
    {
        int temp = a;
        a = b;
        b = temp % b;
    }
    return a;
}

int main()
{
    int result = gcd(56, 98);
    printf("%d\n", result); // 14
    return 0;
}

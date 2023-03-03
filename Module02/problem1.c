#include <stdio.h>

int test(int x, int y)
{
    return x == y ? (x + y) * 3 : x + y;
}

int main(void)
{
    printf("%d", test(1, 2));
    printf("\n%d", test(2, 2));
}
#include<stdio.h>
#include <string.h>

int main()
{
    char x[] = "Hello";
    char y[] = "Josh";
    strcat(x, y);
    printf("%s", x);
    //printf("Hello World ECE 336 Class!");
    return 0;
}
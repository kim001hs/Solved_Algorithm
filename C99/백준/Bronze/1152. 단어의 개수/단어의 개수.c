#include <stdio.h>
#include <string.h>

int main()
{
    char words[1000002];
    fgets(words, sizeof(words), stdin);
    int len = strlen(words);
    int sum = 1;
    for(int i = 0; i < len-1; i++)
    {
        if(words[i] == ' ')
        {
            sum++;
        }
    }
    if(words[0]==' ')
    {
        sum--;
    }
    if (words[len - 2] == ' ')
    {
		sum--;
    }
    printf("%d", sum);
}
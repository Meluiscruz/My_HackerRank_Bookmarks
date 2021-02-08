#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
    int a, b;
    char labels[11][6] ={"one","two","three","four","five","six","seven","eight","nine","even","odd"};
    
    scanf("%d\n%d", &a, &b);
    
  	for(int index = a; index <= b ; index++){
        printf("%s\n", labels[index <= 9 ? index - 1 : 9 + index % 2]);
      }

    return 0;
}
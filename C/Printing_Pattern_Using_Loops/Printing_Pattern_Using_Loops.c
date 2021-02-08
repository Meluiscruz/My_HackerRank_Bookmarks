#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
    int n;
    scanf("%d", &n);
    int m = 2*n -1;
    //Columns
  	for (int i = 0; i < m; i++){ 
        //Rows
        for (int j = 0; j < m; j++){
            //Main part of the computing
            int min;
            if(i < j)
                min = i;
            else {
                min = j;
            }
            if(min < m - i)
                min = min;
            else {
                min = m - i - 1;
            }
            if(min < m - j - 1)
                min = min;
            else {
                min = m - j - 1;
            }
            printf("%d ", n - min);
        }
        printf("\n");   //jump line at the end of the computing.
    }
    return 0;
}
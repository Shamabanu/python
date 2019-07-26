#include <stdio.h>

int main()
{
    int rows, cols, i, j, k;
    printf("Enter number of rows: ");
    scanf("%d", &rows);
    printf("Enter number of columns: ");
    scanf("%d", &cols);
    k = 1;
    for(i=1; i<=rows; i++)
        {
            
        for(j=1; j<=cols; j++, k++)
        {
            if(j!=cols){
            printf("%d*", k);
        }
            else{
                printf("%d",k);
            }
        }

        printf("\n");
    }

    return 0;
}

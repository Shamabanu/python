#include <stdio.h>
int main()
{
    int n=5,i, j,k,l,m,p,q;
    for(i=n; i>0; i--)
    {
        for(j=1; j<=i; j++)
        {
            printf("*");
        }
        for(l=i;l<n;l++)
        {
            printf(" ");
        }
        for(j=1; j<=i; j++)
        {
            printf("*");
        }
        if(i!=1)
        printf("\n");
    }
    for(m=0;m<=n;m++)
    {
        for(k=0;k<m;k++)
        {
            printf("*");
        }
        for(p=m;p<n;p++)
        {
            printf(" ");
        }
        for(q=1; q<=m; q++)
        {
            printf("*");
        }
        printf("\n");
    }
    return 0;
}

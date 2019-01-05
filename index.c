#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
int main() 
{
  int q,*b,n=0;
  scanf("%d",&q);
  b=(int*)malloc(sizeof(int)*q);
  for(int i=0;i<q;i++)
  {
    scanf("%d",&b[i]);
  }  
  for(int i=0;i<(q-2);i++)
  {
    for(int j=i+1;j<(q-1);j++)
    {
      for(int k=j+1;k<q;k++)
      {
        if(b[j]>b[i] && b[k]>b[j])
        {
        n++;
        }
      }
    }
  }
  printf("%d",n);
}

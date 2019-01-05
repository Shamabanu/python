#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
int main() 
{
  int a,*b,n=0;
  scanf("%d",&a);
  b=(int*)malloc(sizeof(int)*a);
  for(int i=0;i<a;i++)
  {
    scanf("%d",&b[i]);
  }  
  for(int i=0;i<(a-2);i++)
  {
    for(int j=i+1;j<(a-1);j++)
    {
      for(int k=j+1;k<a;k++)
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

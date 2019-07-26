void main()
{
int i,j,k;
for(i=4;i>=1;i--)
{
for(j=1;j<=4;j++)
{
if(j<=i)
printf("%d",j);
else
printf(" ");
}
for(j=3;j>=1;j--)
{
if(j<=i)
printf("%d",j);
else
printf(" ");
} 
printf("\n");
}
}
/*output
1234321
123 321
12   21
1     1
*/

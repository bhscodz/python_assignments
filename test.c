#include <stdio.h>

int main()
{
    int arr[3]={1,2,3};
    int p1=0;
    for (int i = 0; i < 10; i++)
    {
        p1=(p1+1)%3;
        printf("%d ",arr[p1]);
    }
    
    
    return 0;
}
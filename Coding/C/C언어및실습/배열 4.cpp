#include <stdio.h>


void make_array(int arr[100][100],int N) {
   int num = 1;
   for (int i=0;i<N;i++) {
       if (i%2 == 0) {
           for (int j=0;j<N;j++) {
               arr[i][j] = num;
               num++;
           }
       }
       else {
           for (int j=N-1;j>=0;j--) {
               arr[i][j] = num;
               num++;
           }
       }
   }
}

void print_array(int arr[100][100], int N) {
   for (int i=0;i<N;i++) {
       for (int j=0;j<N;j++) {
           printf("%2d ",arr[i][j]);
       }
       printf("\n");
   }
}

int main()
{
   int N,arr[100][100];
   
   scanf("%d",&N);
   make_array(arr,N);
   print_array(arr,N);
}

 

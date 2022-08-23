#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int MAX(int a[],int N) {
   int MAX_VAL = -1;
   for (int i=0;i<N;i++) {
       MAX_VAL = (MAX_VAL > a[i])? MAX_VAL:a[i];
   }
   return MAX_VAL;
}

int MIN(int a[],int N) {
   int MIN_VAL = 101;
   for (int i=0;i<N;i++) {
       MIN_VAL = (MIN_VAL < a[i])? MIN_VAL:a[i];
   }
   return MIN_VAL;
}

int main(){
   srand(time(NULL));
   int N;
   scanf("%d",&N);
   int arr[N];
   for (int i=0;i<N;i++) {
       arr[i] = rand()%100 + 1;
   }
   for (int i=0;i<N;i++) {
       printf("%d ",arr[i]);
   }
   printf("\n%d %d",MAX(arr,N),MIN(arr,N));
}

#include <stdio.h>

void find_divisor(int arr[],int x) {
   for (int i=1;i<=x;i++) {
       if (x%i == 0) arr[i] = i;
   }
}

int main() {
   int P,Q, numP[100] = {0}, numQ[100] = {0};
   scanf("%d %d",&P,&Q);
   
   find_divisor(numP,P);
   find_divisor(numQ,Q);

   for (int i=1;i<=P;i++) {
       for (int j=1;j<=Q;j++) {
           if (numP[i]&&numQ[j]) {
               printf("%d %d\n",numP[i],numQ[j]);
           }
       }
   }
}

 

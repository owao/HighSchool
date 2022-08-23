#include <stdio.h>

void sumOfWeight(int g) {

   int cnt = 0;
   for (int i=1;i<=10;i++) {
       for (int j=1;j<=10;j++) {
           for (int k=1;k<=10;k++) {
               int sum = 2*i+3*j+5*k;
               if (sum == g) {
                   printf("%d %d %d\n",i,j,k);
                   cnt++;
               }
           }
       }
   }
   printf("%d",cnt);

}

int main() {
	
   int G;
   scanf("%d",&G);
   sumOfWeight(G);

}

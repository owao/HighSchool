#include <stdio.h>

int rSum(int n) {
	
   if (n < 10) return n;
   else return n%10 + rSum(n/10);

}

int main() {

   int N;
   scanf("%d",&N);
   printf("%d",rSum(N));
   return 0;

}

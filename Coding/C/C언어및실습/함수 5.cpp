#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void getDiceFace(int N) {

   static int one,two,three,four,five,six,cnt;
   cnt++;
   int face = rand()%6+1;
   if (face == 1) one++;
   else if (face == 2) two++;
   else if (face == 3) three++;
   else if (face == 4) four++;
   else if (face == 5) five++;
   else six++;

   if (cnt == N) {
       printf("1: %d\n2: %d\n3: %d\n4: %d\n5: %d\n6: %d\n",one,two,three,four,five,six);
   }
}

int main() {

   int N;
   scanf("%d",&N);
   srand(time(NULL));
   for (int i=1;i<=N;i++) {
       getDiceFace(N);
   }
}

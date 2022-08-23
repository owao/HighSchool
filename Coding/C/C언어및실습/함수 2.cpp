#include <stdio.h>
#include <math.h>

void newtonsLaw(float m) {
	
   double g=9.81,c=12.5;
   
   for (int t=0;t<=30;t+=2) {
       double vt = g*m/c*(1-exp(-(c/m)*t));
       printf("%2d sec   %7.4f m/s\n",t,vt);
   }
   
}


int main() {

   float m;
   scanf("%f",&m);
   newtonsLaw(m);
   return 0;

}

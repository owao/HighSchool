#include <stdio.h>

int main(){
	
	int a;
	int b;
	a=0;
	b=0; 
	
	while (b<100){
		a++;
		b += a;
	}
	
	printf("%d", a);
}

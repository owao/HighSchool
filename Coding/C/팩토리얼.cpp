#include <stdio.h>

int main(){
	int i;
	int a;
	int b;
	b=1;
	
	scanf("%d", &a);
	
	for(i=a; i<0; i--)
		b *= i;
		
	printf("%d", a);
}

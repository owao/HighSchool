#include <stdio.h>

int main(){
	
	int a;
	int b;
	
	printf("Enter number:");
	scanf("%d", &a);
	printf("\nResult:");
	while (a>0){
		b=a%10;
		printf("%d", b);
		a=(a/10)-(b/10);
	}
		
}

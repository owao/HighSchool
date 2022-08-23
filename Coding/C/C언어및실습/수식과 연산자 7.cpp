#include <stdio.h>

int main(){
	
	int C;
	int pieces;
	
	scanf("%d", &C);
	
	pieces = (C/2 +1)*(C - C/2 +1);
	
	printf("%d", pieces);
	
}

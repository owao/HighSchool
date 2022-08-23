#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Bank{
	int num; //°èÁÂ¹øÈ£ 
	char name[10];
	int money;
};

int main(void){
	
	struct Bank b;
	
	scanf("%d %s %d", &b.num, &b.name, &b.money);
	
	printf("%sÀÇ %d °èÁÂÀÇ ÀÜ¾×Àº %d¿ø", b.name, b.num, b.money);
	
	return 0; 
} 

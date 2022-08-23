#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Bank{
	int num; //°èÁÂ¹øÈ£ 
	char name[10];
	int money;
};

void test(struct Bank* a){
	scanf("%d %s %d", &a->num, &a->name, &a->money);
	
	printf("%sÀÇ %d °èÁÂÀÇ ÀÜ¾×Àº %d¿ø", a->name, a->num, a->money);
}

int main(void){
	
	struct Bank b;
	
	test(&b);
	
	return 0; 
} 

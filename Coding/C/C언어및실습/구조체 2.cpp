#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Bank{
	int num; //���¹�ȣ 
	char name[10];
	int money;
};

void test(struct Bank* a){
	scanf("%d %s %d", &a->num, &a->name, &a->money);
	
	printf("%s�� %d ������ �ܾ��� %d��", a->name, a->num, a->money);
}

int main(void){
	
	struct Bank b;
	
	test(&b);
	
	return 0; 
} 

#include <stdio.h>
#define EXCHANGE_RATE 1120 //dollar to won

int main(){
	
	int won = 1000000; //�鸸
	
	int dollar = won / EXCHANGE_RATE;
	
	printf("��ȭ %d���� ȯ���ϸ� ���� �� �ִ� �޷��� $%d�̴�.", won, dollar);
	
}

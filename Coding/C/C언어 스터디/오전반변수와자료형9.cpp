#include <stdio.h>
#define EXCHANGE_RATE 1120 //dollar to won

int main(){
	
	int won = 1000000; //백만
	
	int dollar = won / EXCHANGE_RATE;
	
	printf("한화 %d원을 환전하면 받을 수 있는 달러는 $%d이다.", won, dollar);
	
}

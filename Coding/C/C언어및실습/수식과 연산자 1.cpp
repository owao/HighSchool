#include <stdio.h>

int main(){
	
	int a;
	int b;
	int change;
	
	//a b 받아오기 
	scanf("%d %d", &a, &b);
	
	//원래 a b 출력 
	printf("%d %d \n", a, b); 
	
	//a b 바꾸기
	change = a;
	a = b;
	b = change;
	
	//바꾼 a b 출력
	printf("%d %d \n", a, b); 
}

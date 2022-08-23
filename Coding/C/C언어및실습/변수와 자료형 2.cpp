#include <stdio.h>

int main(){
	
	float x;
	
	printf("실수를 입력하세요: ");
	scanf("%f", &x);	
	printf("\n");
		
	float y = 3*x*x + 7*x + 11;
	
	printf("다항식의 값은 %f", y);
}

#include <stdio.h>

int main(){
	
	float weight; 
	
	printf("몸무게를 입력하세요(단위: kg): ");
	scanf("%f", &weight);	
	printf("\n");
		
	float moon_weight = (weight*17)/100;
	
	printf("달에서의 몸무게는 %fkg입니다.", moon_weight);
}

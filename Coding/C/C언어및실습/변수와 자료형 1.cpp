#include <stdio.h>

int main(){
	
	float a;
	float b;
	float c;
	
	printf("\n실수를 입력하시오: ");
	scanf("%f", &a);
	
	printf("\n실수를 입력하시오: ");
	scanf("%f", &b);
	
	printf("\n실수를 입력하시오: ");
	scanf("%f", &c);
	
	printf("\n");
		
	float sum = a+b+c;
	float average = sum/3;
	
	printf("합은 %f이고 평균은 %f입니다.", sum, average);
}

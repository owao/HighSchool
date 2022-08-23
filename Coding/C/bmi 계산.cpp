#include <stdio.h>

int main(){
	
	float height;
	float weight;
	float result;
	
	printf("Enter height(m) : ");
	scanf("%f", &height);
	printf("\nEnter weight(kg) : ");
	scanf("%f", &weight);
	
	result=weight/(height*height);
	

	if (result<18.5)
		printf("\nbmi : %.f, 저체중입니다", result);
	else if (18.5<=result and result<25.0)
		printf("\nbmi : %.f, 정상입니다", result);
	else if (25.0<=result and result<30.0)
		printf("\nbmi : %.f, 과체중입니다", result);
	else if (30.0<=result)
		printf("\nbmi : %.f, 비만입니다", result);
	
}

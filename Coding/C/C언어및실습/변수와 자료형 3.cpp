#include <stdio.h>

int main(){
	
	float weight; 
	
	printf("�����Ը� �Է��ϼ���(����: kg): ");
	scanf("%f", &weight);	
	printf("\n");
		
	float moon_weight = (weight*17)/100;
	
	printf("�޿����� �����Դ� %fkg�Դϴ�.", moon_weight);
}

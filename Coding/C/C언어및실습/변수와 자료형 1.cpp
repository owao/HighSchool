#include <stdio.h>

int main(){
	
	float a;
	float b;
	float c;
	
	printf("\n�Ǽ��� �Է��Ͻÿ�: ");
	scanf("%f", &a);
	
	printf("\n�Ǽ��� �Է��Ͻÿ�: ");
	scanf("%f", &b);
	
	printf("\n�Ǽ��� �Է��Ͻÿ�: ");
	scanf("%f", &c);
	
	printf("\n");
		
	float sum = a+b+c;
	float average = sum/3;
	
	printf("���� %f�̰� ����� %f�Դϴ�.", sum, average);
}

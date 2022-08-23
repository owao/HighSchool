#include <stdio.h>

int main(){
	
	float r = 5.37;
	const float pi = 3.14;
	float area = pi*r*r;
	float circumference = 2*pi*r;
	
	printf("원의 면적은 %f이고, 원의 둘레는 %f입니다.", area, circumference);
}

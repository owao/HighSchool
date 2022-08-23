#include <stdio.h>

int main()
{
	float height;
	float weight;
	float a;
	float b;
	
	printf("Enter your height and weight:");
	scanf("%f %f", &height, &weight);
	
	a=(height-100)*0.9;
	b=weight-a;
	
	printf("표준 몸무게:%f, gap = %+.2f", a,b);
}

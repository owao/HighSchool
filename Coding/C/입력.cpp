#include <stdio.h>

int main()
{
	int age;
	int height, weight;
	
	printf("Enter your age:");
	scanf("%d", &age);
	printf("Your age is %d\n", age);
	
	printf("Enter your height and weight:");
	scanf("%d %d", &height, &weight);
	printf("height:%d weight:%d", height, weight);
 } 

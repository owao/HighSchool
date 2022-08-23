#include <stdio.h>

int main(void)
{
	printf("%4d\n", 1234);
	printf("%4d\n", 12345);
	printf("%4d\n", 12);
	printf("%04d\n", 12);
	printf("%-4d\n", 12);
	printf("%+4d %+4d\n", 12, -34);
	printf("%+4d %+4d\n", 122345, -343234234);
	
	printf("%f\n", 1.2);
	printf("%0.2f\n", 1.2);
	printf("%.2f\n", 1.2);
	printf("%.2f\n", 1234.23456);
	printf("%10.3f\n", 1234.23456);
	
	printf("%10s %10d\n", "program", 123);
}

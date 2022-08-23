#include <stdio.h>

int main(){
	
	int num;
	int A = 2;
	int B = 12;
	num = ((B/A++) + (B/++A)) + ++B;
	printf(num);
	

}

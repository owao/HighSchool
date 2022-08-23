#include <stdio.h>

int main(){
	
	int number;
	int answer;
	 
	scanf("%d", &number);
	
	answer = number % 10;
	number = number / 10;
	
	answer += number % 10;
	number = number / 10;
	
	answer += number % 10;
	number = number / 10;
	
	answer += number;
	
	printf("%d\n", answer);	
	
}

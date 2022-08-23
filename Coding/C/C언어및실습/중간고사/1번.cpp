#include <stdio.h>
#include <stdlib.h>

int hailstoneSequence(int n){
	if(n%2){
		n = 3*n + 1;
		printf("%d ", n);
		return n;
	}
	else{		
		n = n/2;
		printf("%d ", n);
		return n;
	}
}

int main(int argc, char *argv[]) {
	
	int num;
	int a; //증간 변수 
	
	scanf("%d", &num);
	
	a = num;
	
	while(num != 1){
		num = hailstoneSequence(num);
		if(a < num){
			a = num;
		}
	}
	
	printf("\n%d", a);
	
	return 0;
}

#include <stdio.h>
#include <stdlib.h>

int product(int a, int b){
	int P=a; //결과 

	if(b==1){
		return P;
	}
	else{
		P = product(a, 1) + product(a, b-1);
	}
}

int quotient(int a, int b){
	int Q; //결과 
	
	return Q;
}

int remain(int a, int b){
	int R; //결과 
	
	return R;
}


int main(int argc, char *argv[]) {
	
	int a, b;
	int P, Q, R;
	
	scanf("%d %d", &a, &b);
	P = product(a, b);
	Q = quotient(a, b);
	R = remain(a, b);
	printf("%d %d %d", P, Q, R);
	
	return 0;
}

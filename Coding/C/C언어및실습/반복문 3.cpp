#include <stdio.h>

int main(){
	
	int N;
	int a, b, c = 0;
	
	scanf("%d", &N);
	
	for(int i=1; i<101; i++){
		a += N*i;
	}
	
	for(int i=1; i<N+1; i++){
		b += i*i;
	}
	
	for(int i=1; i<N+1; i++){
		c += i*(N-(i-1));
	}
	

	printf("%d\n%d\n%d", a, b, c);
	
}

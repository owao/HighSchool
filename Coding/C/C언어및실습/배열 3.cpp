#include <stdio.h>
#include <stdlib.h>

#define N 10

int main(){
	int A[N] = {0};
	int a,b,c, index;
	scanf("%d %d %d", &a, &b, &c);
	
	int d = a*b*c;
	
	while(d!=0){
		index = d%10;
		A[index]++;
		d/=10;
	}
	
	for(int i=0; i<N; i++){
		printf("%d ", A[i]);
	}
	printf("\n");

}

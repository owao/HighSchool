#include <stdio.h>
#include <stdlib.h>


int main(){
	
	int N;  //배열 크기 
	int sum = 0;
	scanf("%d", &N);
	
	int A[N] = {0};
	int B[N] = {0};
	for(int i=0; i<N; i++){
		scanf("%d", &A[i]);
	}
	
	for(int i=0; i<N; i++){
		for(int j=0; j<i+1; j++){
			sum += A[j];
		}
		sum = sum/(i+1);
		B[i] = sum;
		sum = 0;
	}
	
	for(int i=0; i<N; i++){
		printf("%d ", B[i]);
	}

}

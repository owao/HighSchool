#include <stdio.h>
#include <stdlib.h>

void DecToBin(int A[], int N){
	for(int i=0; i<8; i++){
		A[7-i] = N%2;
		N=N/2;
	}
	
	for(int i=0; i<8; i++){
		printf("%d", A[i]);
	}
	printf("\n");
}

void BinToDec(int *A){
	int k, sum = 0;
	for(int i=0; i<8; i++){
		for(int j=0; j<i+1; j++){
			if(j==0){
				k=1;
			}
			k *= 2;
		}
		sum += A[7-i]*k/2;
	}
	printf("%d", sum);
}

int main(){
	
	int N;
	int A[8];
	scanf("%d", &N);
	
	DecToBin(A, N);
	BinToDec(A);
}

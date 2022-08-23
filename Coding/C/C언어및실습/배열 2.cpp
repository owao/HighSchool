#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define SIZE 100
#define ROWS 3
#define COLS 5

void makeArray(int A[], int r, int c){
	srand(time(NULL));
	for(int i=0; i<r; i++){
		for(int j=0; j<c; j++)
			A[i][j] = rand() % 90 +10;
	}
}

void printArray(int A[], int r, int c){
	for(int i=0; i<r; i++){
		for(int j=0; j<c; j++)
			printf("%d ", A[i][j]);
		printf("\n");
}

void sumOfRowsCols(int A[], int r, int c){
	int rSum, cSum;
	for(int i=0; i<r; i++){
		rSum=0;
		for(int j=0; j<c; j++){
			rSum += A[i][j];
		}
		printf("%d ", rSum);
	}
	printf("\n");
	
	for(int i=0; i<c; i++){
		cSum=0;
		for(int j=0; j<r; j++){
			cSum += A[j][i];
		}
		printf("%d ", cSum);
	}
	printf("\n");
}

int main(){
   int A[ROWS][COLS];
   int r,c;
   scanf("%d %d", &r, &c);
   
   makeArray(A,r,c);
   printArray(A,r,c);
   sumOfRowsCols(A,r,c);
   
}

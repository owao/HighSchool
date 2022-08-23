#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int getAverage(int list[], int n){
	int sum=0;
	for(int i=0; i<n; i++){
		sum += list[i];
	}
	return sum/n;
}

int main(void){
	int avg;
	int score[3][3]={
		{98, 82, 64},
		{88, 90, 82},
		{94, 70, 76}	
	};
	for(int i=0; i<3; i++){
		avg = getAverage(score[i], 3);
		printf("%dÇàÀÇ Æò±Õ = %d \n", i, avg);
	}
	return 0; 
} 

#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main(void){
	
	int sum;
	int arr[5][6]={
		{1, 2, 3, 4, 5, 0},
		{6, 7, 8, 9, 10, 0},
		{11, 12, 13, 14, 15, 0},
		{16, 17, 18, 19, 20, 0},
		{0, 0, 0, 0, 0, 0}
	};
	
	//가로줄
	for(int i=0; i<4; i++){
		sum=0;
		for(int j=0; j<5; j++){
			sum+=arr[i][j];
		}
		arr[i][5]=sum;
	} 
	
	//세로줄
	for(int i=0; i<6; i++){
		sum=0;
		for(int j=0; j<4; j++){
			sum+=arr[j][i];
		}
		arr[4][i]=sum;
	}
	
	//출력 
	for(int i=0; i<5; i++){
		printf("%d %d %d %d %d %d\n", arr[i][0], arr[i][1], arr[i][2], arr[i][3], arr[i][4], arr[i][5]);
	}
}
/*
	fgets(str, sizeof(str), stdin);	

	char *token[SIZE];

	token[0]=strtok(str, " ");
	while(token[i] != NULL){
		i++
		token[i]=strtok(NULL, " \n");
	}
*/ 

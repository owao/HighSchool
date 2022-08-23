#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int duplicate(int num, int lotto[], int cnt){
	
	//lotto에 cnt만큼 값 생성 
	int k;
	srand(time(NULL));
	for(int i=0; i<cnt; i++){
		k=0;
		lotto[i] = rand() % 45 + 1;
		//중복 값 검사 
		for(int j=0; j<i; j++){
			if(lotto[i]==lotto[j]){
				--i;
			}
		}
	}
	
	//로또 번호 출력 
	printf("로또 당첨 번호: ");
	for(int i=0; i<cnt; i++){
		printf("%d ", lotto[i]);
	}
	
	//lotto 안에 num이 있는지 검사
	for(int i=0; i<cnt; i++){
		if(lotto[i]==num){
			return 1;
		}
	}	
	return 0;


}

int main(int argc, char *argv[]){
	
	int num = 25;
	int lotto[6];
	int cnt = 6;
	int returnValue; 
	
	returnValue = duplicate(num, lotto, cnt);
	
	if(returnValue){
		printf("\n%d은 당첨번호에 존재합니다.", num);
	}
	else{
		printf("\n%d은 당첨번호에 존재하지 않습니다.", num);
	}
	
	return 0;
}

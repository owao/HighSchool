#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int duplicate(int num, int lotto[], int cnt){
	
	//lotto�� cnt��ŭ �� ���� 
	int k;
	srand(time(NULL));
	for(int i=0; i<cnt; i++){
		k=0;
		lotto[i] = rand() % 45 + 1;
		//�ߺ� �� �˻� 
		for(int j=0; j<i; j++){
			if(lotto[i]==lotto[j]){
				--i;
			}
		}
	}
	
	//�ζ� ��ȣ ��� 
	printf("�ζ� ��÷ ��ȣ: ");
	for(int i=0; i<cnt; i++){
		printf("%d ", lotto[i]);
	}
	
	//lotto �ȿ� num�� �ִ��� �˻�
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
		printf("\n%d�� ��÷��ȣ�� �����մϴ�.", num);
	}
	else{
		printf("\n%d�� ��÷��ȣ�� �������� �ʽ��ϴ�.", num);
	}
	
	return 0;
}

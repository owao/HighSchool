#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SIZE 100

int strChr(char* s, char c){
	
	int count=0;
	for(int i=0; i<strlen(s); i++){
		//���ڿ��� ������ �ƴϸ� tmp�� ���� 
		if(s[i]==c){
			count++;
		}
	} 
	return count;
	
}

int main(void){
	char str[SIZE];
	char chr;
	
	fgets(str, sizeof(str), stdin);
	scanf("&c", &chr);
	printf("%d\n", strChr(str,chr));
	return 0; 
} 

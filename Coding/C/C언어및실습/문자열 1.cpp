#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SIZE 100

void deleteSpace(char s[]){
	
	char tmp[SIZE];  //공백이 제거된 문자열을 기억할 배열
	int k=0;
	for(int i=0; i<strlen(s); i++){
		//문자열이 공백이 아니면 tmp에 저장 
		if(s[i]!=' '){
			tmp[k]=s[i];
			k++;
		}
	} 
	strcpy(s,tmp);
}

int main(void){
	char str[SIZE];
	fgets(str, sizeof(str), stdin);  //문자열 입력 함수
	deleteSpace(str);
	printf("%s\n", str);
	return 0; 
} 

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SIZE 100

void deleteSpace(char s[]){
	
	char tmp[SIZE];  //������ ���ŵ� ���ڿ��� ����� �迭
	int k=0;
	for(int i=0; i<strlen(s); i++){
		//���ڿ��� ������ �ƴϸ� tmp�� ���� 
		if(s[i]!=' '){
			tmp[k]=s[i];
			k++;
		}
	} 
	strcpy(s,tmp);
}

int main(void){
	char str[SIZE];
	fgets(str, sizeof(str), stdin);  //���ڿ� �Է� �Լ�
	deleteSpace(str);
	printf("%s\n", str);
	return 0; 
} 

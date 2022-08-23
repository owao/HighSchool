#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SIZE 100

int word(char* s){
	
	int count=0;
	for(int i=0; i<strlen(s); i++){
		if(s[i]==' '){
			count++;
		}
	} 
	return count+1;
	
}

void change(char*s, int k){
	char* token[SIZE];
	int i=0;
	
	token[i]=strtok(s, " ");
	while(token[i]!=NULL){
		i++;
		token[i]=strtok(NULL, " \n");
	}
	
	for(int j=i-1; j>=0; j--){
		printf("%s ", token[j]);
	}
}

int main(void){
	char str[SIZE];
	int k;
	
	fgets(str, sizeof(str), stdin);
	k=word(str);
	change(str, k);
	return 0; 
} 

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SIZE 100

void changeWord(char str[], char change[], char origin[]){
	char* token[SIZE];
	int i=0;
	
	token[i]=strtok(str, " ");
	while(token[i]!=NULL){
		i++;
		token[i]=strtok(NULL, " \n");
	}
	
	for(int j=0; j<i; j++){
		if(strcmp(token[j], origin)==0){
			strcpy(token[j], change);
		}
	}
	
	for(int j=0; j<i; j++){
		printf("%s ", token[j]);
	}
	
}

int main(void){
	char str[SIZE];
	char change[SIZE];
	char origin[SIZE];
	fgets(str, sizeof(str), stdin);	
	fgets(change, sizeof(change), stdin);
	fgets(origin, sizeof(origin), stdin);
	changeWord(str, change, origin);
	return 0; 
} 

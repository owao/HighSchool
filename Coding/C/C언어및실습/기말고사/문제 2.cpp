#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void){
	int *p;
	int size, sum;
	scanf("%d", &size);
	p=(int *)malloc(size*sizeof(int));
	
	for(int i=0; i<size; i++){
		scanf("%d", &p[i]);
	}
	
	for(int i=0; i<size; i++){
		for(int j=i; j<size; j++){
			if(p[i]*2==p[j] || p[i]/2==p[j]){
				sum+=1;
			}
		}
	}
	
	printf("%d", sum);

	free(p);
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

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void setProverb(char** p, int n){
	char *prov[5]={
		"A bad workman always blames his tools.",
		"A bad thing never dies.",
		"A bargain is a bargain.",
		"A barking dog never bites.",
		"A barking dog was never a good hunter."
	};
	*p=prov[n];
}

int main(void){
	char *p;
	int n;
	for(int i=0; i<3; i++){
		scanf("%d", &n);
		setProverb(&p, n);
		printf("Selected: %s \n", p);
	}
	return 0; 
} 

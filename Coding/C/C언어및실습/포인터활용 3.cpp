#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void setMaxPtr(int m[], int size, int **pmax){
	int max;
	max=m[0];
	for(int i=1; i<size; i++){
		if(m[i]>max){
			max=m[i];
		}
	}
	
	*pmax = &max;
}

int main(void){
	int m[50];
	int n;
	scanf("%d", &n);
	
	for(int i=0; i<n; i++){
		scanf("%d", &m[i]);
	}
	
	int *pmax;
	setMaxPtr(m,n,&pmax);
	printf("%d\n", *pmax);
	
	return 0; 
} 

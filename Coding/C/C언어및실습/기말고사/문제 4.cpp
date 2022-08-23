#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void){
	int *p, *q;
	int size1, size2, B;
	
	//기본 배열 
	scanf("%d", &size1);
	p=(int *)malloc(size1*sizeof(int));

	for(int i=0; i<size1; i++){
		scanf("%d", &p[i]);
	}
	
	//위치 바꿈 정보	
	scanf("%d", &size2);
	q=(int *)malloc(size2*sizeof(int));
	
	for(int i=0; i<size2; i++){
		scanf("%d", &q[i]);
	}
	
	//자리 바꾸기
	for(int i=0; i<size2-1; i++){
		//바꿀 자리와 바뀔 자리의 값 받기 
		int a=q[i];
		int b=q[i+1];
		
		B=p[b]; //바뀔 자리 값 백업
		p[b]=p[a];
		p[a]=B;
		
	}
	
	for(int i=0; i<size1; i++){
		printf("%d ", p[i]);
	}
	
}

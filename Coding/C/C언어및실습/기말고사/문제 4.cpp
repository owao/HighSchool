#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void){
	int *p, *q;
	int size1, size2, B;
	
	//�⺻ �迭 
	scanf("%d", &size1);
	p=(int *)malloc(size1*sizeof(int));

	for(int i=0; i<size1; i++){
		scanf("%d", &p[i]);
	}
	
	//��ġ �ٲ� ����	
	scanf("%d", &size2);
	q=(int *)malloc(size2*sizeof(int));
	
	for(int i=0; i<size2; i++){
		scanf("%d", &q[i]);
	}
	
	//�ڸ� �ٲٱ�
	for(int i=0; i<size2-1; i++){
		//�ٲ� �ڸ��� �ٲ� �ڸ��� �� �ޱ� 
		int a=q[i];
		int b=q[i+1];
		
		B=p[b]; //�ٲ� �ڸ� �� ���
		p[b]=p[a];
		p[a]=B;
		
	}
	
	for(int i=0; i<size1; i++){
		printf("%d ", p[i]);
	}
	
}

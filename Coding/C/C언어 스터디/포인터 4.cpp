#include <stdio.h>
#include <stdlib.h>

int main(){
	
	//���� ���� 
	int N;
	scanf("%d", &N);
	int A[N];
	for(int i=0; i<N; i++){
		scanf("%d", &A[i]);
	}
	
	//������
	int k, a, b, c;
	scanf("%d", &k);

		for(int i=0; i<k/2; i++){
			scanf("%d %d", &a, &b);
		}
		//change
		for(int i=a; i<(b-a)/2; i++){
			c = A[a+i];
			A[a+i] = A[b-i];
			A[b-i] = c;
		}
	
	//���
	for(int i=0; i<N; i++){
		printf("%d ", A[i]);
	} 
	
}
